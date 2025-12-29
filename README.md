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

### 1. Environment Variables Setup (REQUIRED)

**⚠️ SECURITY IMPORTANT:** This project requires environment variables to be configured before running.

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and replace all placeholder values with your actual credentials:
   - **DATABASE_URL**: Your PostgreSQL connection string
   - **JWT_SECRET_KEY**: Generate using `openssl rand -hex 32` (must be 32+ characters)
   - **OPENROUTER_API_KEY**: Get from https://openrouter.ai/

3. **Generate a secure JWT secret key:**
   ```bash
   openssl rand -hex 32
   ```
   Copy the output and paste it as your `JWT_SECRET_KEY` in `.env`

**Example `.env` file:**
```bash
DATABASE_URL=postgresql+asyncpg://postgres:YourActualPassword@localhost/loan_app_db
JWT_SECRET_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
OPENROUTER_API_KEY=sk-or-v1-your-actual-api-key-from-openrouter
```

**🔒 Security Reminders:**
- ❌ **NEVER** commit the `.env` file to Git (it's in `.gitignore`)
- ❌ **NEVER** share your credentials publicly
- ✅ Use different credentials for development and production
- ✅ Rotate secrets regularly (every 90 days)
- ✅ Use strong, randomly generated secrets

### 2. Database Setup
1.  Ensure PostgreSQL is running.
2.  Create a database named `loan_app_db`:
    ```bash
    # Login to PostgreSQL
    psql -U postgres
    
    # Create database
    CREATE DATABASE loan_app_db;
    
    # Exit
    \q
    ```
3.  Update the `DATABASE_URL` in your `.env` file with your PostgreSQL credentials.

### 3. Backend Setup
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

**Note:** If you get environment variable errors, make sure you've properly configured your `.env` file as described in step 1.

### 4. Frontend Setup
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
- **User Authentication**: Secure signup and login with JWT tokens
- **AI-Powered Loan Prediction**: Machine learning-based loan eligibility assessment with SHAP explanations
- **Interactive Dashboard**: Real-time loan status, credit score monitoring, and financial overview
- **Loan Application**: Step-by-step loan application form with AI advisor
- **PDF Report Generation**: Comprehensive RBI-compliant loan analysis reports
- **QR Code Sharing**: Share and download reports on mobile devices
- **Payment Gateway**: Mock payment integration (Card, UPI, Net Banking, Wallets)
- **Profile Management**: Complete user profile and security settings

## Screenshots

### 1. Dashboard - Financial Overview
![Dashboard](screenshots/dashboard.png)
- Real-time credit score monitoring (752/900)
- Active loan tracking with outstanding balance
- AI-powered loan eligibility predictions (₹8,00,000 pre-approved)
- Alerts & notifications center
- AI Credit Advisor chatbot

### 2. My Loans
![My Loans](screenshots/my-loans.png)
- View all active loans with details
- Track loan ID, type, amount, and outstanding balance
- Real-time status updates

### 3. Apply for Loan
![Apply for Loan](screenshots/apply-loan.png)
- AI-Powered Loan Eligibility Advisor
- Personal & Employment information
- Financial details with automatic calculations
- Loan details configuration
- Household information
- Instant eligibility assessment

### 4. Loan Analysis Results
![Loan Analysis](screenshots/loan-analysis.png)
- Comprehensive approval decision (95% approval score)
- Credit score range prediction (710-760)
- Interest rate analysis (12.75%)
- Monthly EMI calculation (₹2,263)
- Total interest breakdown (₹1,35,752)
- Decision factors with AI explanations
- Feature impact analysis
- ML approval score visualization
- Loan cost breakdown chart
- Risk assessment radar chart
- Next steps guidance (KYC, documentation)
- PDF report download & QR code sharing

### 5. Security & Profile Settings
![Profile Settings](screenshots/profile-settings.png)
- Complete account information
- Customer ID: LA26253834
- Email verification status
- Mobile number & address details
- KYC status tracking
- Password management
- Account role information

### 6. Mobile QR Code Download
![QR Code](screenshots/qr-code.png)
- Scan to download report on mobile
- Secure & encrypted link
- 24-hour expiration for security
- Works across all devices

## Deployment
**⚠️ PRODUCTION SECURITY:**
- Never use development credentials in production
- Store production secrets in a secure secrets manager (AWS Secrets Manager, Azure Key Vault, etc.)
- Enable SSL/TLS for all connections
- Use environment-specific `.env` files
- Implement proper access controls and audit logging
- Regularly rotate all credentials
- Never commit any `.env` files to version control
