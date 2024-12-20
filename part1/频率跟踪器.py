from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq[self.cnt[number]] -= 1
        self.cnt[number] += 1
        self.freq[self.cnt[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.cnt[number]:
            self.freq[self.cnt[number]] -= 1
            self.cnt[number] -= 1
            self.freq[self.cnt[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


obj = FrequencyTracker()
obj.add(3)
obj.add(1)
obj.hasFrequency(1)
obj.add(3)
obj.hasFrequency(2)
obj.add(1)
obj.add(2)

obj.deleteOne(2)
print(obj.hasFrequency(2))
