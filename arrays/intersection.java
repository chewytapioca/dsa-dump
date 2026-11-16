package arrays;
import java.util.*;

// Leetcode Problem #349 
public class intersection {
//output an array that has intersecting values from the two given arrays
}

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        // need hashset to store first array w/o duplicates 
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
        

        // return an array so we convert it to an array 

        int[] result = new int[newSet.size()]; 
        int index = 0;
        for(int num : newSet) {
            result[index++] = num;
        }

        return result; 
    }
}