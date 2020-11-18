import time

from googletrans import Translator, LANGUAGES
import keyboard
import pyperclip

translator = Translator()


def print_lang_list():
    for language in LANGUAGES:
        print(language + " - " + LANGUAGES[language])


def get():
    clip = pyperclip.paste()
    return clip


def set(a):
    pyperclip.copy(a)


def tr(lang_from, lang_to):
    keyboard.send('ctrl + x')
    time.sleep(0.1)
    text = get()
    text = translator.translate(text, src=lang_from, dest=lang_to)
    set(text.text)
    keyboard.send('ctrl + v')


def get_language_from():
    lang_from = None
    while not lang_from:
        lang_from = input('Введите шифр языка C которого хотите переводить, для справки введите "help":').strip()
        for language in LANGUAGES:
            if language == lang_from:
                return lang_from
        lang_from = None
        print_lang_list()
        print('Введенный шифр не верный, введите шифр еще раз из списка выше')


def get_language_to():
    lang_to = None
    while not lang_to:
        lang_to = input('Введите шифр языка НА который вы хотите переводить, для справки введите "help"\n').strip()
        for language in LANGUAGES:
            if language == lang_to:
                return lang_to
        lang_to = None
        print_lang_list()
        print('Введенный шифр не верный, введите шифр еще раз из списка выше: \n')


def run(lang_from, lang_to):
    keyboard.add_hotkey("f9", lambda: tr(lang_from, lang_to), suppress=True)
    print('Теперь нажав на клавишу f9, выделенный текст будет вырезан, переведен и вставлен обратно')
    keyboard.wait()


language_from = get_language_from()
language_to = get_language_to()
run(language_from, language_to)


