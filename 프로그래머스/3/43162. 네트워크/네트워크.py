#루트 노드 찾기 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#합치기 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    #부모 테이블 초기화
    parent = [0] * (n+1)
    for i in range(n+1):
        parent[i] = i
    #computers 데이터 기반 루트노드 변경
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            if computers[i][j] == 1:
                union_parent(parent, i+1, j+1)
    
    #부모테이블 업데이트
    for i in range(1, n+1):
        parent[i] = find_parent(parent, i)
    #부모테이블 기반 네트워크 개수 구하기
    return len(set(parent[1:]))