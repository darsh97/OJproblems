class Solution {
    public List<Integer> maxScoreIndices(int[] nums) {
        final int n = nums.length;

        int zeroCount = 0, oneCount = Arrays.stream(nums).sum(), maxCount = oneCount;
        List<Integer> result = new ArrayList<>();

        result.add(oneCount);

        for (int num : nums) {
            zeroCount += num == 0 ? 1 : 0;
            oneCount += num == 1 ? -1 : 0;
            int total = oneCount + zeroCount;
            maxCount = Math.max(maxCount, total);
            result.add(total);
        }

        int finalMaxCount = maxCount;
        
        return IntStream.rangeClosed(0, n)
                .boxed()
                .filter(idx -> result.get(idx) == finalMaxCount)
                .collect(Collectors.toList());
    }
}