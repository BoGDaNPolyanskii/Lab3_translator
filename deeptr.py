from mypackage.deeptranslator import TransLate, LangDetect, CodeLang, LanguageList

def save_to_file(filename: str, content: str):
    """Зберігає вміст у файл з вказаним іменем."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Результати були успішно збережені у файл: {filename}")
    except Exception as e:
        print(f"Помилка при збереженні в файл: {e}")

def main():
    text = "Добрий день"
    output_mode = "screen"  # Може бути 'screen' або 'file'
    output_file = "translation_results.txt"

    print("Перевірка функцій з deeptranslator.py:")

    # Виявлення мови тексту
    detected_lang, confidence = LangDetect(text)
    print(f"Виявлена мова: {detected_lang} з вірогідністю {confidence}")

    # Отримання коду мови для перекладу
    lang_code = CodeLang(detected_lang)

    # Переклад тексту на англійську
    translated_text = TransLate(text, detected_lang, 'en')
    print(f"Переклад на англійську: {translated_text}")

    if output_mode == "screen":
        # Виведення таблиці мов з перекладом на всі мови
        LanguageList("screen", text)

    elif output_mode == "file":
        # Формування тексту для збереження у файл
        result = LanguageList("file", text)
        if result:
            save_to_file(output_file, result)

if __name__ == "__main__":
    main()
