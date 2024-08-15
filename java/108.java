import java.util.Arrays;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution108 {

    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 1) {
            return new TreeNode(nums[0]);
        }
        if (nums.length == 0) {
            return null;
        }
        int midle = nums.length / 2;
        return new TreeNode(nums[midle], 
            sortedArrayToBST(Arrays.stream(nums, 0, midle).toArray()),
            sortedArrayToBST(Arrays.stream(nums, midle+1, nums.length).toArray()));
    }

    public TreeNode sortedArrayToBST2(int[] nums) {
        return sortedArrayToBSTRecursive(nums, 0, nums.length);
    }

    public TreeNode sortedArrayToBSTRecursive(int[] nums, int l, int r) {
        if (nums.length == 1) {
            return new TreeNode(nums[0]);
        }
        if (nums.length == 0) {
            return null;
        }

        int midle = l+(r-l) / 2;

        TreeNode node = new TreeNode(midle);
        node.left = sortedArrayToBSTRecursive(nums, l, midle-1);
        node.right = sortedArrayToBSTRecursive(nums, midle+1, r);
        return node;
    }
}