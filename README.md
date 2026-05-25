# 🚀 AI App Compiler

AI-powered multi-stage application compiler that converts natural language prompts into structured system architecture, API schemas, database schemas, and executable configurations.

Built using:
- FastAPI
- Streamlit
- OpenRouter LLM APIs
- Pydantic Validation

---

# 🧠 Problem Statement

This project acts like a software compiler:

Natural Language Prompt
→ Intent Extraction
→ System Design
→ API Schema Generation
→ Database Schema Generation
→ Validation
→ Repair Engine
→ Final Executable Configuration

Example Prompt:

```bash
Build ecommerce app with seller buyer payments analytics
```
# ⚙️ Features
✅ Multi-stage AI pipeline
✅ Intent extraction engine
✅ System architecture generator
✅ API schema generation
✅ Database schema generation
✅ Validation + repair engine
✅ Deterministic structured JSON output
✅ FastAPI backend
✅ Streamlit frontend
✅ Download generated JSON

# 🏗️ Architecture
User Prompt
   ↓
Intent Extractor
   ↓
System Designer
   ↓
API Schema Generator
   ↓
Database Schema Generator
   ↓
Validator
   ↓
Repair Engine
   ↓
Final Structured Output
📂 Project Structure
ai-app-compiler/
│
├── app.py
├── main.py
├── intent_extractor.py
├── system_designer.py
├── api_schema_generator.py
├── db_schema_generator.py
├── validator.py
├── repair_engine.py
├── schemas.py
├── requirements.txt
└── README.md
# ▶️ Run Locally
Install dependencies
pip install -r requirements.txt
Run FastAPI Backend
python -m uvicorn main:app --reload

Backend URL:

http://127.0.0.1:8000

# Swagger Docs:

http://127.0.0.1:8000/docs
Run Streamlit Frontend
python -m streamlit run app.py
🧪 Example Output
{
  "app_name": "Ecommerce App",
  "modules": [
    "Seller",
    "Buyer",
    "Payments",
    "Analytics"
  ],
  "roles": [
    "Seller",
    "Buyer"
  ],
  "features": [
    "Payment Processing",
    "Sales Analytics"
  ]
}
# 🔍 Validation & Repair Engine

The system validates:

Missing fields
Invalid structures
Schema mismatches
Inconsistent outputs

If issues are found:

Automatic repair is triggered
Failed sections are regenerated
# 📊 Evaluation Focus

This project focuses on:

Reliability
Structured generation
Consistency
Execution awareness
Deterministic outputs
# 👨‍💻 Author

B. Satyanarayana
AI & Data Science Student
Aspiring AI Engineer


AFTER SAVE 

# Run these commands:

```bash
git add .
git commit -m "Updated professional README"
git push
```
