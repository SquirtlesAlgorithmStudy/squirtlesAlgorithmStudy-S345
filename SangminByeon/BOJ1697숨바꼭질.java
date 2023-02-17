import java.util.*;
import java.io.*;

public class Main {
	
	public static int bfs(int start, int end, int cnt) {
		
		int now = start;
		boolean[] visited = new boolean[Math.max(start, end)*2];
		
		Queue<Integer> que = new LinkedList<>();
		que.offer(now);
		
		while(!que.isEmpty()) {
			now = que.poll();
			int[] nexts = {now+1, now-1, now*2};
			if (now == end) return cnt;
			if (!visited[now]) {
				visited[now] = true;
				cnt++;
				for (int next : nexts) {
					if (!visited[next]) {
						que.offer(next);
					}
				}
			}
		}
		
		return cnt;
	}

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		System.out.println(bfs(n,k,0));
	
	}
}
