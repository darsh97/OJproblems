class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        List<Integer> lesser = new ArrayList<>();
        List<Integer> greater = new ArrayList<>();
        List<Integer> equal = new ArrayList<>();

        for (Integer e: nums){
            if (e < pivot) lesser.add(e);
            else if (e > pivot) greater.add(e);
            else equal.add(e);
        }

        lesser.addAll(equal);
        lesser.addAll(greater);

        return lesser.stream().mapToInt(Integer::intValue).toArray();
    }
}