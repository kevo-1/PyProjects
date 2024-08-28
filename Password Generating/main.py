import secrets
import string
from enum import Enum

class Strength(Enum):
    Weak = 1
    Fair = 2
    Good = 3
    Strong = 4

class Password:

    def __init__(self, length:int = 12, uppercase: bool = True, symbols:bool = True)-> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        self.base_characters: str = string.ascii_lowercase + string.digits

        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase

        if self.use_symbols:
            self.base_characters += string.punctuation
        

    def generate(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))
        
        return ''.join(password)

    def check_strength(self) -> Strength:
        strength: Strength = Strength.Weak

        if self.length > 16:
            strength = Strength.Fair

        if self.use_uppercase:
            strength = Strength.Good

        if self.use_symbols:
            strength = Strength.Strong

        return strength



def main()-> None:
    num_letters: int = int(input('Enter the length of your desired password: '))
    use_upper: bool = True if input('Would you like to use uppercase letters ? (y/n)') == 'y' else False
    use_symb: bool = True if input('Would you like to use symbols ? (y/n)') == 'y' else False

    password: Password = Password(length=num_letters, uppercase= use_upper, symbols= use_symb)
    generated: str = password.generate()
    strength: Strength = password.check_strength()

    print('*'*20)
    print(f'\nYour generated password : {generated} ({len(generated)} chars)')
    print(f'Your generated password\' strength : {strength.name}\n')
    print('*'*20)


if __name__ == '__main__':
    main()
