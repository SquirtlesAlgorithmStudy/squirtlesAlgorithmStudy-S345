import java.util.*;
import java.io.*;

public class Main {
	public static int n,m;
	public static int[][] field;
	public static int[] dx = {0,0,1,-1};
	public static int[] dy = {1,-1,0,0};
	
	public static boolean dfs(int x, int y) {
		if(x<0||x>=m||y<0||y>=n) {
			return false;
		}
		if(field[y][x]==1) {
			field[y][x]=0; //방문처리 
			for(int i=0; i<4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				dfs(nx,ny);
			}
			return true;
		}
		else return false;
	}
	
	
	
    public static void main(String[] args) throws Exception {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int t = Integer.parseInt(br.readLine().trim());
    	
    	while(t-->0) {
	    	
	    	StringTokenizer st1 = new StringTokenizer(br.readLine().trim());
	    	m = Integer.parseInt(st1.nextToken()); //가로 m, x
	    	n = Integer.parseInt(st1.nextToken()); //세로 n, y
	    	field = new int[n][m];
	    	
	    	int number = Integer.parseInt(st1.nextToken());
	    	for(int i=0; i<number; i++) {
	    		StringTokenizer st2 = new StringTokenizer(br.readLine().trim());
	    		int x = Integer.parseInt(st2.nextToken());
	    		int y = Integer.parseInt(st2.nextToken());
	    		field[y][x] = 1;
	    	}
	    	
	    	int count =0;
	    	for(int i=0; i<n; i++) {
	    		for(int j=0; j<m; j++) {
	    			if(dfs(j,i)==true) count++;
	    		}
	    	}
	    	
	    	System.out.println(count);
	    	
	    	
    	}
    	
    	
    }
    	
}