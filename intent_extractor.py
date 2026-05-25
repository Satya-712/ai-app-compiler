from api_schema_generator import generate_api_schema
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

from schemas import IntentSchema
from validator import validate_output
from repair_engine import repair_output
from system_designer import generate_system_design
from db_schema_generator import generate_db_schema

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def extract_intent(user_prompt):

    prompt = f"""
    Convert the following app request into STRICT structured JSON.

    User Request:
    {user_prompt}

    RULES:
    1. Always return valid JSON only
    2. Never leave fields empty
    3. Infer reasonable roles/features if missing
    4. Return complete structured data

    Return format:

    {{
      "app_name": "",
      "modules": [],
      "roles": [],
      "features": []
    }}
    """

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    raw_output = response.choices[0].message.content

    data = json.loads(raw_output)

    errors = validate_output(data)

    if errors:
        print("Validation Errors:", errors)

        data = repair_output(data)

    validated = IntentSchema(**data)

    design = generate_system_design(data)

    db_schema = generate_db_schema(data)
    api_schema = generate_api_schema(data)

    print("\nAPI SCHEMA:\n")
    print(json.dumps(api_schema, indent=2))

    print("\nSYSTEM DESIGN:\n")
    print(json.dumps(design, indent=2))

    print("\nDATABASE SCHEMA:\n")
    print(json.dumps(db_schema, indent=2))

    return validated.model_dump_json(indent=2)


if __name__ == "__main__":

    user_input = input("Enter app idea: ")

    result = extract_intent(user_input)

    print("\nFINAL VALIDATED OUTPUT:\n")
    print(result)