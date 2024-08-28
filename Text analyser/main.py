import tkinter
from tkinter import filedialog
import collections
import re

def open_file() -> str:
    tkinter.Tk().withdraw()
    path: str = filedialog.askopenfilename()
    if path:
        with open(path, 'r') as file:
            text: str = file.read()
            return text
    return ""

def Analyse(text: str) -> dict[str , int]:
    result: dict[str , int] = {
        'total_characters' : len(text.replace(' ','')),
        'total_words': len(text.split()),
        'total_numbers': sum(c.isdigit() for c in text),
        'total_whitespaces': text.count(' ')
    }

    return result

def Top_5(text: str) -> list[tuple[str,int]]:
    lowered: str = text.lower()
    reg: str = r'\b\w+\b'
    words: list[str] = re.findall(reg, lowered)
    word_count: collections.Counter = collections.Counter(words)
    return word_count.most_common(n=5)


def main() -> None:
    Text: str = open_file()
    analyzation: dict[str , int] = Analyse(text=Text)
    most_common: list[tuple[str,int]] = Top_5(text=Text)

    print('*'*30)
    print(f'The original text: {Text}\n')
    print('This file contains: ')
    print(f'Total words: {analyzation['total_words']}')
    print(f'Total letters: {analyzation['total_characters']}')
    print(f'Total spaces: {analyzation['total_whitespaces']}')
    print(f'Total digits: {analyzation['total_numbers']}\n')
    print('The 5 most common words are: ')
    for first,second in most_common:
        print(f'  {first}: {second}')
    print('*'*30)

if __name__ == '__main__':
    main()