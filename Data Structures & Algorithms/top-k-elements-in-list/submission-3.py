class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        return [number for number, count in Counter(nums).most_common(k)]