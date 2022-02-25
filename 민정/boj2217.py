import sys

n = int(input())

# 로프는 병렬로 연결

# 만약 중량 w의 물체를 들어올린다면?
# 병렬로 연결 시 각 로프에는 w/n만큼의 중량이 걸리게됨
rope = [int(sys.stdin.readline()) for i in range(n)]
# 역순 정렬
rope.sort(reverse=True)
answer = []

for i in range(n):
  answer.append(rope[i]*(i+1))
print(max(answer))

'''

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int n, rope;
vector<int> vec;

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		vec.push_back(x);
	}

	sort(vec.rbegin(), vec.rend());

	for (int i = 0; i < n; i++)
		rope = max(rope, vec[n - i - 1] * (n - i));

	cout << rope;
}

'''