import java.util.*;
import java.io.*;

public class Main {
	
	static int n,m;
	static int[] sequence;
	static int[] numbers;
	static StringBuilder sb = new StringBuilder();
	
	static void bt(int depth, int k) {
		if(depth==m) {
			for(int val:sequence) {
				sb.append(val).append(" ");
			}
			sb.append("\n");
			return;
		}
		for(int i=k; i<n; i++) {
			sequence[depth] = numbers[i];
			bt(depth+1, i+1);
		}
	}
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		sequence = new int[m];
		numbers = Arrays.stream(br.readLine().trim().split(" "))
				.map(s -> Integer.parseInt(s))
				.mapToInt(i->i)
				.toArray();
		Arrays.sort(numbers);
		
		bt(0,0);
		System.out.println(sb);
		
	}
}