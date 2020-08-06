# PracticeAlgorithm

Collection of program for self algorithm training.

## Commit Test

---

### 백준에서 코딩한 프로그램 모음

---

- [1000번 문제](/baekjoon/1000.cpp)
  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

- [1000번 문제](/baekjoon/1000.py)
  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

- [1001번 문제](/baekjoon/1001.py)
  두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

- [1003번 문제](/baekjoon/1003.py)
  다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

int fibonacci(int n) {

    if (n == 0) {

        printf("0");

        return 0;

    } else if (n == 1) {

        printf("1");

        return 1;

    } else {

        return fibonacci(n‐1) + fibonacci(n‐2);

    }

}

fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.

1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

- [1008번 문제](/baekjoon/1008.c)
  두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

- [1010번 문제](/baekjoon/1010.py)
  재원이는 한 도시의 시장이 되었다. 이 도시에는 도시를 동쪽과 서쪽으로 나누는 큰 강이 흐르고 있다. 하지만 재원이는 다리가 없어서 시민들이 강을 건너는데 큰 불편을 겪고 있음을 알고 다리를 짓기로 결심하였다. 강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다. 재원이는 강 주변을 면밀히 조사해 본 결과 강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)
  재원이는 서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다. (이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.) 재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다. 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.

- [1026번 문제](/baekjoon/1026.py)
  옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
  길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
  S = A[0]*B[0] + ... + A[N-1]*B[N-1]
  S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
  S의 최솟값을 출력하는 프로그램을 작성하시오.

- [1065번 문제](/baekjoon/1065.py)
  어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

- [1149번 문제](/baekjoon/1149.py)
  RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
  집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

- [1158번 문제](/baekjoon/1158.cpp)
  요세푸스 문제는 다음과 같다.
  1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
  N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

- [1168번 문제](/baekjoon/1168.cpp)
  요세푸스 문제는 다음과 같다.
  1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
  N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

- [1181번 문제](/baekjoon/1181.py)
  알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로

- [1212번 문제](/baekjoon/1212.cpp)
  8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.

### 리트코드에서 코딩한 프로그램 모음

---

#### August LeetCoding Challenge

- [8월 3일 Design HashSet](/leetcode/DesignHashSet.py)
- [8월 4일 Valid Palindrome](leetcode/ValidPalindrome.py)
