class Solution {
    public int halveArray(int[] nums) {
        PriorityQueue<Double> pq = new PriorityQueue<>(Collections.reverseOrder());
        double total = 0;
        int moves = 0;

        for (Integer e : nums) {
            total += e;
            pq.offer((double) e);
        }

        double half = 0;

        while (half < total / 2) {
            double mx = pq.poll();
            double hmx = mx / 2;
            half += hmx;
            pq.offer(hmx);
            moves++;

        }
        return moves;
    }
}
