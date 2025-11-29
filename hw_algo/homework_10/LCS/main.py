from functools import lru_cache

def lcs(s1, s2):

    @lru_cache(maxsize=None)
    def solve(i, j):
        if i == len(s1) or j == len(s2):
            return ""

        if s1[i] == s2[j]:
            return s1[i] + solve(i + 1, j + 1)

        else:
            option1 = solve(i + 1, j)
            option2 = solve(i, j + 1)

            if len(option1) > len(option2):
                return option1
            else:
                return option2

    return solve(0, 0)
