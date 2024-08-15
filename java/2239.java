class Solution {
    public int findClosestNumber(int[] nums) {
        IntStream.of(nums).map(Math::abs).min().ifPresent(n -> nums.);
        int a = nums[0];
        for(int i = 1; i < nums.length ; i++) {
            int t = Math.abs(a);
            int n = nums[i];
            if (Math.abs(n) < t) {
                a = n;
                continue;
            }
            if (Math.abs(n) == t) {
                a = a > n ? a : n;
            }
        }
        return a;
    }
}