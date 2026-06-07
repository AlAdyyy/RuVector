import os
import sys

def tailor_job_app(master_resume_path, job_description_path, output_dir):
    """
    Automates the process of preparing for a job application by creating the
    directory structure and placing the master resume and job description.

    Note: In a full implementation, this script could call an LLM API to
    perform the tailoring using the Mega-Prompt logic.
    """
    if not os.path.exists(master_resume_path):
        print(f"Error: Master resume not found at {master_resume_path}")
        return

    if not os.path.exists(job_description_path):
        print(f"Error: Job description not found at {job_description_path}")
        return

    os.makedirs(output_dir, exist_ok=True)

    # In this version, we provide the template for the user to follow
    # with their preferred AI assistant.
    print(f"Initializing application in {output_dir}...")

    # Create a 'instructions.txt' for the user
    instructions = f"""
Step 1: Copy the content of {master_resume_path}
Step 2: Copy the content of {job_description_path}
Step 3: Use the Mega-Prompt in docs/mega-prompts/job_application_tailor.md with an AI assistant.
Step 4: Save the output Resume.md and Cover_Letter.md in this directory ({output_dir}).
"""
    with open(os.path.join(output_dir, "automation_instructions.txt"), "w") as f:
        f.write(instructions)

    print("Success! Follow the instructions in automation_instructions.txt to finalize your application.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python tailor_job_app.py <master_resume_path> <job_description_path> <output_dir>")
    else:
        tailor_job_app(sys.argv[1], sys.argv[2], sys.argv[3])
