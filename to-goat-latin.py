'''You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
Return the final sentence representing the conversion from sentence to Goat Latin.

'''
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        formatted_words_list = []
        i = 1
        vowels = ('a','e','i','o','u')
        sentence_list = sentence.split(' ')
        for word in sentence_list:
            if word.lower().startswith(vowels):
                formatted_words_list.append(word+'ma'+'a'*i)
            else:
                formatted_word = word[1:]+word[0]+'ma'+'a'*i
                formatted_words_list.append(formatted_word)
            i += 1

        final_str = ' '.join(formatted_words_list)
        return final_str

sentence = "I speak Goat Latin"
soln = Solution().toGoatLatin(sentence)
print(soln)