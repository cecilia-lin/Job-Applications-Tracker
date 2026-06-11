import os
import datetime
from google import genai
from google.genai import errors
from pydantic import BaseModel, Field, ValidationError
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

class JobApplication(BaseModel):
    company: str = Field(description="Name of the hiring company. If not found, use 'Unknown'.")
    job_title: str = Field(description="Title of the role. If not found, use 'Unknown'.")
    skills: list[str] = Field(default_factory=list, description="List of required technical and soft skills.")
    location: str | None = Field(description="Location of the job, or 'Remote'.")
    pay: str | None = Field(description="Salary or hourly wage, if listed. Otherwise null.")
    status: str = Field(default="Applied", description="Default status is 'Applied'")
    date_applied: str = Field(
        default_factory=lambda: datetime.date.today().isoformat(),
        description="The date the application was tracked (YYYY-MM-DD)."
    )

def extract_job_details(description_text: str) -> JobApplication | None:
    """
    Takes a job description string, sends it to Gemini, and returns a validated JobApplication object.
    Returns None if the extraction fails.
    """
    # 1. Catch missing API keys before making the call
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not found. Please check your .env file.")
        return None

    client = genai.Client()
    prompt = f"Extract the key details from the following job description:\n\n{description_text}"
    
    try:
        # 2. Add temperature: 0.1 to make the model more factual and less creative
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
                'response_schema': JobApplication,
                'temperature': 0.1, 
            },
        )
        # 3. Validate and return
        return JobApplication.model_validate_json(response.text)
        
    except errors.APIError as e:
        print(f"\n[Extraction Failed] API Error: {e}")
        return None
    except ValidationError as e:
        print(f"\n[Extraction Failed] The model returned improperly formatted data: {e}")
        return None
    except Exception as e:
        print(f"\n[Extraction Failed] An unexpected error occurred: {e}")
        return None