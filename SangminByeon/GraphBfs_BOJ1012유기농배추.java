import java.util.*;
import java.io.*;

public class Main {
	public static int t, m, n, k, x, y, cnt; //가로:m,x  세로: n,y
	public static int[][] field;
	public static int[] dx = {0,0,1,-1};
	public static int[] dy = {1,-1,0,0};
	
	public static int bfs(int x, int y) {
		Queue<int[]> q = new LinkedList<>();
//		int[] temp = {x,y};
//		q.offer(temp);
		q.offer(new int[] {x,y});
		field[y][x] = 2; // 방문 체크
		
		while(!q.isEmpty()) {
//			temp = q.poll();
//			x = temp[0];
//			y = temp[1];
			x = q.peek()[0];
			y = q.peek()[1];
			q.poll();
			for (int i=0; i<4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx>=0 && nx<m && ny>=0 && ny<n && field[ny][nx] == 1) {
//					temp[0] = nx;
//					temp[1] = ny;
					q.offer(new int[] {nx,ny});
					field[ny][nx] = 2; // 방문 체크

				}
			}
		}
		return 1;
	}
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine().trim());
		
		while(t-->0) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			m = Integer.parseInt(st.nextToken());
			n = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			
			field = new int[n][m];
			cnt = 0;
			
			while(k-->0) {
				st = new StringTokenizer(br.readLine().trim());
				x = Integer.parseInt(st.nextToken());
				y = Integer.parseInt(st.nextToken());
				
				field[y][x] = 1;
			}
			// 입력받기 끝.
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<m ; j++) {
					if(field[i][j] == 1)
						cnt += bfs(j,i);
				}
			}
			
			System.out.println(cnt);
		}
    	
    }
    	
}