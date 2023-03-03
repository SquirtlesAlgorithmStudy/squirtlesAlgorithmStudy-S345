import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		List<String> editor = new LinkedList<>();
		String[] temp = br.readLine().trim().split("");
		int cs = 0; //cursor
		
		for (String t:temp) {
			editor.add(t);
			cs++;
		}
		
		int m = Integer.parseInt(br.readLine().trim());
		String[][] commands = new String[m][2];
		
		for(int i=0; i<m; i++) {
			String[] command = br.readLine().trim().split(" ");
			commands[i] = command;
		}
		
//		System.out.println(editor.toString());
//		System.out.println(Arrays.deepToString(commands));
		
		for(String[] command : commands) {
			if ("L".equals(command[0]) && cs>0) {
				cs--;
			}
			else if ("D".equals(command[0]) && cs<editor.size()) {
				cs++;
			}
			else if ("B".equals(command[0]) && cs>0) {
				editor.remove(--cs); 
			}
			else if ("P".equals(command[0])) {
				editor.add(cs++, command[1]);
			}
//			else {
//				System.out.println("IGNORED: " + command[0]);
//			}
		}
		
		for(String letter : editor) {
			sb.append(letter);
		}
		
		System.out.println(sb);

	}
}
