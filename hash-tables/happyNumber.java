public class happyNumber {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        boolean test = new Solution().isHappy(19);
        System.out.println(test);
        boolean test2 = new Solution().isHappy(4);
        System.out.println(test2);
    }
}
class Solution {
    public boolean isHappy(int n) {
        if(n == 1) { // base case  (if n is 1 then it is a happy number)
            return true;
        }  

        if(n==4) {
            return false;  // 4 is first number in cycle not happy number will always end in 4, 16, 37, 58, 89, 145, 42, 20, 4 
        }
        
        return isHappy(getNext(n)); 
    }


    private int getNext(int n) {
        if(n == 0) { // base case if n is 0 then return 0 
            return 0; 
        }
        int sum = 0;
        while(n > 0) { // while n is greater than 0 keep breaking it down into digits and squaring them 
            int digit = n % 10; // get last digit / break up into 10s so it can be squared 
            sum += digit * digit; 
            n/=10; 
        }
        return sum; 
    }
       
}