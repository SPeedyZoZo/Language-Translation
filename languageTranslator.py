import argostranslate.package # Import the package module (used to install the translation package)
import argostranslate.translate # Import the translate module (used to translate text)

def setup_translation(from_code, to_code):
    # Update the package index (this is needed to get the latest list of available packages)
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package = next((pkg for pkg in available_packages if pkg.from_code == from_code and pkg.to_code == to_code), None)
    if not package:
        print(f"No package available for translating from {from_code} to {to_code}")
        return None
    print(f"Downloading and installing package for {from_code} to {to_code}...")
    package.install()

def translate_text(text, from_code, to_code):
    # Get installed languages (to check if the source and target languages are both installed)
    languages = argostranslate.translate.get_installed_languages()
    from_lang = next((lang for lang in languages if lang.code == from_code), None)
    if not from_lang:
        return "Source language not installed."
    to_lang = next((lang for lang in languages if lang.code == to_code), None)
    if not to_lang:
        return "Target language not installed."
    translation = from_lang.get_translation(to_lang)
    if not translation:
        return "Translation model for the target language not found."
    translated_text = translation.translate(text)
    return translated_text


def main():
    # Get both the source and target language codes and the text to translate
    from_lang = input("Enter the source language code (e.g., 'en'): ")
    to_lang = input("Enter the target language code (e.g., 'fr'): ")
    text_to_translate = input("Enter the text to translate: ")
    setup_translation(from_lang, to_lang)
    translated_text = translate_text(text_to_translate, from_lang, to_lang)
    print("Translated Text:", translated_text)

if __name__ == "__main__":
    main()

