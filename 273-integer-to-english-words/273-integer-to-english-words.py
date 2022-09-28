class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        numToStr = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        magnitude = {2: "Hundred", 3: "Thousand", 6: "Million", 9: "Billion"}
        rev = set(["Thousand", "Million", "Billion"])
        teens = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        tys = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
        words = []
        numCount = 0
        while num:
            if numCount in magnitude:
                if words and words[-1] in rev:
                    words.pop()
                words.append(magnitude[numCount])
            if num % 100 in teens:
                words.append(teens[num % 100])
                num = num // 100
                numCount += 2
            else:
                if num % 10:
                    words.append(numToStr[num % 10])
                num = num // 10
                numCount += 1
                if num % 10:
                    words.append(tys[num % 10])
                num = num // 10
                numCount += 1
            if num % 10 > 0:
                words.append('Hundred')
                words.append(numToStr[num % 10])
            num = num // 10
            numCount += 1
        words.reverse()
        return " ".join(words)