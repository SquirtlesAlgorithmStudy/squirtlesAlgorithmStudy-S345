import java.util.*;
import java.io.*;

public class Main {
	
	static StringBuilder sb = new StringBuilder();
	static int n,m;
	static int[] arr;
	static boolean[] isUsed;
	
	static void bt(int depth)  {
		if(depth==m) {
			for(int val : arr) {
				sb.append(val).append(' ');
			}
			sb.append('\n');
			return;
		}
		
		for (int i=0; i<n; i++) {
			if(!isUsed[i]) {
				isUsed[i] = true;
				arr[depth] = i+1;
				bt(depth+1);
				isUsed[i] = false;
			}
		}		
	}
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		arr = new int[m];
		isUsed = new boolean[n];
		
		bt(0);
		System.out.println(sb);
	
	}
	
	
}