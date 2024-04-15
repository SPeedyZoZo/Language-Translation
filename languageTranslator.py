from translate import Translator

languages = ['en', 'fr', 'ar']

text = input("What text would you like to translate? >> ")

for language in languages:
    translator = Translator(provider='libre', from_lang='en', to_lang=language)
    translation = translator.translate(text)
    print(f"Translation to {language}: {translation}")