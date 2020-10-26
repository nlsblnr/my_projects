from translate import Translator
translator = Translator(to_lang='de', from_lang='it')

file_object  = open('wordlist.txt', 'r')

l = file_object.readlines()

for x in l:
    translation = translator.translate(x)
    print(x, '=', translation)
