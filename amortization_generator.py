import argparse
import os

def calculate_amortization(principal, annual_interest_rate, years):
    monthly_rate = annual_interest_rate / 12 / 100
    num_payments = years * 12
    payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    
    schedule = []
    balance = principal
    for month in range(1, num_payments + 1):
        interest_payment = balance * monthly_rate
        principal_payment = payment - interest_payment
        balance -= principal_payment
        
        schedule.append({
            'Month': month,
            'Payment': payment,
            'Principal': principal_payment,
            'Interest': interest_payment,
            'Remaining Balance': balance
        })
    
    return schedule

def write_schedule_to_file(schedule, filename):
    with open(filename, 'w') as f:
        f.write(f"Month,Payment,Principal,Interest,Remaining Balance\n")
        for entry in schedule:
            f.write(f"{entry['Month']},{entry['Payment']:.2f},{entry['Principal']:.2f},{entry['Interest']:.2f},{entry['Remaining Balance']:.2f}\n")

def main():
    parser = argparse.ArgumentParser(description="Generate a loan amortization schedule.")
    parser.add_argument('--principal', type=float, required=True, help='Loan principal amount (e.g., 50000 for $50,000)')
    parser.add_argument('--rate', type=float, required=True, help='Annual interest rate percentage (e.g., 6 for 6%)')
    parser.add_argument('--years', type=int, required=True, help='Amortization period in years')

    args = parser.parse_args()

    # Generate a unique filename based on the parameters
    filename = f"loan_{int(args.principal)}k_{args.rate:.0f}pct_{args.years}yr.csv"
    
    schedule = calculate_amortization(args.principal, args.rate, args.years)
    write_schedule_to_file(schedule, filename)
    print(f"Amortization schedule saved to {filename}")

if __name__ == "__main__":
    main()
