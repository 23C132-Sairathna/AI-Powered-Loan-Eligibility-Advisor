# AI-Powered Loan Eligibility Advisor

This project is an AI-driven web application that predicts a user’s loan approval probability and provides clear, explainable insights. It streamlines the loan evaluation workflow by combining machine learning, explainable AI, and an interactive financial chatbot.

# Overview

The system allows applicants to enter financial details and instantly receive:

Loan eligibility prediction

Key factor explanations

A downloadable PDF decision report

Guidance from an integrated financial chatbot

Built using Python, Streamlit, and NLP models, the platform improves transparency in loan decisions and supports users with real-time insights.

# Core Features

Loan Approval Prediction
ML models evaluate credit score, income, loan history, and other inputs to determine approval probability.

Explainable AI
SHAP-based visualizations show how each feature influenced the final prediction.

PDF Report Generation
Each evaluation generates a professional, downloadable credit appraisal report.

Financial Chatbot
NLP-powered chatbot helps users understand EMI concepts, credit impact, and rejection reasons.

# System Modules

Data Ingestion & Preprocessing
Collect user inputs, clean data, encode categories, and build preprocessing pipelines.

Model Training & Inference
Train and tune models (Logistic Regression, Random Forest, XGBoost), evaluate performance, and generate predictions.

Explainability & Reporting
Generate SHAP plots and compile user-specific PDF summaries.

Chatbot Integration & Deployment
Incorporate transformer-based chatbot and deploy the end-to-end system on Streamlit Cloud or similar platforms.

# Milestones

Milestone 1: Input form creation, data cleaning, and exploratory analysis

Milestone 2: Model development, evaluation, and threshold tuning

Milestone 3: Explainable AI integration and PDF report generation

Milestone 4: Chatbot integration and final deployment

# Outcome

The finished system acts as a fast, transparent, and user-friendly loan eligibility advisor—benefiting both applicants and financial institutions.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
