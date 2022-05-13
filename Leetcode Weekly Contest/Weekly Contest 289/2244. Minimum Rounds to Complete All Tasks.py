# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task.
# In each round, you can complete either 2 or 3 tasks of the same difficulty level.
#
# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        res = 0
        for a, b in c.items():
            if b == 1:
                return -1
            else:
                if b % 3 == 0:
                    res += b // 3
                elif b % 3 == 2:
                    res += b // 3 + 1
                elif b % 3 == 1:
                    res += (b-4)//3 + 2
        return res