class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        int m = nums1.length, n = nums2.length;
        List<List<Integer>> res = new ArrayList<>();

        PriorityQueue<List<Integer>> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.get(0)));

        for (int j = 0; j < Math.min(n, k); j++) {
            pq.offer(List.of(nums1[0] + nums2[j], 0, j));
        }
        
        while (  pq.size() > 0 && k > 0) {
            List<Integer> top = pq.poll();
            assert top != null;

            int i = top.get(1), j = top.get(2);

            res.add(List.of(nums1[i], nums2[j]));

            if (i + 1 < m) {
                pq.offer(List.of(nums1[i + 1] + nums2[j], i + 1, j ));
            }
            
            k--;

        }

        return res;
    }
}
