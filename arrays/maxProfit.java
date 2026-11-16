package arrays;

public class maxProfit {

    // Leetcode #121 stock prices

     public static void main(String[] args) {
        int[] prices = {7,1,5,3,6,4};
        System.out.println("Function outputs:");
        System.out.println(calculateMaxProfit(prices));
    }



    public static int calculateMaxProfit(int[] prices) {
        // return max profit, buy one day then sell the next 
        // if cannot achieve any profit, return 0 
        int  minPrice = prices[0]; // find minimum price
        int maxPrice = prices[0];
        int maxProfit = 0;
        for(int i = 1; i < prices.length; i++) { 
            if(prices[i] > maxPrice) {
                maxPrice = prices[i];
                // System.out.println("Max price:" + maxPrice); 

            }
           if(prices[i] < minPrice) {
                minPrice = prices[i];
                // System.out.println("Min Price:" + minPrice);
            
           } else if(prices[i] - minPrice > maxProfit) {
                // System.out.println("Calculation " + prices[i] + " - " + minPrice);
                maxProfit = prices[i] - minPrice;

           }
        
        }

       return maxProfit;
        
       // This is worst case O(n)
    }

   
}
