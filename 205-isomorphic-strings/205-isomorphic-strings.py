class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}
        for s_char, t_char in zip(s, t):
            if s_char not in s_map:
                s_map[s_char] = t_char
            if t_char not in t_map:
                t_map[t_char] = s_char
            if s_map.get(s_char, 0) != t_char or t_map.get(t_char, 0) != s_char:
                return False
        return True