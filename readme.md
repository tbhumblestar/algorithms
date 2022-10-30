# Algorithm study repo
푼 알고리즘 문제를 기록해두는 레포

<br/>


## 문제별 타입
- H : 어려웠던 문제
- G : 좋아서 다시 풀었으면 하는 문제
- U : 유용한 부분(개념, 메서드..)이 있음
- F : 못풀었음
- 아무 표시없음 : 무난. 굳이 다시볼 필요까지는 없음

<br/>

## 알고리즘 별 팁


### greedy
- 정당성 검토가 필요. 즉, 탐욕적인 선택들이 만들어낼 수 없는 결과를 탐욕적이지 않는 선택들도 만들어낼 수 없다는 것을 증명하면 됨. 그러면 굳이 탐욕적이지 않은 선택을 할 필요가 없으니까

### 완전탐색
- N,M 등 주어지는 값을 완전탐색 여부를 빠르게 체크

### DFS/BFS
- DFS,BFS만으로 문제가 바로 풀리는 경우는 당연히 없음
- DFS,BFS로 구현할 부분을 정하고, 나머지 빈 부분을 어떻게 채워넣을지 고민할 것
- 재귀함수를 사용하는 경우, 재귀함수의 시작조건과 종료조건에 유의해야 함

### 정렬
- 파이썬 기본라이브러리의 정렬속도가 NlogN임
- 이걸로 안된다면 삽입정렬이나 계수 정렬을 고민해볼 것
- 특히 삽입정렬은 데이터가 거의 다 정렬되어 있을 때 매우 빠르다
- 문자열 정렬은 문자열들의 동일한 위치의 글자를 비교하고, 같을 경우 그다음 자리의 글자로 넘어가서 비교하는 방식임

### 이분탐색
- 검색해야 할 경우의 수가 극단적으로 많을 경우에 우선적으로 고려해볼 것
- 이분탐색의 시간복잡도는 LogN임


### 다이나믹 프로그래밍
- 아이디어 자체는 있는데, 시간이 너무 많이 걸린다(ex:완전탐색)할 때 다이나믹 프로그래밍을 사용해 시간을 줄이는 방법을 모색

<br/>

## 참고

### 참고사이트
- 이코테 깃헙 : https://github.com/ndb796/python-for-coding-test

### 문제 출처
- 이것이 코딩 테스트다!(나동빈 저)
- 파이썬 알고리즘 문제풀이(인프런)
- 코딩테스트_고득점_KIT(프로그래머스)