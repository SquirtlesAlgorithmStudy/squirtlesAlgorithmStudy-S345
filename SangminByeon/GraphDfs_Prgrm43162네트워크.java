class Solution {
    //세로, i, y
    //가로, j, x
    //arr[세로][가로]
    
    
    public boolean dfs(int y, int x, int[][] graph) {
        // if (y==x) continue;
        if (graph[y][x] == 1) {
            graph[y][x] = 2; // 방문 표시
            for(int i=0; i<graph[0].length; i++) {
                dfs(x,i,graph);
            }
            return true;
        }
        return false;
    }
    
    public int solution(int n, int[][] computers) {
        int cnt = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if (dfs(i, j, computers)==true){
                    cnt++;
                }
            }
        }
        
        return cnt;
    }
}