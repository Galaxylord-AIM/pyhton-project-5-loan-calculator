"""
----> Stage 1
loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

write your code here
print(loan_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)"""
import math

"""
----> Stage 2
def number_of_months(monthly_payment_amount):
    statement = 'It will take '
    month = round(principle / monthly_payment_amount)
    if month == 1:
        statement = statement + str(month) + ' month to repay the loan'
        return statement
    else:
        statement = statement + str(month) + ' months to repay the loan'
        return statement


def monthly_payment_calc(duration):
    statement = 'Your monthly payment = '
    payment = principle / months
    payment_check = str(payment).split('.')
    if int(payment_check[1]) == 0:
        return statement + payment_check[0]
    else:
        last_payment = principle - (duration - 1) * (round(payment) + 1)
        return statement + str(int(payment_check[0]) + 1) + ' and the last payment = ' + str(last_payment)


principle = int(input('''Enter the loan principal:
'''))
selected_option = input('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
''')

if selected_option == 'm':
    monthly_payment = int(input('''Enter the monthly payment:
'''))
    print(number_of_months(monthly_payment))

elif selected_option == 'p':
    months = int(input('''Enter the number of months:
'''))
    print(monthly_payment_calc(months))"""

# ----> Stage 3

# notes
# annuity, interest = float
# payments, periods,principal = int

print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
calculate = input()


# creating function to ask the questions that are required in all the stages
def required_details(string):
    switch = {
        'annuity': 'Enter the annuity payment:\n',
        'interest': 'Enter the loan interest:\n',
        'period': 'Enter the number of periods:\n',
        'principal': 'Enter the loan principal:\n',
        'monthly': 'Enter the monthly payment:\n'
    }
    return switch[string]


def month_to_year_formate(months):
    text = ''
    if months == 1:
        text = '1 month'
    elif months < 12:
        text = str(months) + 'months'
    elif months == 12:
        text = '1 year'
    else:
        years = months // 12
        month = months % 12
        text = str(years) + ' years and ' + str(month) + ' months'

    return 'It will take ' + text + ' to repay this loan!'


if calculate == 'n':
    principle = int(input(required_details('principal')))
    monthly_payments = int(input(required_details('monthly')))
    loan_interest = float(input(required_details('interest')))
    i = loan_interest / (12 * 100)
    print(month_to_year_formate(math.ceil(math.log((monthly_payments / (monthly_payments - i * principle)), (1 + i)))))

elif calculate == 'a':
    principle = int(input(required_details('principal')))
    period = int(input(required_details('period')))
    loan_interest = float(input(required_details('interest')))
    i = loan_interest / (12 * 100)
    print('Your monthly payment =', str(round((principle * ((i * ((1 + i) ** period)) / (((1 + i) ** period) - 1))) + 1)) + '!')
else:

    annuity = float(input(required_details('annuity')))
    period = int(input(required_details('period')))
    loan_interest = float(input(required_details('interest')))
    i = loan_interest / (12 * 100)
    print('Your monthly payment =', str(round((annuity / ((i * ((1 + i) ** period)) / (((1 + i) ** period) - 1))))) + '!')


