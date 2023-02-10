import java.util.*;
import java.io.*;

public class Main {
	
	public static int cnt = 0;

	public static void bfs(ArrayList<Integer>[] graph, int start, boolean[] visited) {
		Queue<Integer> q = new LinkedList<>();
		q.offer(start);
		visited[start] = true;
		
		while(!q.isEmpty()) {
			int x = q.poll();
			
			for(int i=0; i<graph[x].size(); i++) {
				int y = graph[x].get(i);
				if (!visited[y]) {
					q.offer(y);
					visited[y] = true;
					cnt++;
				}
			}
		}
	}
	
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int n = Integer.parseInt(br.readLine().trim());
    	ArrayList<Integer>[] graph = new ArrayList[n+1]; 
    	for(int i=0; i<n+1; i++){
    	    graph[i] = new ArrayList<Integer>();
    	}
    	boolean[] visited = new boolean[n+1];
    	
    	int w = Integer.parseInt(br.readLine().trim());
    	for(int i=0; i<w; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine().trim());
    		int a = Integer.parseInt(st.nextToken());
    		int b = Integer.parseInt(st.nextToken());
    		
//    		System.out.println(a + " " + b);
    		
    		graph[a].add(b);
    		graph[b].add(a);
    	}
    	
    	bfs(graph, 1, visited);
    	
    	System.out.println(cnt);
    	
    	
    
    }
}