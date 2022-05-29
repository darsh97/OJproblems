class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        cnt = Counter()
        mx = 0

        for m, s in zip(messages, senders):
            cnt[s] += len(m.split())
            mx = max(mx, cnt[s])

        return sorted(k for k, v in cnt.items() if v == mx)[-1]