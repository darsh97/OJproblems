class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_cnt, loss_cnt = Counter(), Counter()

        for w, l in matches:
            win_cnt[w] += 1
            loss_cnt[l] += 1

        win_set, loss_set = set(win_cnt), set(loss_cnt)
        return [sorted((win_set ^ loss_set) - loss_set),
                sorted(t for t, v in loss_cnt.items() if v == 1)]
