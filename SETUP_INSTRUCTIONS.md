# Setup Instructions

The project has been reorganized into the proper structure. Follow these steps to get it running:

## Project Structure

```
project/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example (copy to .env)
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── brief_agent.py
│   │   ├── copy_agent.py
│   │   ├── creative_agent.py
│   │   ├── resize_agent.py
│   │   └── publisher_agent.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── storage.py
├── frontend/
│   ├── package.json
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.jsx
│       ├── index.js
│       └── index.css
└── .gitignore
```

## Backend Setup

1. **Navigate to backend directory:**
   ```powershell
   cd backend
   ```

2. **Create virtual environment:**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Create .env file:**
   ```powershell
   copy .env.example .env
   ```
   Then edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

5. **Run the backend server:**
   ```powershell
   python main.py
   ```
   Server will run on: http://localhost:8000
   API docs: http://localhost:8000/docs

## Frontend Setup

1. **Navigate to frontend directory:**
   ```powershell
   cd frontend
   ```

2. **Install dependencies:**
   ```powershell
   npm install
   ```

3. **Run the frontend:**
   ```powershell
   npm start
   ```
   Frontend will run on: http://localhost:3000

## Notes

- The backend needs to be running before starting the frontend
- Make sure you have Python 3.9+ and Node.js 16+ installed
- OpenAI API key is required for the copy generation to work
- Social media API credentials are optional (demo mode will be used if not configured)

