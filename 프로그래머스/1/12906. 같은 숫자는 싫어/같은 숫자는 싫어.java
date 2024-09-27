import java.util.*;

public class Solution {
    public int[] solution(int []arr) {

        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> newlist = new ArrayList<Integer>();
        
        newlist.add(arr[0]);
        
        for (int i = 1; i<arr.length; i++) {
            if (arr[i] != arr[i-1]) {
                newlist.add(arr[i]);
            }
        }
        int[] answer = new int[newlist.size()];
        for (int i=0; i < newlist.size(); i++) {
            answer[i] = newlist.get(i);
        }
        // System.out.println(newlist);
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        // System.out.println("Hello Java");

        return answer;
    }
}