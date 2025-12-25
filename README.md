# Secure Identity Hub & Loan Approval System

This project contains a comprehensive banking system comprising a **Secure Identity Hub** frontend and a **Loan Approval Prediction** backend.

## Project Structure

- `frontend/`: React/Vite application for the user interface.
- `backend/`: FastAPI application for loan prediction and user management.
- `sql/`: Database scripts.

## Prerequisites

- **Python 3.8+**
- **Node.js 16+** & **npm**
- **PostgreSQL** (running locally)

## Setup Instructions

### 1. Database Setup
1.  Ensure PostgreSQL is running.
2.  Create a database named `loan_app_db` (or update `.env` with your preferred name).
3.  The application is pre-configured to connect to `postgresql+asyncpg://postgres:Padma%40123@localhost/loan_app_db` via the included `.env` file.
    > **Note**: If your PostgreSQL credentials differ, update the `.env` file in the root directory.

### 2. Backend Setup
Navigate to the root directory and install Python dependencies:

```bash
pip install -r backend/requirements.txt
```

Initialize the database tables:

```bash
python backend/create_tables.py
```

Start the backend server:

```bash
uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000`.

### 3. Frontend Setup
Open a new terminal, navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`.

## Features
- **User Authentication**: Secure signup and login.
- **Loan Prediction**: AI-powered loan eligibility assessment.
- **Dashboard**: View loan status and history.

## Deployment
This repository is configured to include the `.env` file for ease of setup. **Do not use these credentials in a production environment.**
