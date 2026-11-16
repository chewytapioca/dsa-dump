import java.util.*;
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
        if(n == 1) {
            return true;
        }  

        if(n==4) {
            return false; 
        }
        
        return isHappy(getNext(n)); 
    }


    private int getNext(int n) {
        if(n == 0) {
            return 0; 
        }
        int sum = 0;
        while(n > 0) {
            int digit = n % 10; 
            sum += digit * digit; 
            n/=10; 
        }
        return sum; 
    }
       
}