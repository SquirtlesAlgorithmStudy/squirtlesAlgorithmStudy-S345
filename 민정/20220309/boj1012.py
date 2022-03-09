from collections import deque
import sys

fastin = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(fastin())


def testcasein(T):
    m, n, k = map(int, fastin().strip().split())
    data = [list(map(int, fastin().strip().split())) for _ in range(k)]
    field = [[0] * n for _ in range(m)]
    for i, j in data:
        field[i][j] = 1

    return m, n, k, field, data


def bfs(x, y, k, field, data):
    warms = 0
    q = deque()
    for i in range(k):
        if field[data[i][0]][data[i][1]] == 1:
            nx = data[i][0]
            ny = data[i][1]
            field[data[i][0]][data[i][1]] = 2
            q.append([nx, ny])

            while q:
                x, y = q.popleft()
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if (0 <= nx < m) and (0 <= ny < n):
                        if field[nx][ny] == 1:
                            q.append([nx, ny])
                            field[nx][ny] = 2

            warms += 1
    return warms


result = []

for _ in range(T):
    m, n, k, Field, datas = testcasein(T)
    result.append(bfs(m, n, k, Field, datas))

for i in range(T):
    print(result[i])


'''
// DFS
#include <iostream>
#include <cstring>
using namespace std;

bool check[51][51]; // 가로, 세로길이 1 ~ 50
int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, 1, -1 };
int a[51][51]; // 밭
int m, n, k;

void DFS(int x, int y) {
	check[x][y] = true;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
			if (a[nx][ny] == 1) {
				if (check[nx][ny] == false) {
					DFS(nx, ny);
				}
			}
		}
		else continue;
	}
}

int main() {
	int t;
	cin >> t;
	while (t--) {
		cin >> m >> n >> k;
		int cnt = 0;
		for (int i = 0; i < k; i++) {
			int x, y;
			cin >> x >> y;
			a[y][x] = 1;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (a[i][j] == 1) {
					if (check[i][j] == false) {
						cnt++;
						DFS(i, j);
					}
				}
			}
		}
		cout << cnt << '\n';
		memset(check, false, sizeof(check));
		memset(a, 0, sizeof(a));
	}
}
'''