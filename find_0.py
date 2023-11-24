digit = int(input())
marks = list(map(int, input().split()))

marks.sort(key=lambda i: bool(i), reverse=True)

print(*marks)