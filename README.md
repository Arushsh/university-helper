# University Helper 🎓

An AI-powered academic assistant and university advisor application built with a React (Vite + TypeScript) frontend and a Django (Django REST Framework) backend powered by Google Gemini.

---

## 📁 Project Structure

```text
university-helper/
├── myUniApp/          # Frontend (React + TypeScript + Vite + Tailwind CSS / UI components)
├── unihelp/           # Backend (Django + Django REST Framework + Google GenAI SDK)
├── .env.example       # Example environment variables
└── README.md          # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- [Node.js](https://nodejs.org/) (v18+)
- [Python](https://www.python.org/) (v3.10+)
- Google Gemini API Key

---

### 2. Backend Setup (Django)

1. Navigate to the `unihelp` directory:
   ```bash
   cd unihelp
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install django djangorestframework django-cors-headers python-dotenv google-genai
   ```

4. Configure environment variables:
   Copy `.env.example` in the root or create a `.env` file with your Gemini API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver 8000
   ```

The backend API will be available at `http://127.0.0.1:8000/`.

---

### 3. Frontend Setup (React)

1. Navigate to the `myUniApp` directory:
   ```bash
   cd myUniApp
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the Vite development server:
   ```bash
   npm run dev
   ```

The application will be running at `http://localhost:5173/` (or port specified in console).

---

## 🛠️ Tech Stack

- **Frontend:** React, TypeScript, Vite, Tailwind CSS, Lucide Icons
- **Backend:** Python, Django, Django REST Framework, Django CORS Headers
- **AI Integration:** Google Gemini API (`google-genai` SDK)
