import java.util.HashMap;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Graph{
    public int n;
    public int m;
    public double p;
    public HashMap<Integer, ArrayList<Integer>> vertexMap = new HashMap<>();
    public ArrayList<int[]> edgeList = new ArrayList<>();
    public int[] degrees;
    
    public Graph(int n, double p) {
        this.n = n;
        this.p = p;
        m = (int) (n * (n - 1) * p / 2.0);
        degrees = new int[this.n];
        getRandomGraph();
	}

	void getRandomGraph(){
        Random rand = new Random();
        for (int i = 0; i < n - 1; i++)
            for (int j = i + 1; j < n; j++)
                if (rand.nextDouble() < p){
                    AddEdge(i, j);
                }
        }                       

    void AddEdge(int i, int j) {
        if(!vertexMap.containsKey(i)){
            vertexMap.put(i, new ArrayList<>());
        }
        vertexMap.get(i).add(j);
        degrees[i]++;

        if(!vertexMap.containsKey(j)){
            vertexMap.put(j, new ArrayList<>());
        }      
        vertexMap.get(j).add(i);
        degrees[j]++;
    }

    Integer greedyColoring(){
        int[] color = new int[n];
        int maxColor = 1;
        Arrays.fill(color, -1);
        for (int i = 0; i < n; i++){
            if (color[i] == -1){
                int[] colorToChoose = new int[maxColor];
                if(vertexMap.containsKey(i)){
                    for (int j:vertexMap.get(i)){
                        if(color[j]!= -1){
                            colorToChoose[color[j]] = 1;
                        }
                    }
                }
                int k = 0;
                while(k < maxColor){
                    if(colorToChoose[k] == 0){
                        color[i] = k;
                        break;
                    }
                    k++;
                }
                if(k == maxColor){
                    maxColor ++;
                    color[i] = maxColor-1;
                }
            }
        }
        return maxColor;
    }

    public Integer WelshPowellColoring() {
    
        //sort the vertices in order of descending degrees
        Pair[] indices = new Pair[n];
        for (int i = 0; i < n; i++) {
            indices[i] = new Pair(i, degrees[i]);
        }
        Arrays.sort(indices);
        ArrayList<?> sortedVertex[]= new ArrayList[n];
        // color the noncolored vertices based on the degree order 
        // color all the vertices that are not connected to the 
        // coloured vertex with the same color.
        for(int i = 0; i<n; i++){
            if (indices[i].value != 0){
                sortedVertex[i] = vertexMap.get(indices[i].index);
            }
            else{
                sortedVertex[i] = new ArrayList<Integer>();
            }
        }

        int[] colors = new int[n];
        Arrays.fill(colors, -1);
        int maxColor = 0;
        for (int i = 0; i < n; i++){
            if (colors[i] != -1){	
                continue;
            }
            else{
                maxColor ++;
                colors[i] = maxColor;
                for (int j = i+1; j < n; j++){
                    if (!(sortedVertex[i].contains(j)) && (colors[j] == -1)){
                        // make sure j's neighbor are not colored this color
                        boolean flag = true;
                        for(int k = 0; k < sortedVertex[j].size(); k++) {
                            flag &= 
                            (colors[(int) sortedVertex[j].get(k)] 
                            != maxColor);
                        }
                        if(flag)
                            colors[j] = maxColor;
                    }
                    else{
                        continue;
                    }
                }
            }	
        }
        System.out.println(Arrays.toString(colors));
        return maxColor;
    }


    public int WelshPowellColoring1() {

        //sort the vertices in order of descending degrees
        Pair[] indices = new Pair[n];
        for (int i = 0; i < n; i++) {
            indices[i] = new Pair(i, degrees[i]);
        }
        Arrays.sort(indices);
        ArrayList<?> sortedVertex[]= new ArrayList[n];

        // color the noncolored vertices based on the degree order 
        // color all the vertices that are not connected to the coloured vertex with the same color.
        for(int i = 0; i<n; i++){
            if (indices[i].value != 0){
                sortedVertex[i] = vertexMap.get(indices[i].index);
            }
            else{
                sortedVertex[i] = new ArrayList<Integer>();
            }
        }

        int[] color = new int[n];
        int maxColor = 0;
        Arrays.fill(color, -1);
        for (int i = 0; i < n; i++){
            if (color[i] == -1){
                int[] colorToChoose = new int[maxColor];
                for (Object j : sortedVertex[i]) {
                    if(color[(int)j]!= -1){
                        colorToChoose[color[(int)j]] = 1;
                    }
                }
                int k = 0;
                while(k < maxColor){
                    if(colorToChoose[k] == 0){
                        color[i] = k;
                        break;
                    }
                    k++;
                }
                if(k == maxColor){
                    maxColor ++;
                    color[i] = maxColor-1;
                }
            }
        }
        System.out.println(Arrays.toString(color));
		return maxColor;
	}



    public static void main(String[] args){
        Graph gp = new Graph(10, 0.2);
        System.out.println(gp.vertexMap);
        System.out.println("greedyColoring " + gp.greedyColoring() + '\n');
        System.out.println("WelshPowellColoring " + gp.WelshPowellColoring() + '\n');
        System.out.println("WelshPowellColoringPlus " + gp.WelshPowellColoring1() + '\n');

        
        /*
        for(double i = 0.002; i <= 0.021; i += 0.001){
            int wpcolor = 0;
            int gdcolor = 0;
            for(int j = 0; j <= 101; j++){
                Graph g = new Graph(1000, i);
                wpcolor += g.WelshPowellColoring(); 
                gdcolor += g.greedyColoring();
            }
                System.out.printf(" n:%d, p:%.3f\n" + 
                                 "avgWelshPowellColorNumber:%.2f " +
                                 "avgGreedyColorNumber%.2f\n", 
                                 1000, i, wpcolor/100.0, gdcolor/100.0);
        } 
        */
        
        
    }  
}

class Pair implements Comparable<Pair> {
    public final int index;
    public final int value;

    public Pair(int index, int value) {
        this.index = index;
        this.value = value;
    }

    @Override
    public int compareTo(Pair other) {
        return other.value - this.value;
    }
}