package arrays;

public class maxProfit {

    // Leetcode #121 stock prices

     public static void main(String[] args) {
        int[] prices = {7,1,5,3,6,4};
        System.out.println(calculateMaxProfit(prices));
    }



    public static int calculateMaxProfit(int[] prices) {
        // return max profit, buy one day then sell the next 
        // if cannot achieve any profit, return 0 
        int  minPrice = prices[0]; // find minimum price
        int maxProfit = 0;
        for(int i = 1; i < prices.length; i++) { // only need to iterate through the array once
           if(prices[i] < minPrice) {
                minPrice = prices[i];
           } else {
            maxProfit = prices[i] - minPrice;
           }
        
        }

        return maxProfit;
        
       // This is worst case O(n)
    }

   
}
