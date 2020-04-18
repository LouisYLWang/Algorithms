import java.util.ArrayList;
import java.util.Arrays;


public class electoralCollege  {
    static String[] states = {"Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida",
    "Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts",
    "Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico",
    "New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina",
    "South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"};
    static long[] electoralVotes = { 9, 3, 11, 6, 55, 9, 7, 3, 3, 29, 16, 4, 4, 20, 11, 6, 6, 8, 8, 4, 10, 11, 16, 10,
            6, 10, 3, 5, 6, 4, 14, 5, 29, 15, 3, 18, 7, 7, 20, 4, 9, 3, 11, 38, 6, 3, 13, 12, 5, 10, 3 };
    static long solutionCount(long[] electoralVotes){
        int K = 269;
        long[] Opt = new long[K + 1];
        Opt[0] = 1;
        for(long num : electoralVotes){
            for(int k = K; k >= 0; k--){
                if(k >= num){
                    Opt[k] += Opt[(int) (k - num)];
                }
            }
        }
        return Opt[K]/2;
    }
    
    
    static ArrayList<String> getASolution(long[] electoralVotes){
        int K = 269;
        int n = electoralVotes.length;
        Boolean[][] Opt = new Boolean[n + 1][K + 1];
        for (int i = 0; i <= n; i++)  
        {  
            Arrays.fill(Opt[i], false);
        }  

        Opt[0][0] = true;

        for (int j = 1; j <= n; j++){
            for (int k = 0; k <= K; k ++){
                Opt[j][k] = Opt[j-1][k];
                if (k - electoralVotes[j-1] >= 0){
                    int residue = (int) (k - electoralVotes[j-1]);
                    Opt[j][k] = (Opt[j-1][k] || Opt[j-1][residue]);
                }
            }
        }

        ArrayList<String> subSet = new ArrayList<String>();
        int verifySum = 0;
        int k = K;
        for (int j = n; j >= 1; j--){
            if(!Opt[j-1][k]){
                subSet.add(states[j-1]);
                verifySum += electoralVotes[j-1];
                System.out.printf("%s:%d\n", states[j-1], electoralVotes[j-1]);
                k -= electoralVotes[j-1];
            }
        }
        assert verifySum == 269;
        return subSet;
    }
    public static void main(String[] args) {
        System.out.println(solutionCount(electoralVotes));
        System.out.println(getASolution(electoralVotes));
        }
    }
            




