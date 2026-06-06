import streamlit as st
import os
import time
import json
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Database Setup
DB_PATH = "esl_professor.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, level TEXT, context TEXT, goals TEXT, confidence REAL, trajectory TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS sessions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, summary TEXT, takeaways TEXT, created_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS error_patterns
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, error_type TEXT, frequency INTEGER, severity TEXT, cause TEXT, last_seen TEXT)''')
    conn.commit()
    conn.close()

init_db()

def get_student(name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE name=?", (name,))
    row = c.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0], "name": row[1], "proficiency_level": row[2],
            "professional_context": row[3], "learning_goals": json.loads(row[4] or "[]"),
            "confidence_level": row[5], "engagement_trajectory": row[6]
        }
    return None

def save_student(profile):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    existing = get_student(profile["name"])
    goals_json = json.dumps(profile["learning_goals"])
    if existing:
        c.execute("UPDATE students SET level=?, context=?, goals=?, confidence=?, trajectory=? WHERE name=?",
                  (profile["proficiency_level"], profile["professional_context"], goals_json,
                   profile["confidence_level"], profile["engagement_trajectory"], profile["name"]))
    else:
        c.execute("INSERT INTO students (name, level, context, goals, confidence, trajectory) VALUES (?, ?, ?, ?, ?, ?)",
                  (profile["name"], profile["proficiency_level"], profile["professional_context"],
                   goals_json, profile["confidence_level"], profile["engagement_trajectory"]))
    conn.commit()
    conn.close()

def get_past_summaries(student_id, limit=3):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT summary, created_at FROM sessions WHERE student_id=? ORDER BY created_at DESC LIMIT ?", (student_id, limit))
    rows = c.fetchall()
    conn.close()
    return [{"summary": row[0], "date": row[1]} for row in rows]

# Configure Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# App Config
st.set_page_config(page_title="Professor Corrects - Elite ESL Coach", page_icon="🎓", layout="wide")

# Persistent State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "student_profile" not in st.session_state:
    st.session_state.student_profile = {
        "name": "New Student",
        "proficiency_level": "B2",
        "professional_context": "",
        "learning_goals": [],
        "confidence_level": 0.8,
        "engagement_trajectory": "stable"
    }

# Load Mega-Prompt
SYSTEM_PROMPT_TEMPLATE = """# Professor Corrects — Elite ESL Coach Mega-Prompt

## Agent Identity & Persona
- Name: Professor Corrects
- Nationality: British (London-based)
- Accent: Sophisticated London English (British RP with contemporary warmth).
- Voice: Commands attention, builds trust, and makes students stop and listen.
- Credentials: Cambridge MA (English), MEd (SLA), NLP Practitioner, Krashen Theory Specialist.
- Tone: Warm, precise, dry British wit. Corrects with such grace that students feel seen, not shamed.

## Revolutionary Framework: Krashen-NLP Integration
Internal multi-agent reasoning workflow:
1. Analysis Agent: Identifies B2-C1 errors (surface, naturalness, register). Focuses on L1 interference (Thai, Vietnamese, etc.).
2. NLP Diagnosis Agent: Detects representational systems and Affective Filter blocks.
3. Krashen i+1 Calibration: Calibrates feedback to exactly one step beyond current level.
4. Action Plan Deliverer: Creates neurologically-aligned, specific steps.

## Core Mission: The Accent Pivot
While you speak with a sophisticated British RP accent, the ultimate goal for all your students is to sound fluent with a pure American accent. Leverage your British authority to provide elite coaching in Southeast Asia.

## Student Profile & Memory
- Student Name: {name}
- Proficiency Level: {level}
- Professional Context: {context}
- Past Session History: {memory}

## Feedback Structure:
- [What they did RIGHT - celebration]
- [Error analysis - SLA + NLP diagnostic]
- [Why it matters - Krashen i+1 explanation]
- [Natural alternative - Focus on American fluency pathway]
- [Action plan - specific, executable steps]
- [Confidence anchor & encouragement]
"""

def get_professor_response(messages, system_prompt):
    # User requested Gemini 2.5 Pro, falling back to 1.5-pro as it's the current SOTA
    model = genai.GenerativeModel('gemini-1.5-pro')

    chat_messages = [{"role": "system", "parts": [system_prompt]}]

    for msg in messages:
        role = "model" if msg["role"] == "assistant" else "user"
        chat_messages.append({"role": role, "parts": [msg["content"]]})

    response = model.generate_content(
        contents=[m["parts"][0] for m in chat_messages],
        stream=True
    )
    return response

# UI Layout
st.title("🎓 Professor Corrects")
st.subheader("Elite ESL Coaching with Krashen-NLP Integration")

with st.sidebar:
    st.header("Student Profile")
    student_name = st.text_input("Name", st.session_state.student_profile["name"])

    if student_name != st.session_state.student_profile["name"]:
        existing = get_student(student_name)
        if existing:
            st.session_state.student_profile = existing
            st.success(f"Loaded profile for {student_name}")
        else:
            st.session_state.student_profile = {
                "name": student_name,
                "proficiency_level": "B2",
                "professional_context": "",
                "learning_goals": [],
                "confidence_level": 0.8,
                "engagement_trajectory": "stable"
            }

    st.session_state.student_profile["proficiency_level"] = st.selectbox("Proficiency", ["B2", "C1"], index=0 if st.session_state.student_profile["proficiency_level"] == "B2" else 1)
    st.session_state.student_profile["professional_context"] = st.text_input("Context (e.g. Tech PM)", st.session_state.student_profile["professional_context"])

    if st.button("Save Profile"):
        save_student(st.session_state.student_profile)
        st.success("Profile saved!")

    st.divider()
    st.header("Past Sessions")
    student = get_student(st.session_state.student_profile["name"])
    if student:
        past_summaries = get_past_summaries(student["id"])
        for session in past_summaries:
            with st.expander(f"Session {session['date'][:10]}"):
                st.write(session['summary'])
    else:
        st.write("No past sessions found.")

    st.divider()
    st.write(f"Session Timer: 25:00")
    if st.button("Reset Session"):
        st.session_state.messages = []
        if "last_summary" in st.session_state:
            del st.session_state.last_summary
        st.rerun()

    if st.button("End & Summarize Session"):
        with st.spinner("Professor Corrects is reflecting on your progress..."):
            student = get_student(st.session_state.student_profile["name"])
            past_mem = json.dumps(get_past_summaries(student["id"]) if student else [])
            sys_prompt = SYSTEM_PROMPT_TEMPLATE.format(
                name=st.session_state.student_profile["name"],
                level=st.session_state.student_profile["proficiency_level"],
                context=st.session_state.student_profile["professional_context"],
                memory=past_mem
            )

            summary_prompt = "Based on our interaction today, provide a concise summary of the student's progress, 3 key takeaways, and a warm closing remark that anchors their confidence for the next session."
            response = get_professor_response(st.session_state.messages + [{"role": "user", "content": summary_prompt}], sys_prompt)
            summary_text = ""
            for chunk in response:
                summary_text += chunk.text

            if student:
                conn = sqlite3.connect(DB_PATH)
                c = conn.cursor()
                c.execute("INSERT INTO sessions (student_id, summary, created_at) VALUES (?, ?, ?)",
                          (student["id"], summary_text, datetime.now().isoformat()))
                conn.commit()
                conn.close()
            st.session_state.last_summary = summary_text
            st.success("Session summarized and saved!")

if "last_summary" in st.session_state:
    st.info(st.session_state.last_summary)
    if st.button("Clear Summary"):
        del st.session_state.last_summary
        st.rerun()

# Teacher Introduction Section
if not st.session_state.messages:
    with st.expander("Step 1: Teacher Introduction", expanded=True):
        teacher_intro = st.text_area("Introduce the student and the Professor:",
                                   "Dear Professor, I'd like to introduce my student Somchai. We've been working on his business English for the tech sector. He's ready for your feedback.")
        if st.button("Start Live Session"):
            st.session_state.messages.append({"role": "user", "content": f"TEACHER INTRO: {teacher_intro}"})
            st.rerun()

# Chat Interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.messages:
    if prompt := st.chat_input("Student writes here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            try:
                student = get_student(st.session_state.student_profile["name"])
                past_mem = json.dumps(get_past_summaries(student["id"]) if student else [])
                sys_prompt = SYSTEM_PROMPT_TEMPLATE.format(
                    name=st.session_state.student_profile["name"],
                    level=st.session_state.student_profile["proficiency_level"],
                    context=st.session_state.student_profile["professional_context"],
                    memory=past_mem
                )

                if not api_key:
                    full_response = "JULES: Please set your GOOGLE_API_KEY in .env to enable live interaction with the Professor."
                    response_placeholder.markdown(full_response)
                else:
                    response_stream = get_professor_response(st.session_state.messages, sys_prompt)
                    for chunk in response_stream:
                        full_response += chunk.text
                        response_placeholder.markdown(full_response + "▌")
                    response_placeholder.markdown(full_response)
            except Exception as e:
                st.error(f"Error: {str(e)}")

        st.session_state.messages.append({"role": "assistant", "content": full_response})
