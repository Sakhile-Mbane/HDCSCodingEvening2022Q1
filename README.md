# HDCSCodingEvening2022Q1
HyperionDev Codenight

#STAGE1 - encrytion.

morse_map = {'A':'.-','B':'-...','C':'-.-.','D' : '-..', 'E':'.','F':'..-.','G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..','-..-.':'/'}
message = input('enter messageto encrypt in CAPITAL LETTERS: ')
def encrytion(message):
    ciphertext = ''
    for letter in message:
        if letter != ' ':
            ciphertext += morse_map[letter] + ' '
        else:
            ciphertext += ' '
    return ciphertext

encrytion(message)

def decryption(message):
    message += ' '
    deciphertext = ''
    ciphertext = ''
    
    for letter in message:
        
        if letter != ' ':
            temp = 0
            ciphertext +=letter
            if temp == 2:
                deciphertext += ' '
        else: 
            deciphertext += list(morse_map.keys())[list(morse_map.values()).index(ciphertext)]
            ciphertext = ''
                               
    return deciphertext
decryption('.... . .-.. .-.. --- / .-- --- .-. .-.. -..')
