# 객체 할당

x=3.14159; y='hello world'; z=TRUE
ls()
print(y)
rm(y)
rm(list=ls())

getwd()
setwd('C:/Users/admin/Documents')

y='hello world'

save(y, file='y.RData')
save.image('total.RData')


# 벡터 만들기

vec<- 1:20
vec[3]
vec[3:6]
vec[c(1,3,8)]
vec[vec>15]

5 %in% vec
12 %in% vec
m<- matrix(1:16, nrow=4)
dim(m)
m
t(m)

df<- data.frame(times=c(4,3,5), brand=c('버거킹','맥도날드','롯데리아'))
str(df)
df

df[1,]
df[2:3,]
df[2,1]

names(df)
row.names(df)
df$brand

h=1:4
I<-cbind(h,c(1,2,3,4))
I
j<-rbind(h,c(1,2,3,4))
j

# 인덱싱

data(InsectSprays)
head(InsectSprays)

summary(InsectSprays)

lst=list()
lst[1]='one'
lst[[2]]<-'two'
lst[length(lst)+1]<-'three'
lst
lst[2:3]
lst[c(1,3)]
lst[1]
lst[[1]]

# 반복문 연습
for(i in 1:10){
  print(paste('numbere',i))
}

# 함수 만들기

funcName<-function(para1, para2){
  print(para1)
  print(para2)
  return(para1+para2)
}

funcName(3,4)

