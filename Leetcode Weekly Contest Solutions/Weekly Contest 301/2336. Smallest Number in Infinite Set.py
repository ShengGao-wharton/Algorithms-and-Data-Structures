class SmallestInfiniteSet:

    def __init__(self):
        self.pop = set()

    def popSmallest(self) -> int:
        for i in range(1, 2000):
            if i not in self.pop:
                break
        self.pop.add(i)
        return i

    def addBack(self, num: int) -> None:
        if num in self.pop:
            self.pop.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)