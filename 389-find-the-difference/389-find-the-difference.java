class Solution {

    private static Map<Character, Integer> Counter(String s){
        Map<Character, Integer> cnt = new HashMap<>();
        for (char c: s.toCharArray()){
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
        }

        return cnt;

    }

    public char findTheDifference(String s, String t) {
        Map<Character, Integer> cntS = Solution.Counter(s);
        Map<Character, Integer> cntT = Solution.Counter(t);

        for (char key: cntT.keySet()){
            if (!cntS.containsKey(key) || !Objects.equals(cntT.get(key), cntS.get(key))){
                return key;
            }
        }

        return 'a';
    }
}