package arrays;
import java.util.*;
public class intersection {
    
}

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        // return hashset prob 
        Set<Integer> seen = new HashSet<>(); 
        for (int i : nums1) {
            seen.add(i); // set: 1,2,2,1
        }

        //compare 

        Set<Integer> newSet = new HashSet<>(); 
        for(int i : nums2) {
            if(seen.contains(i)) {
                newSet.add(i); 
            }
        }   
        

        // return an array 

        int[] result = new int[newSet.size()]; 
        int index = 0;
        for(int num : newSet) {
            result[index++] = num;
        }

        return result; 
        }
}