"""
COVID-19 Capital Costs Tax Credit - Eligibility Validation Engine (Simulated)
Author: Alexander Morrison

Description:
This script simulates the compliance logic used on the SaaS backend to screen 
initial applications based on statutory requirements (e.g., NY ESD guidelines).
It validates business size, revenue caps, and qualifying expense dates.
"""

import datetime

# --- Program Statutory Parameters (Configurable based on legislative changes) ---
PROGRAM_START_DATE = datetime.date(2021, 1, 1)
PROGRAM_END_DATE = datetime.date(2022, 12, 31)
MAX_FULL_TIME_EMPLOYEES = 100
MAX_GROSS_RECEIPTS = 2500000.00 # $2.5 Million
MIN_QUALIFYING_EXPENSE = 2000.00

def validate_application(applicant_data):
    """
    Evaluates applicant data against program compliance rules.
    
    Args:
        applicant_data (dict): JSON payload from the SaaS application intake form.
        
    Returns:
        dict: Status ('Approved', 'Denied', 'Manual Review') and reason codes.
    """
    reasons = []
    status = "Approved"

    # 1. Check Business Size (Employee Count)
    if applicant_data.get('fte_count', 0) > MAX_FULL_TIME_EMPLOYEES:
        status = "Denied"
        reasons.append(f"Exceeds maximum FTE limit of {MAX_FULL_TIME_EMPLOYEES}.")

    # 2. Check Gross Receipts Limit
    if applicant_data.get('gross_receipts', 0.0) > MAX_GROSS_RECEIPTS:
        status = "Denied"
        reasons.append(f"Exceeds gross receipts limit of ${MAX_GROSS_RECEIPTS:,.2f}.")

    # 3. Check Qualifying Expenses
    total_expenses = sum(item['amount'] for item in applicant_data.get('expenses', []))
    if total_expenses < MIN_QUALIFYING_EXPENSE:
        status = "Denied"
        reasons.append(f"Total qualifying expenses (${total_expenses:,.2f}) are below the ${MIN_QUALIFYING_EXPENSE:,.2f} minimum.")

    # 4. Check Expense Date Range Compliance
    for expense in applicant_data.get('expenses', []):
        exp_date = datetime.datetime.strptime(expense['date'], "%Y-%m-%d").date()
        if not (PROGRAM_START_DATE <= exp_date <= PROGRAM_END_DATE):
            status = "Manual Review"
            reasons.append(f"Expense '{expense['description']}' dated {exp_date} is outside the statutory timeframe.")

    # 5. Require NYS Business Registration (State Compliance)
    if not applicant_data.get('nys_registered_business', False):
        status = "Denied"
        reasons.append("Applicant must be a registered business operating in New York State.")

    return {
        "status": status,
        "reasons": reasons,
        "calculated_eligible_expenses": total_expenses if status != "Denied" else 0.0
    }

# --- Example Usage for Testing ---
if __name__ == "__main__":
    # Simulated application payload from the frontend dashboard
    sample_application = {
        "business_name": "Main Street Cafe LLC",
        "nys_registered_business": True,
        "fte_count": 12,
        "gross_receipts": 850000.00,
        "expenses": [
            {"description": "HVAC Air Purifier Installation", "amount": 3500.00, "date": "2021-08-15"},
            {"description": "Outdoor Dining Structural Setup", "amount": 5000.00, "date": "2021-04-10"}
        ]
    }

    result = validate_application(sample_application)
    
    print(f"Analyzing Application for: {sample_application['business_name']}")
    print(f"Compliance Status: {result['status']}")
    if result['reasons']:
        print("Notices:")
        for reason in result['reasons']:
            print(f" - {reason}")
    print(f"Total Eligible Capital Costs: ${result['calculated_eligible_expenses']:,.2f}")
