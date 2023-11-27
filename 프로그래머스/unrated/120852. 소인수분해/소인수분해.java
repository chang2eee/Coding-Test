import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[] answer;
        HashMap<Integer, Integer> map = new HashMap<>();
        int index = 0;
        
        for(int i = 2; i <= n;) //소인수는 1보다 크기에 2부터 시작
        {
        	if(n%i==0) // 나눠지면 인수라는 것
        	{
        		map.put(i, i); //해시맵에 저장
        		n/=i; // n을 소인수로 나누기
        	}
        	else // 나눠지지 않으면 i++;
        	{
        		i++;
        	}
        	
        }
        
        answer = new int[map.size()]; //해시맵 크기만큼
        for(Integer i : map.keySet()) //배열에 값 넣기
        {
        	answer[index] = map.get(i);
        	index++;
        }
        Arrays.sort(answer); //해시맵은 정렬된 상태가 아니기 때문에 정렬
        return answer;
    }
}