package javaAlgorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;
import java.util.Stack;

public class Stack_BOJ_4949 {

	public static void main(String[] args) throws IOException {

		Stack<Character> st = new Stack<Character>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<String> strings = new ArrayList<>();
		
		String str = "";
		while ((str = br.readLine()) != null) {
//            strings.add(str);
//			String[] tokens = str.split("\\s");
            System.out.println(str);

		}
        for(String sentence : strings) {
        	System.out.println(sentence);
        	try {
				final int endIndex = sentence.length();
				for(int i=0; i<endIndex; i++) {
					
					char ch = sentence.charAt(i);
					if (ch =='.') {
						System.out.println("yes");
					}else if (ch =='(') {
						st.push('(');
					}else if (ch == '[') {
						st.push('[');
					}else if (ch == ')') {
						if(st.pop()!='(') {
							System.out.println("no");
							break;
						}
					}else if (ch == ']') {
						if(st.pop()!='['){
							System.out.println("no");
							break;
						}
					}
				}
        	} catch (EmptyStackException e) {
        		System.out.println("no");
        	}
		}
		
	}

}
