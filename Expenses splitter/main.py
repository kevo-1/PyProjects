def Splitter(num_people: int, Total_Expenses: float, curr: str) -> None:

    if num_people <= 1:
        raise ValueError('Number of people should be greater than 1')

    Per_person: float = Total_Expenses/num_people

    print('*'*20)
    print('Number of people : {}'.format(num_people))
    print('Total Expenses : {} {}'.format(Total_Expenses, curr))
    print('Each person should pay : {} {}'.format(Per_person, curr))
    print('*'*20)


def main() -> None:
    validPeople: bool = False
    while True:
        if validPeople is not True:
            try:
                nPeople: int = int(input('Enter the total number of people: '))
                validPeople = True
            except ValueError:
                print('Please enter valid number of people')
                continue
        try:
            totalExpenses: float = float(
                input('Enter the total of expenses: '))
            break
        except ValueError:
            print('Please enter valid number of expenses')

    currency: str = input('Enter your currency: ')
    Splitter(num_people=nPeople, Total_Expenses=totalExpenses, curr=currency)


if __name__ == '__main__':
    main()
