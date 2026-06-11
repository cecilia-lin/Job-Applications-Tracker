import argparse
import sys
from extractor import extract_job_details
from storage import save_application, update_status, view_dashboard

def main():
    parser = argparse.ArgumentParser(description="JobTrack: An AI-powered Job Application CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: add
    parser_add = subparsers.add_parser("add", help="Add a new job application")
    parser_add.add_argument("--file", help="Path to a text file containing the job description")
    parser_add.add_argument("--text", help="Directly paste the raw job description text")
        
    # Command: update
    parser_update = subparsers.add_parser("update", help="Update the status of an existing application")
    parser_update.add_argument("company", help="The name of the company")
    parser_update.add_argument("--title", required=True, help="The exact job title of the application")
    parser_update.add_argument("--status", required=True, help="The new status (e.g., 'Interviewing', 'Rejected')")

    # Command: dashboard
    parser_dashboard = subparsers.add_parser("dashboard", help="View your application metrics and top skills")

    args = parser.parse_args()

    # --- Routing the Commands ---
    
    if args.command == "add":
        raw_text = ""
        
        if args.file:
            try:
                with open(args.file, "r", encoding="utf-8") as f:
                    raw_text = f.read()
            except FileNotFoundError:
                print(f"❌ Error: Could not find file '{args.file}'")
                sys.exit(1)
        elif args.text:
            raw_text = args.text
        else:
            print("❌ Error: You must provide either --file or --text")
            sys.exit(1)
            
        print(f"Analyzing job description with Gemini...")

        # Extract job details using the AI model
        job = extract_job_details(raw_text)
        
        if job:
            # Save the extracted job and raw text to storage
            save_application(job, raw_text)
            print(f"✅ Successfully added '{job.job_title}' at {job.company}")
        else:
            print("❌ Failed to extract job details. Please check the input.")
            sys.exit(1)
        
    elif args.command == "update":
        update_status(args.company, args.title, args.status)

    elif args.command == "dashboard":
        view_dashboard()
        
    else:
        # If the user just types 'jobtrack', show them the help menu
        parser.print_help()

if __name__ == "__main__":
    main()