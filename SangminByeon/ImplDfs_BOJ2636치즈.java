import java.util.*;
import java.io.*;

public class Main {
	
	final static int AIR = 9;
	final static int CWM = 8; //Cheese that Will Melt 
	
	static int y, x, cnt; //세로: y, i 가로: x,j
	static int cheeseNum = 0;
	static Integer[][] pan; // arr[y][x]
	static boolean[][] visited;
	
	public static boolean AirDetectionDfs(int py, int px) { //parameter y, parameter x
		
		if (px<0 || px>=x || py<0 || py>=y)
			return false;
		if ((pan[py][px] == 0 || pan[py][px] == AIR) && !visited[py][px]) {
			pan[py][px] = AIR; // 공기 표시 
			visited[py][px] = true;
			AirDetectionDfs(py+1,px);
			AirDetectionDfs(py-1,px);
			AirDetectionDfs(py,px+1);
			AirDetectionDfs(py,px-1);
			return true;
		}
		return false;
	}
	
	public static int CheeseDetectionDfs(int py, int px) {
		if (px<1 || px >=x-1 || py<1 || py>=y-1)
			return 0;
		if(pan[py][px] == 1 && !visited[py][px]) {
			visited[py][px] = true;
			if(pan[py+1][px] == AIR  // 공기와 맞닿은 치즈 표시 
					|| pan[py-1][px] == AIR
					|| pan[py][px+1] == AIR
					|| pan[py][px-1] == AIR) {
				pan[py][px] = CWM;
			}
			CheeseDetectionDfs(py+1,px);
			CheeseDetectionDfs(py-1,px);
			CheeseDetectionDfs(py,px+1);
			CheeseDetectionDfs(py,px-1);
			return cheeseNum+=1;
		}
		return 0;
	}
	
	
	
	
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		
		y = Integer.parseInt(st.nextToken());
		x = Integer.parseInt(st.nextToken());
		pan = new Integer[y][x];
		visited = new boolean[y][x];
	
		for(int i=0; i<y;i++) {
			pan[i] = Arrays.stream(br.readLine().trim().split(" "))
					.map(s -> Integer.parseInt(s))
					.toArray(Integer[]::new);
		}
		
//		for (Integer[] raw : pan) {
//			System.out.println(Arrays.toString(raw));
//		}
		// 입력 완료 
		
		int sumArr = 0;
		int hour = 0;

		while (sumArr < AIR*x*y) { //pan의 모든 요소가 AIR이 될때 까지 반복 
			cnt = 0;
			hour++;
//			System.out.println("-----"+ hour + "-----");


			// 1. Air Detection 
//			System.out.println("Air Detection");
			
			AirDetectionDfs(0,0); // 매번 0,0 에서부터 공기 영역 감지
			visited = new boolean[y][x];
			
//			for (Integer[] raw : pan) {
//				System.out.println(Arrays.toString(raw));
//			}
//			System.out.println();

			
			// 2. Cheese Detection
//			System.out.println("Cheese Detection");
			
			cheeseNum = 0;
			for(int i=1; i<y-1; i++) {
				for(int j=1; j<x-1; j++) { // pan의 가장자리는 무조건 공기임.
					CheeseDetectionDfs(i,j);
//					System.out.println(cheeseNum);
				}
			}
			visited = new boolean[y][x];
			
//			for (Integer[] raw : pan) {
//				System.out.println(Arrays.toString(raw));
//			}
//			System.out.println();

			
			//3 Cheese Melting
//			System.out.println("Cheese Melting");
			
			for(int i=1; i<y-1; i++) {
				for(int j=1; j<x-1; j++) { // pan의 가장자리는 무조건 공기임.
					if (pan[i][j] == CWM) {
						pan[i][j] = AIR;
					}
				}
			}
			AirDetectionDfs(0,0); // 멜팅 이후에도 0,0 에서부터 공기 영역 감지

			
//			for (Integer[] raw : pan) {
//				System.out.println(Arrays.toString(raw));
//			}
//			System.out.println();

			
			sumArr = Arrays.stream(pan)
					.flatMap(list -> Arrays.stream(list))
					.reduce(0, Integer::sum);
			
		}
		
		System.out.println(hour);
		System.out.println(cheeseNum);
		
		
    }
}