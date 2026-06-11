from extractor import extract_job_details

sample_description = """
Junior Data Analyst
Location: San Francisco, CA (Hybrid)
Company: TechNova Solutions
Pay: $75,000 - $85,000 / year

About the Role:
We are looking for a Junior Data Analyst to join our operations team. You will be responsible for cleaning datasets, building dashboards, and running ad-hoc SQL queries to support our daily metrics.

Requirements:
- Bachelor's degree in a quantitative field or equivalent experience.
- Proficiency in Python (Pandas, NumPy) and SQL.
- Experience with data visualization tools (Tableau or PowerBI).
- Strong communication and presentation skills.
"""

print("Sending job description to Gemini...")
result = extract_job_details(sample_description)

print("\n--- Extracted Data ---")
# .model_dump_json(indent=2) formats the Pydantic object into readable JSON
print(result.model_dump_json(indent=2))