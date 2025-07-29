class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        seen = {}
        result = 0
        MORSE_CODE = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }

        for word in words:
            alias = ""
            for ch in word:
                alias += MORSE_CODE[ch]
            if alias not in seen:
                seen[alias] = 1
                result += 1

        return result