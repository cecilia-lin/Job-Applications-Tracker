import os
import datetime
from google import genai
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

class JobApplication(BaseModel):
    company: str = Field(description="Name of the hiring company")
    job_title: str = Field(description="Title of the role")
    skills: list[str] = Field(description="List of required technical and soft skills")
    location: str | None = Field(description="Location of the job, or 'Remote'")
    pay: str | None = Field(description="Salary or hourly wage, if listed. Otherwise null.")
    status: str = Field(default="Applied", description="Default status is 'Applied'")
    date_applied: str = Field(
        default_factory=lambda: datetime.date.today().isoformat(),
        description="The date the application was tracked"
    )

def extract_job_details(description_text: str) -> JobApplication:
    client = genai.Client()
    
    prompt = f"Extract the key details from the following job description:\n\n{description_text}"
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'response_schema': JobApplication,
        },
    )
    
    return JobApplication.model_validate_json(response.text)
