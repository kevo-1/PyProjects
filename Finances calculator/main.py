def calculate_finances(monthly_income: float, tax_rate: float, expenses: list[float], currency: str) -> None:
    # All of the calculations are done here:
    monthly_taxed: float = monthly_income * (tax_rate / 100)
    monthly_net: float = monthly_income - monthly_taxed
    monthly_saved: float = monthly_net - sum(expenses)
    yearly_income: float = monthly_income * 12
    yearly_net: float = monthly_net * 12

    # Printing statements are here:
    print('*' * 20)
    print(f'* Monthly Income: {monthly_income} {currency}')
    print(f'* Monthly Tax Rate: {tax_rate}%')
    print(f'* Monthly Net Income: {monthly_net} {currency}')
    print(f'* Monthly Income after expenses: {monthly_saved} {currency} \n')
    print(f'* Yearly Income: {yearly_income} {currency}')
    print(f'* Yearly Net Income: {yearly_net} {currency}')
    print('*' * 20)


def check_user_input(user_input, type_to_check: str) -> bool:
    if type_to_check == 'float':
        try:
            float(user_input)
            return True
        except ValueError:
            return False
    elif type_to_check == 'int':
        try:
            int(user_input)
            return True
        except ValueError:
            return False


def main() -> None:
    monthly_inc = input('Enter your monthly income in numbers: ')
    while not check_user_input(monthly_inc, 'float'):
        monthly_inc = input('Please enter your income in numbers: ')
    tax_rate = input('Enter your tax rate (%): ')
    while not check_user_input(tax_rate, 'float'):
        tax_rate = input('Please enter the tax rate in numbers form (%): ')
    currency: str = input('Enter your currency: ')
    expenses: list[float] = []
    for i in range(int(input('Enter number of expenses for this month: '))):
        expense = input(f'Expense {i+1}: ')
        while not check_user_input(expense, 'float'):
            expense = input(f'Please enter a valid number for Expense {i+1}: ')
        expenses.append(float(expense))
    calculate_finances(monthly_income=float(monthly_inc), tax_rate=float(tax_rate), currency=currency, expenses=expenses)


if __name__ == '__main__':
    main()