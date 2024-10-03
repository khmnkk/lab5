import string

def sort_words(words, ukrainian_alphabet, english_alphabet):
    def clean_word(word):
        return word.strip(string.punctuation)

    def sort_key(word):
        cleaned_word = clean_word(word).lower()
        return [
            ukrainian_alphabet.index(c) if c in ukrainian_alphabet else \
            len(ukrainian_alphabet) + english_alphabet.index(c) if c in english_alphabet else \
            len(ukrainian_alphabet) + len(english_alphabet)  # Для символів, які не належать жодному алфавіту
            for c in cleaned_word
        ]

    return sorted(words, key=sort_key)

def read_file_and_sort(file_path):
    ukrainian_alphabet = 'абвгґдеєжззиійклмнопрстуфхцчшщьюя'
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            print("Заданий список:")
            print(text)

            words = eval(text)

            ukrainian_words = [word for word in words if any(char in ukrainian_alphabet for char in word)]
            english_words = [word for word in words if all(char in english_alphabet for char in word.lower())]

            sorted_ukrainian = sort_words(ukrainian_words, ukrainian_alphabet, english_alphabet)
            sorted_english = sort_words(english_words, ukrainian_alphabet, english_alphabet)
            sorted_words = sorted_ukrainian + sorted_english

            print("\nВідсортований список:")
            print(sorted_words)

            total_words = len(words)
            print(f"\nКількість слів: {total_words}")

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

file_path = 'C:/Users/wvs/Desktop/Python/lab5/text.txt'
read_file_and_sort(file_path)
