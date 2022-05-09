class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        # digit map for generator to take lists of values from
        digitMap = {'1': None, '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        generator = self._generator(digits, 0, digitMap)
        while True:
            try:
                result.append(next(generator))
            except:
                return result
        return result
        
    # TODO: change return value to list, since we are currently creating a new string for each permutation
    def _generator(self, digits, i, digitMap):
        dList = digitMap[digits[i]]
        if not dList:
            yield ''
        for letter in dList:
            if i == len(digits) - 1:
                yield letter
            else:
                for ltr in self._generator(digits, i + 1, digitMap):
                    yield letter + ltr
        