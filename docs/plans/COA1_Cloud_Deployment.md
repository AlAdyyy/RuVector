# Course of Action 1: Cloud Deployment (Hugging Face Spaces)

This guide explains how to deploy the Professor Corrects ESL Agent to Hugging Face Spaces for free, providing a live URL for your students.

## Prerequisites
- A Hugging Face account ([huggingface.co](https://huggingface.co/))
- A Google AI Studio API Key ([aistudio.google.com](https://aistudio.google.com/))

## Step-by-Step Deployment

1. **Create a New Space:**
   - Go to Hugging Face and click "New Space".
   - **Name:** `professor-corrects`
   - **SDK:** `Streamlit`
   - **Space Hardware:** `CPU Basic` (Free)
   - **Visibility:** `Public` or `Private` (Private is recommended for boutique coaching).

2. **Add Files:**
   - In your Space, click on the "Files" tab.
   - Upload the following files from `scripts/esl/`:
     - `streamlit_professor_corrects.py` (Rename to `app.py` on Hugging Face).
     - `requirements.txt`
   - The Space will automatically start building.

3. **Configure Secrets:**
   - Go to the "Settings" tab of your Space.
   - Scroll down to "Variables and secrets".
   - Click "New secret".
   - **Key:** `GOOGLE_API_KEY`
   - **Value:** Your Gemini API Key from Google AI Studio.
   - Click "Save".

4. **Persistent Storage (Optional but Recommended):**
   - In the Space "Settings", you can enable "Persistent Storage" (Tier: `Small` or above). This ensures the `esl_professor.db` file is not deleted when the Space restarts, allowing the Professor to remember students indefinitely.

5. **Activation:**
   - Your Space will rebuild. Once complete, you will have a live URL (e.g., `https://huggingface.co/spaces/your-username/professor-corrects`).
   - Open this URL to start your first session.

## Usage in a 25-Minute Session
1. **Teacher Intro:** Open the URL, enter the student's name in the sidebar, and type your introduction in the "Teacher Introduction" box. Click "Start Live Session".
2. **Student Interaction:** Hand the device to the student or share the link. They can now interact live with the Professor.
3. **Persistence:** The student profile is saved to a local SQLite database within the Space. Note: If the Space is restarted, the database may reset unless persistent storage is enabled (requires a small fee). For a completely free experience, session history is kept while the Space is active.
