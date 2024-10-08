class Solution {
    public int romanToInt(String s) {
        int res = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int t = cast(s.charAt(i));
            res += (i + 1 < s.length() && t < cast(s.charAt(i+1))) ? -t : t;
        }
        return res;
    }

    private int cast(char c) {
        switch (c) {
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
            default:
                return 0;
        }
    }
}