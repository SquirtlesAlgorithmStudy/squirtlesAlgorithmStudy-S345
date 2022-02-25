import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort(reverse=True)
B.sort()
# print(rope)
answer = 0
for i in range(n):
  answer += A[i]*B[i]

print(answer)

'''

#include <algorithm>
#include <iostream>
#include <vector>


using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> A;
	vector<int> B;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		A.push_back(a);
	}

	for (int i = 0; i < n; i++) {
		int b;
		cin >> b;
		B.push_back(b);
	}


	sort(A.begin(), A.end());
	sort(B.begin(), B.end());

	int answer = 0;
	for (int i = 0; i < n; i++)
		answer += A[i] * B[n - 1 - i];

		cout << answer;
}

'''