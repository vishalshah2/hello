import pyperclip

message = 'This is my secret message.'
key = 13
mode = 'encrypt'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolindex = SYMBOLS.find(symbol)

    
        if mode == 'encrypt':
            translatedindex = symbolindex + key
        elif mode == 'decrypt':
            translatedindex = symbolindex - key
      
        if translatedindex >= len(SYMBOLS):
            translatedindex = translatedindex - len(SYMBOLS)
        elif translatedindex < 0:
            translatedindex = translatedindex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedindex]

    else:
        translated = teanslated + symbol

print(translated)
pyperclip.copy(translated)
