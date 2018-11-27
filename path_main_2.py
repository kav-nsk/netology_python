# Скрипт запуска интернет-браузера двумя способами
#

# Import library
import webbrowser

# Main section
wb = webbrowser.get(using=None)  # получаем данные о объекте-контроллере веббраузера по умолчанию в ОС
wb.open('')                     # применяем метод к объекту.
# или
webbrowser.open('')
