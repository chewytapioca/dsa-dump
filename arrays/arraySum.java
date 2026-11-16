package arrays;

public class arraySum {
    public static void main(String[] args) {
        int[] nums = {1, 1, 1};
        int k = 2;
        System.out.println("Function outputs: " + subArraySum(nums, k)); // 2
    }

    public static int subArraySum(int[] nums, int k) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) { // go through actual array
            int sum = 0;
            for (int j = i; j < nums.length; j++) { // subarray, so starts at first index
                                                    // then lopp through each number

                sum += nums[j];

                if (sum == k) { 
                    count++; // count if equal k
                }
            }
        }
        return count;
    }
}