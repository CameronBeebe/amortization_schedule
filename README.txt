prompt:

"Please generate a python script for a loan amortization schedule.  I should be able to use the command line (e.g. argparse) to adjust parameters (interest rate, principal, amortization years) so that a new file is created for a loan fitting those parameters inside the project directory.  (E.g. loan_50k_6pct_30yr.py)"

example usage:

python amortization_generator.py --principal 50000 --rate 6 --years 30
