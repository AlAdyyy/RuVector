# AI Job Application Automation Hub

This directory contains the resources and instructions for automating the tailoring of job applications for 'Alex Lomax'.

## Resources
- **Master Resume:** `docs/applications/Alex_Lomax_Master_Resume.md` - The source of truth for Alex's experience.
- **Mega-Prompt:** `docs/mega-prompts/job_application_tailor.md` - The logic used to generate tailored versions.

## How to Automate Your Next Application

Whenever you have a new job post, follow these steps:

1. **Copy the Mega-Prompt:** Open `docs/mega-prompts/job_application_tailor.md`.
2. **Paste into an AI Assistant (like Jules/Claude):** Provide the AI with the content of the Mega-Prompt.
3. **Provide Input Data:**
   - Paste the content of the **Master Resume**.
   - Paste the **Job Description** you are targeting.
4. **Review & Save:**
   - Create a new directory under `docs/applications/[Company]/[Role]/`.
   - Save the generated **Resume.md** and **Cover_Letter.md** there.

## Automation Script
Use `scripts/tailor_job_app.py` to initialize a new application directory. It will generate instructions for using the mega-prompt with an AI assistant to produce your tailored documents.

```bash
python scripts/tailor_job_app.py docs/applications/Alex_Lomax_Master_Resume.md path/to/job_description.txt docs/applications/CompanyName/RoleName
```

## Strategy Notes
- **Linguistic Framing:** Always refer to teaching experience as linguistic expertise.
- **ATS Optimization:** Mirror the exact phrasing used in the job description's "What You'll Do" and "Who You Are" sections.
- **Contact Details:** Always use Alex Lomax's professional contact info provided in the Master Resume.
