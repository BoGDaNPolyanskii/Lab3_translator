import json
import os
import subprocess
from mypackage.gtranslator import TransLate, LangDetect

def count_words(text):
    return len(text.split())

def count_sentences(text):
    # Рахуємо речення за кількістю крапок, знаків оклику та питань.
    return text.count('.') + text.count('!') + text.count('?')

def process_file(config_file):
    try:
        # Читаємо конфігураційний файл
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)

        text_file = config['text_file']
        dest_language = config['destination_language']
        output = config['output']
        max_characters = config['max_characters']
        max_words = config['max_words']
        max_sentences = config['max_sentences']

        # Перевірка наявності текстового файлу
        if not os.path.exists(text_file):
            print(f"Файл {text_file} не знайдено.")
            return

        # Отримуємо розмір файлу
        file_size = os.path.getsize(text_file)

        # Читаємо текстовий файл
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Виводимо основну інформацію про текст
        num_characters = len(text)
        num_words = count_words(text)
        num_sentences = count_sentences(text)
        detected_lang = LangDetect(text, 'lang')

        print(f"Назва файлу: {text_file}")
        print(f"Розмір файлу: {file_size} байт")
        print(f"Кількість символів: {num_characters}")
        print(f"Кількість слів: {num_words}")
        print(f"Кількість речень: {num_sentences}")
        print(f"Мова тексту: {detected_lang}")

        # Перевіряємо умови обмежень
        if num_characters > max_characters or num_words > max_words or num_sentences > max_sentences:
            print("Текст перевищує вказані обмеження за символами, словами або реченнями.")
            return

        # Перекладаємо текст
        translated_text = TransLate(text, 'auto', dest_language)

        # Виводимо або записуємо результат
        if output == "screen":
            print(f"Переклад на {dest_language}: {translated_text}")
        else:
            output_file = f"{text_file.split('.')[0]}_{dest_language}.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(translated_text)
            print(f"Переклад збережено у файл {output_file}")
            print("Ok")

    except Exception as e:
        print(f"Помилка: {str(e)}")

    # Створюємо файл requirements.txt
    try:
        subprocess.run(['pip', 'freeze', '>', 'requirements.txt'], check=True, shell=True)
        print("Файл requirements.txt успішно створено, в якому зберігаються всі встановлені модулі та пакети.")
    except subprocess.CalledProcessError as e:
        print(f"Помилка при створенні requirements.txt: {str(e)}")

process_file('config.json')