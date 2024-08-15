class Solution {
    public int hammingWeight(int n) {
        int answer = 0;
        answer = hammingWeightRec(answer, n);
        return answer;
    }

    public int hammingWeightRec(int answer, int n) {
        if (n == 0) {
            return answer;
        }
        if (n % 2 == 1) {
            answer += 1;
        }
        return hammingWeightRec(answer, n / 2);
    }
}