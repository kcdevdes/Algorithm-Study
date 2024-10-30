# DFS, BFS
## Stack 스택
- 박스를 쌓듯이 구현하는 자료구조
- 먼저 들어간 데이터가 가장 이후에 나오는 데이터구조. 선입후출(First In Last Out)구조를 가진다.
- 입력은 push(), 출력은 pop()을 사용한다.
- 파이썬에선 일반 List로 구현이 가능하다. `(stack = list())`
  - list로 스택을 구현하면, `append()`와 `pop()`을 사용한다.
- `stack[::-1]`로 거꾸로 출력할 수 있다.

## Queue 큐
- 대기 줄에 서듯이 구현하는 자료구조
- `from collections import deque`를 대입하면 deque 자료구조를 사용할 수 있다.
- `append()`로 삽입, `popleft()`로 출력을 담당한다.
- `reverse()`로 거꾸로 출력도 가능하다.