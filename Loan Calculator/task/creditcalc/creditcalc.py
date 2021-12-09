loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'


# write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

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
    print(monthly_payment_calc(months))
