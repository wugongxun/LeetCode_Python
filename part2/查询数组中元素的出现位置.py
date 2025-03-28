from typing import List


def occurrencesOfElement(nums: List[int], queries: List[int], x: int) -> List[int]:
    ids = [i for i, num in enumerate(nums) if num == x]
    return [-1 if len(ids) < q else ids[q - 1] for q in queries]


print(occurrencesOfElement([1, 3, 1, 7], [1, 3, 2, 4], 1))
