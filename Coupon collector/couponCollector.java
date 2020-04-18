import java.util.Arrays;

class couponCollector2{
    public static void main(String[] args){
        for(int i = 500; i <= 5000; i += 500){
            float localSum = 0;
            for(int j = 0; j < 50; j ++)
                localSum += sim(i);
            System.out.printf(
                            "n:%d, "+ 
                            "avgV:%.2f, "+ 
                            "V/n:%.2f\n", 
                               i, 
                               localSum/50, 
                               (localSum/50)/i);
        }
    }

    public static float sim(int n) {
        int[] owned = new int[n];
        int[] minVal = new int[n];
        while (Arrays.stream(owned).sum() != n){
            int idx = (int)(Math.random() * n);
            int val = (int)(Math.random() * n);
            if (owned[idx] == 0) {
                owned[idx] ++;
                minVal[idx] = val;
            }
            else{
                if (minVal[idx] > val) minVal[idx] = val;
            }
        }
        return Arrays.stream(minVal).sum();
    }

}