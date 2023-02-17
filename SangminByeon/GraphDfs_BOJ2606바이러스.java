import java.util.*;
import java.io.*;

public class Main {
	
	public static int cnt = 0;
	public static void dfs(ArrayList<Integer>[] graph, int node, boolean[] visited) {
		if(!visited[node]) {
			cnt++;
			visited[node] = true;
			for(int i=0; i<graph[node].size(); i++) {
				dfs(graph, graph[node].get(i),visited);
			}
		}
	}
	
	
    public static void main(String[] args) throws NumberFormatException, IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int n = Integer.parseInt(br.readLine().trim());
    	ArrayList<Integer>[] network = new ArrayList[n+1];
    	for(int i=0; i<n+1; i++) {
    		network[i] = new ArrayList<Integer>();
    	}
    	boolean[] visited = new boolean[n+1];
    	
    	int numOfPairs = Integer.parseInt(br.readLine().trim());
    	
    	for(int i=0; i<numOfPairs; i++) {
    		StringTokenizer st = new StringTokenizer(br.readLine().trim());
    		int a = Integer.parseInt(st.nextToken());
    		int b = Integer.parseInt(st.nextToken());
    		
    		network[a].add(b);
    		network[b].add(a);
    	}
    	
    	dfs(network, 1, visited);
    	System.out.println(cnt-1);
    
    }
}