caesarized_letters = {"a":"g", "b":"h", "c":"i" ,"d":"j" ,"e":"k", "f":"m", "g":"n", "h":"o" ,"i":"p" ,"j":"q", "k":"r", "m":"s" ,"n":"t", "o":"u", "p":"v", "q":"w", "r":"x", "s":"y", "t":"z", "u":"a", "v":"b", "w":"c", "x":"d", "y":"e", "z":"f"}
uncaesarized_letters = {
    caesar_letter: letter
    for letter, caesar_letter in caesarized_letters.items()
}

def caesarize_letter(letter):
    return caesarized_letters.get(letter, letter)

def uncaesarize_letter(letter):
    return uncaesarized_letters.get(letter, letter)

def caesarize(text):
    return ''.join([caesarize_letter(letter) for letter in text])

def uncaesarize(text):
    return ''.join([uncaesarize_letter(letter) for letter in text])
