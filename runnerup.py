Author : Abdul Hameed
Runner_Up Score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max = -100
    runnerup = -100
    for x in arr:
        if x > max:
            runnerup = max
            max = x;
        elif x > runnerup and x != max:
            runnerup = x
    print(runnerup)
