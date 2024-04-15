import argostranslate.package
import argostranslate.translate

def setup_translation(from_code, to_code):
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package = next((pkg for pkg in available_packages if pkg.from_code == from_code and pkg.to_code == to_code), None)
    if not package:
        print(f"No package available for translating from {from_code} to {to_code}")
        return None
    print(f"Downloading and installing package for {from_code} to {to_code}...")
    package.install()

def translate_text(text, from_code, to_code):
    translation = argostranslate.translate.load_installed_languages()[0].get_translation(from_code, to_code)
    translated_text = translation.translate(text)
    return translated_text

def main():
    from_lang = input("Enter the source language code (e.g., 'en'): ")
    to_lang = input("Enter the target language code (e.g., 'es'): ")
    text_to_translate = input("Enter the text to translate: ")
    setup_translation(from_lang, to_lang)
    translated_text = translate_text(text_to_translate, from_lang, to_lang)
    print("Translated Text:", translated_text)

if __name__ == "__main__":
    main()
