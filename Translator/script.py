from translate import Translator

translator = Translator(to_lang='hi')

try:
    with open('./test.txt') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('./trans.txt', mode='w', encoding='utf-8') as file:
            file.write(translation)
except FileNotFoundError as e:
    print('File not found')
