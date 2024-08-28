from morsedict import morsecode

def english_to_morse(text: str) -> str:
    translated: str = ' '.join(morsecode.get(letter.upper(),'') for letter in text)
    return translated

def reverse_dict(morsecode: dict)-> dict:
    return {value: key for key,value in morsecode.items()}

def morse_to_english(text: str) -> str:
    to_use: dict = reverse_dict(morsecode= morsecode)
    translated_words: list[str] = [''.join(to_use.get(letter, '') for letter in word.split(' '))for word in text.split('   ')]
    return ' '.join(translated_words)

def main() -> None:
    Morse_to_english: bool = False
    if input('Do you want to translate from English or Morse? (e/m)') == 'm':
        Morse_to_english = True
    text: str = input("Enter the text you want to translate: ")
    if Morse_to_english:
        translated: str = morse_to_english(text= text)
    else:
        translated: str = english_to_morse(text=text)
    print(translated.capitalize())


if __name__ == '__main__':
    main()