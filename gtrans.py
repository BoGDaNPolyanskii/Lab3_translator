from mypackage.gtranslator import TransLate, LangDetect, CodeLang, LanguageList

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

    print("Перевірка функцій модуля gtranslator.py:")

    # Виявлення мови тексту з ймовірністю
    lang_info = LangDetect(text, 'all')
    detected_lang = LangDetect(text, 'lang')
    # print(f"Виявлена мова та ймовірність: {lang_info}")

    # Отримання коду мови для перекладу за допомогою функції CodeLang
    lang_code = CodeLang(detected_lang)  # Автоматичне визначення коду мови

    # Переклад тексту на англійську
    translated_text = TransLate(text, lang_code, 'en')
    # print(f"\nТекст для перекладу: {text}")
    # print(f"Переклад на англійську: {translated_text}")

    if output_mode == "file":
        # Формування тексту для збереження в файл translation_results.txt
        output_content2 = f"""
Текст для перекладу: {text}
Переклад на англійську: {translated_text}
Виявлена мова та ймовірність: {lang_info}
        """

    # Виведення на екран
    if output_mode == "screen":
        print(f"\nТекст для перекладу: {text}")
        print(f"Виявлена мова та ймовірність: {lang_info}")
        print(f"Переклад на англійську: {translated_text}")
        # Виведення таблиці мов з перекладом
        result = LanguageList("screen", text)

        if result is None:
            print("Ok")
        else:
            print(f"Помилка: {result}")

    elif output_mode == "file":
        print(f"\nТекст для перекладу: {text}")
        print(f"Виявлена мова та ймовірність: {lang_info}")
        print(f"Переклад на англійську: {translated_text}")
        # Виведення таблиці мов з перекладом
        result = LanguageList("screen", text)
        save_to_file(output_file, output_content2)
    else:
        print("Невірний режим виведення.")

if __name__ == "__main__":
    main()