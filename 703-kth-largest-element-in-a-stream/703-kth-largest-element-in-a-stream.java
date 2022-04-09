
class KthLargest {

    int k;
    int[] nums;
    PriorityQueue<Integer> pq = new PriorityQueue<>();

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.nums = nums;

        for (Integer e : this.nums) {
            pq.offer(e);
        }

        while (pq.size() > k) {
            pq.poll();
        }
    }

    public int add(int val) {
        if (pq.size() < this.k){
            pq.offer(val);
            return pq.peek();
        }

        int top = pq.peek();
        
        if (val > top) {
            
            pq.poll();
            pq.offer(val);

        }
        return pq.peek();
    }
}
