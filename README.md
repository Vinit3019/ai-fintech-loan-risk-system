# 🧠 AI Fintech Loan Risk System

An end-to-end AI-powered loan risk assessment system that combines **Machine Learning (ML)** and **Large Language Models (LLMs)** to automate loan approval decisions with intelligent, human-like explanations.

---

## 🚀 Features

* ✅ Loan approval prediction using ML (Random Forest)
* 🤖 AI-generated explanations using LLM
* 📊 Feature importance-based ML explainability
* 💬 Chatbot for financial guidance
* ⚡ FastAPI backend (production-ready APIs)
* 🎨 Streamlit UI for interactive testing

---

## 🏗️ System Architecture

```
User Input (Streamlit UI)
        ↓
FastAPI Backend
        ↓
+---------------------------+
|  ML Model (Scikit-learn) |
|  - Loan Prediction       |
|  - Feature Importance    |
+---------------------------+
        ↓
+---------------------------+
|  LLM (OpenAI API)        |
|  - Risk Explanation      |
|  - Financial Chatbot     |
+---------------------------+
        ↓
Final Response (Decision + Explanation)
```

---

## 📡 API Endpoints

### 🔹 1. Predict Loan Approval

`POST /predict`

```json
{
  "income": 50000,
  "credit_score": 700,
  "loan_amount": 200000
}
```

---

### 🔹 2. AI Explanation (LLM)

`POST /explain`

➡️ Generates human-like reasoning for loan decision

---

### 🔹 3. ML Explainability

`POST /ml-explain`

➡️ Returns feature importance from ML model

---

### 🔹 4. Combined Analysis 🔥

`POST /analyze`

➡️ Returns:

* Loan approval decision
* AI-generated explanation

---

### 🔹 5. Chatbot

`POST /chat`

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Should I take a loan of 200000 with 50000 income?"
    }
  ]
}
```

---

## 🧪 Tech Stack

* Python
* FastAPI
* Scikit-learn
* OpenAI API (LLM)
* Streamlit
* Pandas / NumPy

---

## ⚙️ Setup Instructions

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/ai-fintech-loan-risk-system.git
cd ai-fintech-loan-risk-system

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
OPENAI_API_KEY=your_api_key_here

# Run FastAPI server
uvicorn app.main:app --reload

# Run Streamlit UI
streamlit run app_ui.py
```

---

## 💡 Key Highlights

* 🔥 Combines ML + Generative AI (real-world fintech use case)
* ⚡ Production-ready backend using FastAPI
* 🧠 Explainable AI system (ML + LLM explanations)
* 💬 Conversational financial assistant
* 📊 End-to-end deployment-ready project

---

## 📌 Use Cases

* Loan approval automation
* Credit risk assessment
* Fintech AI platforms
* Banking decision support systems

---

## 👨‍💻 Author

**Vinit S B**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
