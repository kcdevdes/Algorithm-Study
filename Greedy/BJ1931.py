"""
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는
회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
"""

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

=> (1,4), (5,7), (8,11), (12,14) 4
"""

n = int(input())
data = []
answer = []

for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: x[0])
for count, time in enumerate(data):
    schedule=[]
    time_s = time[0]
    time_e = time[1]
    schedule.append(time)

    # TODO : O(n)으로 풀이해야함.

print(answer)