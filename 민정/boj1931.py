import sys

fastin = sys.stdin.readline

n = int(fastin())

t = [[0]*2 for _ in range(n)]
for i in range(n):
    t[i][0], t[i][1] = map(int, fastin().split())
    
t.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = t[0][1]
for i in range(1, n):
    if t[i][0] >= end_time:
        cnt += 1
        end_time = t[i][1]
    
print(cnt)


'''

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<pair<int, int>> a(n);
	for (int i = 0; i < n; i++)
		cin >> a[i].second >> a[i].first;

	sort(a.begin(), a.end());
	int savetime = 0, ans = 0;
	for (int i = 0; i < n; i++) {
		if (savetime <= a[i].second) {
			savetime = a[i].first;
			ans++;
		}
	}

	cout << ans;
}

'''