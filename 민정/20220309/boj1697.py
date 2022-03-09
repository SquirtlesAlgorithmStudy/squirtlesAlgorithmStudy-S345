from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1,x+1, x*2):
            if 0<=nx<=MAX and not dist[nx]:
                dist[nx]=dist[x]+1
                q.append(nx)
MAX = 100000
dist = [0] * (MAX+1)
n, k = map(int, input().split())

bfs()

'''
#include <iostream>
#include <queue>
using namespace std;

const int M = 100000;
bool dist[(2 * M) + 1];
queue<pair<int, int>> q;
int n, k;

void dfs() {
	q.push({n, 0});
	dist[n] = 0;

	while (!q.empty()) {
		int subin = q.front().first; // 수빈이의 위치
		int t = q.front().second; // 동생 찾는 시간
		q.pop();

		// (1) 범위 벗어나면 컨티뉴
		if (subin<0 || subin>M) continue;
		// (2) 동생 찾았으면 t 출력
		if (subin == k) {
			cout << t;
			break;
		}

		// (3) 동생 찾기
		if (!dist[subin * 2]) {
			dist[subin * 2] = true;
			q.push({ subin * 2, t + 1 });
		}
		if (!dist[subin + 1]) {
			dist[subin + 1] = true;
			q.push({ subin + 1, t + 1 });
		}
		if (!dist[subin - 1]) {
			dist[subin - 1] = true;
			q.push({ subin - 1, t + 1 });
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> k;
	dfs();
}
'''