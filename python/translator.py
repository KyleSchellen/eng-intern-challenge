import sys

# English -> Braille (raised dots represented as O, unraised dots as .)
english_to_braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',  # Space
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    '.': '..OO.O', ',': '..O...', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '(': 'O.O..O', ')': '.O.OO.',
    '<': '.OO..O', '>': 'O..OO.'
}

# Add capitalization and number markers
capitalization_marker = '.....O'  # Prefix for capital letters
number_marker = '.O.OOO'          # Prefix for numbers

# TODO Automatically create the Braille to English map by reversing the above map.
braille_to_english_map = {v: k for k, v in english_to_braille_map.items()}

def braille_to_english(braille_text: str) -> str:
    """Convert Braille text to English."""
    return "English translation not yet implemented."

# TODO Converts English text to Braille.
def english_to_braille(text: str) -> str:
    """Convert English text to Braille."""
    return "Braille translation not yet implemented."


# TODO Detect whether the input is Braille or English.
def is_braille(input_string: str) -> bool:
    """Detect if the input string is Braille"""
    return False #stub

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py <text_or_braille_string>")
        return
    
    # Join all arguments (after script name) into a single string
    input_string = ' '.join(sys.argv[1:])
    
    # Decide whether the input is Braille or English
    if is_braille(input_string):
        # Convert Braille to English
        result = braille_to_english(input_string)
    else:
        # Convert English to Braille
        result = english_to_braille(input_string)
    
    # Output the result
    print(result)

if __name__ == "__main__":
    main()
