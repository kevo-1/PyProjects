from collections import Counter
import re
import docx
import os

def Print_words_counter(words: list[tuple[str, int]]) -> None:
    for word, count in words:
        print(f'{word}: {count}')

def Frequency(Text: str, number_of_words: int) -> list[tuple[str, int]]:
    lowered: str = Text.lower()
    reg: str = r'\b\w+\b'
    words: list[str] = re.findall(reg, lowered)

    word_count: Counter = Counter(words)
    return word_count.most_common(n=number_of_words) if number_of_words != 0 else word_count.most_common()

def main() -> None:
    use_file: bool = False
    choice: int = 0

    while True:
        try:
            choice = int(input("Would you like to read from a file or enter manually (1/2): "))
            if choice != 1 and choice != 2:
                print("Please enter a valid choice!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")

    if choice == 1:
        use_file = True
    
    if not use_file:
        text: str = input("Enter your text: ").strip()
        number_of_words: int = int(input("Enter how many words you want to see (if all enter 0): "))
        word_freq: list[tuple[str, int]] = Frequency(text, number_of_words)
        Print_words_counter(words=word_freq)
    
    else:
        path: str = input("Enter the path to the file: ").strip()
        Number_of_words: int = int(input("Enter how many words you want to see (if all enter 0): "))
        
        if not os.path.exists(path):
            print("File does not exist. Please check the path.")
            return
        
        if path.lower().endswith('.docx'):
            doc = docx.Document(path)
            Words: str = " ".join([para.text for para in doc.paragraphs])
        else:
            while True:
                try:
                    with open(path, 'r', encoding='utf-8') as file:
                        Words: str = file.read()
                except Exception as e:
                    print(f"Error reading the file: {e}")
                    return
        
        word_freq: list[tuple[str, int]] = Frequency(Words, number_of_words=Number_of_words)
        Print_words_counter(words=word_freq)

if __name__ == "__main__":
    main()
