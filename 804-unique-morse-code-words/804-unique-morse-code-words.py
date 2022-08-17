class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformations = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            curWord = []
            for c in word:
                curWord.append(morse[ord(c) - 97])
            transformations.add("".join(curWord))
        return len(transformations)