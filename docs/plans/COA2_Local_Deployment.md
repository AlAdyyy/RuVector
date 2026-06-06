# Course of Action 2: Local "Professor-in-a-Box" (Local Machine)

This guide explains how to run the Professor Corrects ESL Agent entirely on your local machine for private 1-on-1 sessions with zero hosting costs and maximum data privacy.

## Prerequisites
- Python 3.9 or higher installed.
- A Google AI Studio API Key ([aistudio.google.com](https://aistudio.google.com/)).

## Step-by-Step Setup

1. **Navigate to the ESL Directory:**
   ```bash
   cd scripts/esl
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment:**
   - Create a `.env` file in the `scripts/esl` directory:
     ```bash
     touch .env
     ```
   - Open `.env` and add your Gemini API Key:
     ```env
     GOOGLE_API_KEY=your_gemini_api_key_here
     ```

4. **Launch the Professor:**
   ```bash
   streamlit run streamlit_professor_corrects.py
   ```

5. **Activation:**
   - Streamlit will automatically open your default browser to `http://localhost:8501`.
   - The Professor is now active and ready for the session.

## Advantages of Local Deployment
- **Perfect Precision:** No network latency beyond the Gemini API call.
- **Full Persistence:** The `esl_professor.db` file is stored permanently on your machine, ensuring the Professor remembers students across sessions forever.
- **Zero Cost:** No hosting fees. Only your local electricity and internet.
- **Portability:** You can run this on a laptop during your 1-on-1 coaching in Southeast Asia without needing a public cloud URL.

## Deployment for Offline Use (Advanced)
To make this truly "Professor-in-a-Box," you can package the `scripts/esl` folder into a single executable using tools like `PyInstaller` or simply keep the directory on a USB drive with a portable Python environment.
