# Job-Applications-Tracker

A robust command-line tool designed to streamline job hunting for data analysts and engineers. It uses the Gemini LLM to automatically parse unstructured job descriptions (extracting the company, title, salary, location, and technical requirements) and manages data using a dual-storage system (CSV for metadata, JSONL for raw text).

## Features
- **AI-Powered Extraction:** Automatically parses job details from raw text using the Gemini API.
- **Dual-Database Architecture:** Stores processed data in a structured CSV and archives raw descriptions in a JSONL file.
- **CLI-First Workflow:** Easily add, track, and update job applications directly from the terminal.
- **Analytics Dashboard:** Summarize your application status and identify the most demanded skills in your target roles.

## Setup
1. Clone the repository and navigate to the root directory.
2. Ensure you have `uv` installed (`pip install uv`).
3. Create a `.env` file and add your `GEMINI_API_KEY`:
   ```bash
   GEMINI_API_KEY=your_actual_api_key_here
   ```
4. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

### Add a Job Application

**From a text file:**
```bash
python src/main.py add --file path/to/job_description.txt
```

**Paste text directly:**
```bash
python src/main.py add --text "Software Engineer at TechCorp Inc. Location: San Francisco, CA. Salary: $120k-$150k. Requirements: Python, React, PostgreSQL..."
```

The tool will:
- Send the job description to Gemini API for extraction
- Parse company, title, location, salary, and required skills
- Save structured data to `applications.csv`
- Archive raw text to `raw_descriptions.jsonl`

### Update Application Status

Track your progress as you interview:
```bash
python src/main.py update "Company Name" --title "Job Title" --status "Interviewing"
```

Valid statuses: `Applied`, `Interviewing`, `Offer`, `Rejected`, etc.

### View Dashboard

See your application metrics and top in-demand skills:
```bash
python src/main.py dashboard
```

This displays:
- Total applications tracked
- Breakdown by status (Applied, Interviewing, Rejected, etc.)
- Top 10 most-demanded skills across all applications

## Data Files

- **applications.csv** - Structured metadata for all applications
- **raw_descriptions.jsonl** - Raw job posting text linked to each application