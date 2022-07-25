m1<- matrix(1:16, nrow=4)
dim(m1)
m1
t(m1)
m2<-matrix(1:16, nrow=4, byrow=T)
m2
m1+1
m1*2
m1
m1+m2
m1*m2
m2
m1
m1 %*% m2

m3=matrix(1:25, nrow=5)
m3
diag(m3)
diag(m2)

# 역행렬 계산하기
A=matrix(c(2,-5,4,1,-2,1,1,-4,6), byrow=T, nrow=3)
B=solve(A)
print(B)

c=c(-3,5,10)
c
b

# 역행렬이 존재하지 않는 행렬 D 만들고 행렬식 계산

D=matrix(c(2,-5,4,1,-2,1,1,-4,5), byrow=T, nrow=3)
solve(D)
D[1,]*2+D[2,]*-3
D[3,]
det(A)
det(D)

