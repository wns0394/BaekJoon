import java.io.*;
import java.util.*;

class Solution {
    
    int[] dx = {1,0,-1,0};
    int[] dy = {0,1,0,-1};
    
    public int solution(int[][] maps) {
        int answer = 0;
        
        int[][] visited = new int[maps.length][maps[0].length];
        bfs(maps,visited);
        answer = visited[maps.length-1][maps[0].length-1];
        // System.out.println(Arrays.deepToString(visited));
        // System.out.println(answer);
        if (answer == 0) {
            answer = -1;
        }
        return answer;
    }
    
    public void bfs(int[][] maps, int[][] visited) {
        int x = 0;
        int y = 0;
        visited[x][y] = 1;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x,y});
        
        while(!q.isEmpty()) {
            int[] current = q.remove();
            int cx = current[0];
            int cy = current[1];
            
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                
                if (nx >= 0 && nx < maps.length && ny >=0 && ny < maps[0].length) {
                    if (visited[nx][ny] == 0 && maps[nx][ny] == 1) {
                        q.add(new int[]{nx,ny});
                        visited[nx][ny] = visited[cx][cy] + 1;
                    }
                }
            }
        }
    }
}