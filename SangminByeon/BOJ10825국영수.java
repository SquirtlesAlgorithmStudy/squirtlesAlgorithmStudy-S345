import java.util.*;
import java.io.*;


public class Main {
	
	static int n;
	static ArrayList<Student> reports = new ArrayList<>();

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine().trim());
		
		while(n-->0) {
			String[] temp = br.readLine().trim().split(" ");
			reports.add(new Student(
					temp[0], 
					Integer.parseInt(temp[1]), 
					Integer.parseInt(temp[2]), 
					Integer.parseInt(temp[3])));
		}
		
		for(Student report: reports)
			System.out.println(report.toString());
		// 입력완료 
		
		
		
		
		
		
    }
	
}

class Student {
	String name;
	int korean;
	int english;
	int math;
	
	Student(String name, int korean, int english, int math) {
		this.name = name;
		this.korean = korean;
		this.english = english;
		this.math = math;
	}
	
	@Override
	public String toString() {
		return name +" "+ korean + " " + english + " " + math;
	}
}