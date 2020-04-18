package problem5;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Random;

public class Interval {
    public int index;
    public int startTime;
    public int endTime;
    public int length;
    public boolean exluded = false;

    public Interval(int s, int l){
        this.startTime = s;
        this.length = l;
        this.endTime = s + l;
    }

    @Override
    public String toString(){
        return String.format("%d:%d-%d(%d)", index, startTime, endTime, length); 
    }
    
}

class IntervalSet{
    public int n;
    public Interval[] intervals;
    public IntervalSet(int n, int L, int r) {
        this.intervals = new Interval[n];
        this.n = n;
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            int s = rand.nextInt(L) + 1;
            int l = rand.nextInt(r) + 1;
            this.intervals[i] = new Interval(s, l);
        }    
        Arrays.sort(this.intervals, new startTimeComparator());    
        for (int i = 0; i < n; i++) {
            this.intervals[i].index = i;
        }    
    }

    public int nextCompatiInv(Interval inv){
        int i = Arrays.binarySearch(this.intervals, inv, 
        (Interval i1, Interval i2) -> i1.startTime - i2.endTime);
        
        if (i < 0) {
            return -i-1;
        }
        return i;
    }

    public int lastCompatInv(Interval inv){
        int i = Arrays.binarySearch(this.intervals, inv, 
        (Interval i1, Interval i2) -> i1.endTime - i2.startTime);

        if (i >= 0){
            return i;
        }
        // if no leftmost compatible interval found, return -1
        return Math.max(-i-2, -1);
    }

    public int StartTimeFirstSolution(){
        int maxLen = 0;
        for (int i = 0; i < this.n;){
            Interval curInv = this.intervals[i];
            maxLen += curInv.length;
            i = this.nextCompatiInv(curInv);
        }
        return maxLen;
    }

    public int LongestLengthFirstSolution(){
        int maxLen = 0;
        Interval[] intervalsByLen = this.intervals.clone();
        Arrays.sort(intervalsByLen, new lengthComparator());

        for (int i = 0; i < this.n; i++){
            Interval curInv = intervalsByLen[i];
            if (!curInv.exluded){
                maxLen += curInv.length;
                // ignore the overlap intervals
                for (int j = curInv.index; j < this.nextCompatiInv(curInv); j ++){
                    this.intervals[j].exluded = true;
                }
                for (int j = this.lastCompatInv(curInv) + 1; j < curInv.index; j ++){
                    this.intervals[j].exluded = true;
                }
            }
        }
        return maxLen;
    }

    
    public int DynamicProgrammingSolution(){
        Arrays.sort(this.intervals, new endTimeComparator());    
        int[] opts = new int[this.n + 1];
        for (int i = 1; i < this.n + 1; i++) {
            Interval curInv = this.intervals[i-1];        
            int p_cur = this.lastCompatInv(curInv);    
            if(p_cur != -1){
                opts[i] = Math.max(curInv.length + opts[p_cur+1] , opts[i-1]);
            }else{
                opts[i] = Math.max(curInv.length, opts[i-1]);
            }  
        }
        return opts[this.n];
    }


    public static void main(String[] args) {
        int n = 20;
        int sumSTF = 0;
        int sumLLF = 0;
        int sumDP = 0;
        
        for(int i = 0; i < n; i++){
            System.out.printf("case %d\n\n",i);
            IntervalSet set = new IntervalSet(10000, 1000000, 2000);
            int STF = set.StartTimeFirstSolution();
            int LLF = set.LongestLengthFirstSolution();
            int DP = set.DynamicProgrammingSolution();
            
            System.out.printf("Start Time First:     %d\n\n", STF);
            System.out.printf("Longest Length First: %d\n\n", LLF);
            System.out.printf("Dynamic Programming:  %d\n\n\n", DP);

            sumSTF += STF;
            sumLLF += LLF;
            sumDP += DP;
        }

        System.out.printf("Average Start Time First:     %.2f\n\n", 
                            sumSTF/20.0);
        System.out.printf("Average Longest Length First: %.2f\n\n", 
                            sumLLF/20.0);
        System.out.printf("Average Dynamic Programming:  %.2f\n\n\n", 
                            sumDP/20.0);
    }
}



    
class startTimeComparator implements Comparator<Interval> {
    @Override
    public int compare(Interval i1, Interval i2) {
        return i1.startTime - i2.startTime;
    }
}

class endTimeComparator implements Comparator<Interval> {
    @Override
    public int compare(Interval i1, Interval i2) {
        return i1.endTime - i2.endTime;
    }
}

class lengthComparator implements Comparator<Interval> {
    @Override
    public int compare(Interval i1, Interval i2) {
        return i2.length - i1.length;
    }
}