import java.util.*;
import java.io.*;


public class Main {
	
	static int n;
	static ArrayList<Student> reports = new ArrayList<>();
//	static Student[] reports;

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine().trim());
//		reports = new Student[n];
		
		for(int i=0; i<n; i++) {
			String[] temp = br.readLine().trim().split(" ");
			reports.add(new Student(
					temp[0], 
					Integer.parseInt(temp[1]), 
					Integer.parseInt(temp[2]), 
					Integer.parseInt(temp[3])));
//			reports[i] = new Student(
//					temp[0], 
//					Integer.parseInt(temp[1]), 
//					Integer.parseInt(temp[2]), 
//					Integer.parseInt(temp[3]));
		}
		
//		for(Student report: reports)
//			System.out.println(report.toString());
		// 입력완료 
		
		Comparator<Student> myComparator = new Comparator<Student>() {

			@Override
			public int compare(Student o1, Student o2) {
				if(o1.korean < o2.korean) {
					return 1;
				} else if(o1.korean == o2.korean) {
					if(o1.english > o2.english) {
						return 1;
					} else if(o1.english == o2.english) {
						if(o1.math < o2.math) {
							return 1;
						} else if(o1.math == o2.math) {
							return o1.name.compareTo(o2.name);
						}
					}
				}
				return -1;
			}
		};
		
		reports.sort(myComparator);
//		Arrays.sort(reports, myComparator);
		
		for (int i=0; i<n; i++) {
			System.out.println(reports.get(i).name);
//			System.out.println(reports[i].name);
		}
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
	
//	@Override
//	public String toString() {
//		// TODO Auto-generated method stub
//		return name +" "+ korean + " " + english + " " + math;
//	}
}