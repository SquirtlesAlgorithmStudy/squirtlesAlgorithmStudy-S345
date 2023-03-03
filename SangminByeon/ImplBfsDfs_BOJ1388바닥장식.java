import java.util.*;
import java.io.*;

public class Main {
	
	public static boolean dfs_vertical(int py, int px) {
		if(py<0 | py>=n | px<0 | px>=m) {
			return false;
		}
		if(floor[py][px] == '|') {
			floor[py][px] = 'x';
			dfs_vertical(py-1,px);
			dfs_vertical(py+1,px);
			return true;
			
		}
		return false;
	}
	
	public static boolean dfs_horizon(int py, int px) {
		if(py<0 | py>=n | px<0 | px>=m) {
			return false;
		}
		if(floor[py][px] == '-') {
			floor[py][px] = 'x';
			dfs_horizon(py,px-1);
			dfs_horizon(py,px+1);
			return true;
			
		}
		return false;
	}
	
	static int n, m, cnt;
	static char[][] floor;
	
	public static void main(String[] args) throws Exception {
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken()); //세로,y
		m = Integer.parseInt(st.nextToken()); //가로,x arr[y][x]
		floor = new char[n][m];
		
		for(int i = 0; i<n; i++) {
			char[] temp = br.readLine().toCharArray();
			for(int j = 0; j<m; j++) {
				floor[i][j] = temp[j];
			}
		}
		
//		System.out.println(Arrays.deepToString(floor));
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				
				if(dfs_vertical(i,j)) 
					cnt++;
				if(dfs_horizon(i,j)) 
					cnt++;

			}
		}
	
		System.out.println(cnt);
	
	}
	
	
}