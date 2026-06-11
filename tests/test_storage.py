import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from extractor import JobApplication
from storage import save_application, update_status, view_dashboard

def run_tests():
    # Fake raw text inputs
    raw_text_1 = "We are looking for a Data Analyst at Meta. Must know Python, SQL, and Tableau. Pay is $90k."
    raw_text_2 = "Skechers needs a Business Analyst in Manhattan Beach. Use Excel and SQL to improve processes. Pay: $85k."

    job1 = JobApplication(
        is_valid_job=True, company="Meta", job_title="Data Analyst",
        location="Remote", pay="$90k", skills=["Python", "SQL", "Tableau", "Communication"],
    )
    
    job2 = JobApplication(
        is_valid_job=True, company="Skechers", job_title="Business Analyst",
        location="Manhattan Beach, CA", pay="$85k", skills=["Excel", "SQL", "Tableau", "Process Improvement"],
    )

    job3 = JobApplication(
        is_valid_job=True, company="Visa", job_title="Technical Business Analyst",
        location="Austin, TX", pay="$95k", skills=["SQL", "Python", "Agile", "Tableau"],
    )
    save_application(job3, "Visa needs a BA with SQL, Python, Agile, and Tableau. $95k.", "test_db.csv", "test_raw.jsonl")


    print("\n[TEST 1] Saving Applications & Raw Text...")
    save_application(job1, raw_text_1, "test_db.csv", "test_raw.jsonl")
    save_application(job2, raw_text_2, "test_db.csv", "test_raw.jsonl")

    print("\n[TEST 2] Updating Status...")
    update_status("Meta", "Data Analyst", "Interview Scheduled", "test_db.csv")
    update_status("Visa", "Technical Business Analyst", "Interview Scheduled", "test_db.csv")

    print("\n[TEST 3] Viewing Dashboard...")
    view_dashboard("test_db.csv")

if __name__ == "__main__":
    run_tests()