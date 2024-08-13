def Splitter(num_people: int, Total_Expenses: float, curr: str, SplitEqualy: bool, Ratios: list[int]) -> None:
    if num_people <= 1:
        raise ValueError('Number of people should be greater than 1')
    
    print('*' * 20)
    print('Number of people : {}'.format(num_people))
    print('Total Expenses : {:.2f} {}'.format(Total_Expenses, curr))

    if SplitEqualy:
        Per_person: float = Total_Expenses / num_people
        print('Each person should pay : {:.2f} {}'.format(Per_person, curr))
    else:
        for i in range(num_people):
            ToPay = Total_Expenses * (Ratios[i] / 100)
            print(f'Person {i + 1} should pay: {ToPay:.2f} {curr}')
    print('*' * 20)


def main() -> None:
    validPeople: bool = False

    while True:
        if not validPeople:
            try:
                nPeople: int = int(input('Enter the total number of people: '))
                validPeople = True
            except ValueError:
                print('Please enter a valid number of people')
                continue

        try:
            totalExpenses: float = float(input('Enter the total of expenses: '))
            break
        except ValueError:
            print('Please enter a valid number of expenses')

    SplitRatio: list[int] = []
    TempTotal: int = 0
    SplitEqually: bool = False

    if input('Would you like to specify the ratios (y) / Split it equally (n): ') == 'n':
        SplitEqually = True

    if not SplitEqually:
        for i in range(nPeople):
            while True:
                try:
                    ratio: int = int(input(f'Enter the ratio for person {i + 1} (current total ratio = {TempTotal}%): '))
                    if TempTotal + ratio <= 100:
                        TempTotal += ratio
                        SplitRatio.append(ratio)
                        break
                    else:
                        print('The total is greater than 100%. Please re-enter the ratios again!')
                except ValueError:
                    print('Please enter a valid number!')
                    
        if TempTotal < 100:
            SplitRatio[-1] += 100 - TempTotal

    currency: str = input('Enter your currency: ')
    Splitter(num_people=nPeople, Total_Expenses=totalExpenses, curr=currency, SplitEqualy=SplitEqually, Ratios=SplitRatio)


if __name__ == '__main__':
    main()

