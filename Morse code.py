#STAGE1 - encrytion.

morse_map = {'A':'.-','B':'-...','C':'-.-.','D' : '-..', 'E':'.','F':'..-.','G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}
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