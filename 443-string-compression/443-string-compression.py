class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        
        length, count, insert = 0, 1, 1
        for i in range(1, len(chars)):
            if chars[i] != chars[i - 1]:
                length += 1
                if count > 1:
                    cStr = str(count)
                    for num in cStr:
                        length += 1
                        chars[insert] = num
                        insert += 1
                chars[insert] = chars[i]
                insert += 1
                count = 0
            count += 1
            
        length += 1
        if count > 1:
            cStr = str(count)
            for num in cStr:
                length += 1
                chars[insert] = num
                insert += 1
        return length