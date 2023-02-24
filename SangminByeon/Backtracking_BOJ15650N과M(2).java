import java.util.*;
import java.io.*;

public class Main {
	
	static int n,m;
	static int[] sequence;
	static boolean[] isUsed;
	static StringBuilder sb = new StringBuilder();
	
	static void bt(int depth, int k) {
		if(depth == m) {
			for (int val : sequence) {
				sb.append(val).append(' ');
			}
			sb.append('\n');
			
			return;
		}
		
		for(int i=k; i<n; i++) {
			if(!isUsed[i]) {
				isUsed[i] = true;
				sequence[depth] = i + 1;
				bt(depth+1, sequence[depth]);
				isUsed[i] = false;
			}
		}
	}
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		sequence = new int[m];
		isUsed = new boolean[n];
		
		bt(0,0);
		System.out.println(sb);
		
		
		
	}
	
	
}