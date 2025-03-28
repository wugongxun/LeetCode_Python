from typing import List

amountArr = [20, 50, 100, 200, 500]

class ATM:

    reduce = List[int]

    def __init__(self):
        self.reduce = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, c in enumerate(banknotesCount):
            self.reduce[i] += c


    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for i in range(4, -1, -1):
            c = min(amount // amountArr[i], self.reduce[i])
            amount -= c * amountArr[i]
            res[i] = c
        if amount > 0:
            return [-1]
        for i, c in enumerate(res):
            self.reduce[i] -= c
        return res

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)