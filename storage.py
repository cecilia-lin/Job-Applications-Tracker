import csv
import json
import os
from collections import Counter
from extractor import JobApplication

# Our two database files
CSV_FILE = "applications.csv"
RAW_DB_FILE = "raw_descriptions.jsonl"

FIELDNAMES = ["company", "job_title", "location", "pay", "status", "date_applied", "skills"]

def save_application(job: JobApplication, raw_text: str, csv_filename: str = CSV_FILE, raw_filename: str = RAW_DB_FILE):
    """Saves parsed data to CSV and the raw description to a JSONL database."""
    
    # --- 1. SAVE TO CSV ---
    file_exists = os.path.isfile(csv_filename)
    with open(csv_filename, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()
            
        row = job.model_dump(exclude={"is_valid_job"})
        row['skills'] = ", ".join(row['skills']) 
        writer.writerow(row)
        print(f"Saved metadata for {job.company} to {csv_filename}")

    # --- 2. SAVE TO RAW DATABASE (JSONL) ---
    # Create a dictionary tying the raw text to its basic identifiers
    raw_record = {
        "company": job.company,
        "job_title": job.job_title,
        "date_applied": job.date_applied,
        "raw_text": raw_text
    }
    
    # Append it as a single, serialized string ending with a newline
    with open(raw_filename, mode='a', encoding='utf-8') as f:
        f.write(json.dumps(raw_record) + "\n")
    print(f"Saved raw description to {raw_filename}")

def update_status(company_name: str, new_status: str, filename: str = CSV_FILE) -> bool:
    """Finds an application by company name and updates its status in the CSV."""
    if not os.path.isfile(filename):
        print("No applications file found.")
        return False

    updated = False
    rows = []
    
    with open(filename, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['company'].lower() == company_name.lower():
                row['status'] = new_status
                updated = True
            rows.append(row)
            
    if updated:
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Updated status for {company_name} to '{new_status}'")
        return True
    else:
        print(f"Could not find an application for '{company_name}'.")
        return False

def view_dashboard(filename: str = CSV_FILE):
    """Reads all saved jobs and prints a summary dashboard of statuses and skills."""
    if not os.path.isfile(filename):
        print("No applications file found.")
        return
        
    total_applications = 0
    status_counts = Counter()
    all_skills = []
    
    with open(filename, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_applications += 1
            # Tally the status (e.g., 'Applied', 'Interview Scheduled', 'Rejected')
            status_counts[row['status']] += 1
            
            # Tally the skills
            if row['skills']:
                job_skills = [skill.strip() for skill in row['skills'].split(",")]
                all_skills.extend(job_skills)
                
    # --- Print the Dashboard ---
    print("\n" + "="*35)
    print(" JOB APPLICATION DASHBOARD ")
    print("="*35)
    print(f"Total Applications Tracked: {total_applications}")
    
    print("\n--- Pipeline Status ---")
    for status, count in status_counts.items():
        # Calculate the percentage for each status
        percentage = (count / total_applications) * 100
        print(f"{status}: {count} ({percentage:.1f}%)")

    if all_skills:
        skill_counts = Counter(all_skills)
        print("\n--- Top 5 Demanded Skills ---")
        for skill, count in skill_counts.most_common(5):
            print(f"{skill}: {count} occurrences")
    print("="*35 + "\n")