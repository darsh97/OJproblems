class Solution {
    public int[] rearrangeArray(int[] nums) {
        ArrayList<Integer> positive = new ArrayList<>();
        ArrayList<Integer> negative = new ArrayList<>();
        
        ArrayList<Integer> result = new ArrayList<>();
        
        for (int e: nums){
            (e > 0? positive : negative).add(e);
        }
        
        for (int i = 0; i < positive.size(); i++){
            result.add(positive.get(i));
            result.add(negative.get(i));
        }
        
        return result.stream().mapToInt(e->e).toArray();
    }
}