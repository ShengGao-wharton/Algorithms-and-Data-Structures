# You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:
#
# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
# Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i, j = 0, 0
        cs, ct = 0, 0
        s = [a for a in start if a != "_"]
        t = [a for a in target if a != "_"]
        if s != t:
            return False
        lastR = -1
        while i < n and j < n:
            while j < n and target[j] != "L":
                j += 1
            if j == n:
                break
            while i < n and start[i] != "L":
                i += 1
                if i < n and start[i] == "R":
                    lastR = i
            if j <= lastR or j > i:
                return False
            i += 1
            j += 1
        rs = start[::-1]
        rt = target[::-1]
        i, j = 0, 0
        lastL = -1
        while i < n and j < n:
            while j < n and rt[j] != "R":
                j += 1
            if j == n:
                break
            while i < n and rs[i] != "R":
                i += 1
                if i < n and rs[i] == "L":
                    lastL = i
            if j <= lastL or j > i:
                return False
            i += 1
            j += 1
        return True
