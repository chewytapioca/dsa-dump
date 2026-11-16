package heaps;
import java.util.*;

public class heap {

}

class Solution {
    public static long minTotalTime(int[] belt, int[] storage) {
        PriorityQueue<Long> heap = new PriorityQueue<>();
        for (int p : belt) {
            heap.offer(Math.abs((long) p));   // only distance from 0 matters
        }

        long total = 0;
        for (int s : storage) {
            long d = Math.abs((long) s);
            long closest = heap.poll();       // belt nearest to 0
            total += closest + d;             // pickup leg + delivery leg
            heap.offer(d);                    // belt now sits at storage[i]
        }
        return total;
    }

    public static void main(String[] args) {
        int[] belt = {-3, 5};
        int[] storage = {2, -4, 1};
        System.out.println(minTotalTime(belt, storage)); // 16
    }
}