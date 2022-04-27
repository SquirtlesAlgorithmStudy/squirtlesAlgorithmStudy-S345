import sys
fastin = sys.stdin.readline
k, n = map(int, fastin().split())
LAN = [int(fastin()) for _ in range(k)]
start, end = 1, max(LAN)

while start <= end:
  mid = (start + end) // 2
  lines = 0
  for i in LAN:
    lines += i // mid

  if lines >= n:
    start = mid + 1
  else:
    end = mid - 1

print(end)


'''
#include <iostream>
using namespace std;

int k, n, ans;
int line[10001];
int M = 0;
long long mid, End, Start;

int main(){
    cin >> k >> n;
    for (int i = 0; i < k; i++){
        cin >> line[i];
        if (M < line[i]) M = line[i];
    }
    
    Start = 1;
    End = M;
    ans = 0;
    
    while (Start <= End){
        mid = (Start + End) / 2;
        int cnt = 0;
        
        for (int i = 0; i < k; i++)
            cnt += line[i] / mid;
        
        if (cnt >= n){
            Start = mid + 1;
            if (ans < mid) ans = mid;
        }
        else{
            End = mid - 1;
        }
    }
    cout << ans;
}
'''