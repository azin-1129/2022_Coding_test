"""1. 다양한 그래프 알고리즘

    크루스칼 알고리즘(그리디)

    위상정렬 알고리즘(큐나 스택)



    그래프: 노드+엣지.

        -인접행렬 생성 시 O(V²) 비용확인 O(1). 플로이드 워셜

        -인접 리스트 생성 시 O(E) 비용확인 O(V). 큐 다익스트라


    서로소 집합: 공통 원소가 없는 두 집합. (union-find 구조)

        -union. A,B의 루트노드 A',B' 중 더 작은 부모노드를 다른 자식노드의 부모 노드로 설정.(반복)

        -find

    서로소 집합을 이용해 무방향 그래프 내 사이클 판별 가능. """


#10-1 서로소 집합 알고리즘

def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
v,e=map(int,input().split())

parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i
    
for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)
    
print('각 원소가 속한 집합:',end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
    
print()

print('부모 테이블:',end='')
for i in range(1,v+1):
    print(parent[i],end=' ')


#위 함수는 find_parent가 비효율적. O(V)

#따라서 이를 경로 압축 기법으로 개선. (find_parent 함수 재귀적 호출)






#10-3 개선된 서로소 집합 알고리즘(경로 압축)

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
        
def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i
    
for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)
    
print('각 원소가 속한 집합:',end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()

print('부모 테이블:',end='')

for i in range(1,v+1):
    print(parent[i],end=' ')


#대략 O(V+M(1+log₂V)). V=노드 개수, M=find_parent 연산 횟수











"""사이클 판별 알고리즘 (모든 간선에 대해 union, find. 무방향만 가능)

    각 엣지 두 루트 노드 확인.

        -다르면 union

        -같으면 cycle"""



#10-4

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i
    
cycle=False

for i in range(e):
    a,b=map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union_parent(parent,a,b)
        
if cycle:
    print("Cycle")
else:
    print("No Cycle")




"""신장트리: 모든 노드를 포함하면서 사이클이 없는 부분 그래프. (트리 성립 조건)

    =모든 노드가 이어져 있으며 싸이클이 없는 그래프."""



"""최소 신장 트리 알고리즘

    크루스칼 알고리즘(그리디)

        간선 정렬. 최단 거리부터 싸이클이 없도록 집합에 포함

            1. 간선 오름차순 정렬

            2. for 간선:

                -사이클 O: 집합 포함 X union X

                -사이클 X: 집합 포함 O, union O"""





#10-5

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
v,e=map(int,input().split())
parent=[0]*(v+1)

edges=[]
result=0

for i in range(1,v+1):
    parent[i]=i
    
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
    
edges.sort()

for edge in edges:
    cost,a,b=edge
    
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        
print(result)
