from fpdf import FPDF
from datetime import datetime

class LoanReportPDF(FPDF):
    def header(self):
        # Logo placeholder (optional)
        # self.image('logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 20)
        self.set_text_color(5, 150, 105) # Emerald-600 (Green/Teal theme)
        self.cell(0, 10, 'Secure Identity Hub', 0, 1, 'C')
        self.set_font('Arial', '', 12)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'Bank-Grade Loan Eligibility Analysis', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}} | Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(240, 253, 244) # Light green bg
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, f'  {title}', 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 7, body)
        self.ln()

    def add_key_val(self, key, val):
        self.set_font('Arial', 'B', 11)
        self.cell(60, 8, f"{key}:", 0)
        self.set_font('Arial', '', 11)
        self.cell(0, 8, f"{str(val)}", 0, 1)

def generate_loan_report_pdf(application, analysis_result):
    pdf = LoanReportPDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # 1. Applicant Details
    pdf.chapter_title('Applicant Information')
    pdf.add_key_val('Full Name', application.full_name)
    pdf.add_key_val('Email', application.email)
    pdf.add_key_val('Mobile', application.mobile_number)
    pdf.add_key_val('Application ID', application.id)
    pdf.ln(5)

    # 2. Loan Request
    pdf.chapter_title('Loan Request Analysis')
    pdf.add_key_val('Loan Amount', f"Rs. {analysis_result['loan_details']['amount']:,.0f}")
    pdf.add_key_val('Duration', f"{analysis_result['loan_details']['duration_years']} Years")
    pdf.add_key_val('Purpose', analysis_result.get('loan_purpose', 'Personal')) # Assuming added to result, else generic
    pdf.ln(5)

    # 3. Decision & Score
    pdf.chapter_title('AI Decision & Score')
    decision = analysis_result['decision']
    
    # Color coded decision
    pdf.set_font('Arial', 'B', 16)
    if decision == 'APPROVED':
        pdf.set_text_color(0, 128, 0) # Green
    elif decision == 'REJECTED':
        pdf.set_text_color(200, 0, 0) # Red
    else:
        pdf.set_text_color(200, 150, 0) # Orange
        
    pdf.cell(0, 10, f"Status: {decision.replace('_', ' ')}", 0, 1)
    
    pdf.set_text_color(0, 0, 0) # Reset
    pdf.set_font('Arial', '', 12)
    pdf.add_key_val('Approval Probability', f"{analysis_result['approval_probability']}%")
    pdf.add_key_val('Decision Reason', analysis_result['decision_reason'])
    pdf.ln(5)

    # 4. Financial Terms (if approved/pending)
    if decision != 'REJECTED':
        pdf.chapter_title('Proposed Terms')
        pdf.add_key_val('Interest Rate', f"{analysis_result['interest_rate']['annual']}% p.a.")
        pdf.add_key_val('Monthly EMI', f"Rs. {analysis_result['emi']['monthly']:,.0f}")
        pdf.add_key_val('Total Repayment', f"Rs. {analysis_result['emi']['total_repayment']:,.0f}")
        pdf.ln(5)

    # 5. AI Explanations (SHAP)
    pdf.chapter_title('Key Factors Influencing Decision')
    explanations = analysis_result.get('explanations', [])
    if explanations:
        for exp in explanations:
            impact_sign = "(+)" if exp['impact'] == 'positive' else "(-)"
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(10, 6, impact_sign, 0)
            pdf.cell(50, 6, exp['factor'], 0)
            pdf.set_font('Arial', 'I', 10)
            pdf.multi_cell(0, 6, exp['description'])
            pdf.ln(2)
    else:
        pdf.cell(0, 6, "No specific AI explanations available.", 0, 1)
    
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 10, '* This is a computer-generated report and does not require a physical signature.', 0, 1, 'C')

    # Output to bytes
    return pdf.output()
