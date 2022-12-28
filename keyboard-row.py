'''Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
'''

class Solution:
    def findWords(self, words: list) -> list:
        result = []
        self.american_keyboard = {
            'qwertyuiop':0,
            'asdfghjkl':1,
            'zxcvbnm':2
        }

        for word in words:
            keyboard_line = self.getKeyboardLine(word[0])
            current_line = 0
            for char in word:
                current_line = self.getKeyboardLine(char)
                if current_line != keyboard_line:
                    break
            if current_line == keyboard_line:
                result.append(word)
        
        return result

    
    def getKeyboardLine(self, char):
        for k,v in self.american_keyboard.items():
            if char.casefold() not in k:
                continue
            return v



input = ["Hello","Alaska","Dad","Peace"]
Solution().findWords(input)