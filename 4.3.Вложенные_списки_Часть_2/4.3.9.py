# put your python code here
n = int(input())
lst = []

for _ in range(n):
    lst_sub = [i for i in range(1, n + 1)]
    lst.append(lst_sub)
    n -= 1

lst.reverse()
    
print(*lst, sep='\n')