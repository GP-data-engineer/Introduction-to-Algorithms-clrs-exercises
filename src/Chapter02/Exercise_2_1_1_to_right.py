'''
for n in [10, 100, 1000, 10000]:
    value = (n**3)/1000 - 100*(n**2) - 100*n + 3
    print(f"n = {n:<6}  f(n) = {value:<20}  Dominant term: n^3")
'''
A = [9,8,7,6,5,4,3,2,1,0]
#A = [5,8,7,6,9,4,3,2,1,0]

for j in range(1,len(A)):
    print("j=",j)
    key = A[j]
    i=j-1
    print("for dla key= ",key,"A[i+1]=", A[i+1],"i=",i,"len(A)=",len(A),", A=",A)
    while i >= 0 & key < A[i]:
        print("przesuwanie w prawo " , A[i])
        A[i+1] = A[i]
        A[i] = key
        i-=1
    
    print("Tab po -> ",A)
print("liczba elmenetów do sortowania: ", len(A))
print("Tablica końcowa posotrowana z lewej do prawj: ",A)