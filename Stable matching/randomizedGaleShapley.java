import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import java.util.stream.IntStream;

class GaleShapley2 {
    public static void main(String[] args){

        Random rnd = new Random();
        rnd.setSeed(23);

        // – Preference lists for m1, m2, …, mn
        int[][] M = {
        {2, 1, 3, 0},
        {0, 1, 3, 2},
        {0, 1, 2, 3},
        {0, 1, 2, 3},
        };

        //– Preference lists for w1, w2, …, wn
        int[][] W = {
        {0, 2, 1, 3},
        {2, 0, 3, 1},
        {3, 2, 1, 0},
        {2, 3, 1, 0},
        };
        
        test();
        System.out.println(Arrays.toString(galeShapley(M,W)));

        
    }    

    public static int[] galeShapley(int[][] M, int[][] W){
        int[] pairM = new int [M.length];
        int[] pairW = new int [W.length];

        // memorize w's index in m's preference list to avoid revisited same w 
        int[] rankM = new int [M.length];
        
        Arrays.fill(pairM, -1);
        Arrays.fill(pairW, -1);
        Arrays.fill(rankM, -1);

        // using Queue to track free m
        Queue<Integer>freeM = new LinkedList<Integer>();
        for (int i = 0; i <  W.length; i++){
            freeM.offer(i); 
        }
        
        while (!freeM.isEmpty()){
            int m = freeM.poll();
            // start searching qualified w from last unmatch w index + 1
            for(int i = rankM[m] + 1; i < W.length; i++){
                int w = M[m][i];
                if (pairW[w] == -1){
                    // if w is free, match (m, w)
                    System.out.printf("%d proposes to %d [%d, %d]  Accepted\n", m , w, w, pairW[w] );
                    pairM[m] = w;
                    pairW[w] = m;
                    
                    // note down starting point for next iteration
                    rankM[m] = i;
                    break;
                    
                }else{
                    for(int j = 0; j < W.length; j++){
                        if (W[w][j] == m){
                            // unmatch w with pairW[w]
                            freeM.offer(pairW[w]);
                        
                            // match w with m
                            System.out.printf("%d proposes to %d [%d, %d]"+  
                                              "  Accepted\n", m , w, w, pairW[w] );
                            pairM[m] = w;
                            pairW[w] = m;
                            
                            // note down starting point for next iteration
                            rankM[m] = findIndex(M[m], w);
                            i = W.length;
                            break;
                        }
                        if (W[w][j]  == pairW[w]){
                            System.out.printf("%d proposes to %d [%d, %d]  Rejected\n", m , w, w, pairW[w] );
                            break;
                        }
                    }
                }
            }
        }
        return pairM;
    } 

    
    public static int[] permutation(int n, Random rand) {
        int[] arr = IntStream.range(0, n).toArray();
        for (int i = 0; i < n; i++) {
            int j = rand.nextInt(i + 1);
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        return arr;
        }

    
    public static int[][] generatePef(int n, Random rand){
        int[][] pef = new int[n][];
        for(int i = 0; i < n; i++){
            int[] cur = permutation(n, rand);
            pef[i] = cur;
        }
        return pef;
    }

    public static int findIndex(int[] arr, int t) {
        if (arr == null) return -1;
        int len = arr.length;
        int i = 0;
        while (i < len) {
            if (arr[i] == t){
                return i;
            }
            else{
                i++;
            } 
        }
        return -1;
    }

    public static void test(){
        // case 0
        int[][] M0 = {
        {2, 0, 1},
        {2, 0, 1},
        {2, 1, 0}
        };
        
        int[][] W0 = {
        {2, 0, 1},
        {0, 2, 1},
        {2, 0, 1}
        };

        int[] ans0 ={
            0,1,2
        };
 
            
        // case 1
        int[][] M1 = {
        {3, 1, 0, 2}, 
        {3, 0, 1, 2}, 
        {3, 1, 2, 0},
        {0, 3, 2, 1}
        };

        int[][] W1 = {
        {3, 0, 2, 1},
        {3, 1, 2, 0},
        {0, 1, 3, 2},
        {3, 0, 2, 1},
        };
    
        int[] ans1 = {
            3, 1, 2, 0
        };

        // case 2
        int[][] M2 = {
        {1, 3, 0, 2},
        {3, 0, 2, 1},
        {2, 3, 1, 0},
        {2, 0, 3, 1}
        };

        int[][] W2 = {
        {1, 2, 0, 3},
        {0, 3, 2, 1},
        {1, 2, 3, 0},
        {0, 1, 2, 3}
        };

        int[] ans2 = {
            1, 3, 2, 0
        };

         // case 3
        int[][] M3 = {
        {4, 2, 0, 1, 3},
        {0, 1, 4, 2, 3},
        {4, 0, 1, 3, 2},
        {1, 4, 3, 0, 2},
        {0, 1, 3, 4, 2}
        };

        int[][] W3 = {
        {2, 3, 4, 0, 1},
        {2, 4, 0, 3, 1},
        {1, 4, 2, 3, 0},
        {3, 0, 1, 4, 2},
        {0, 3, 1, 2, 4}
        };

        int[] ans3 = {
            4, 2, 0, 3, 1
        };

        int[][][] M_all = {M0, M1, M2, M3};
        int[][][] W_all = {W0, W1, W2, W3};
        int[][] ans = {ans0, ans1, ans2, ans3};
        
        for(int i = 0; i < M_all.length; i++){
            int[][] curM = M_all[i];
            int[][] curN = W_all[i];
            try{
                if(Arrays.equals(galeShapley(curM, curN),(ans[i]))){
                    System.out.println(String.format("Case pass %d/4", i+1));
                }
            }   
            catch(Exception e){
                System.out.println(e);
            };
        }
    }
}   





 