from translate import Translator

original_file_path = "./translations/navy_ethos.txt"
translate_path = "./translations/converted.txt"

try:
    with open(original_file_path, mode='r') as file_object:
        current_file = file_object.read()
        translator = Translator(to_lang="fr")
        translation = translator.translate(current_file)
        with open(translate_path, mode='w') as file_object:
            file_object.write(translation)
except FileNotFoundError as err:
    print("The file for translation does not exist")
finally:
    print("Translation done!")
