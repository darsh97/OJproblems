class Solution {
    public int findComplement(int num) {
        long bit = 1;
        while (bit <= num) {
            num ^= bit;
            bit <<= 1;
        }
        return num;
    }
}
