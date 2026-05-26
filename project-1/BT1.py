mang=[]
a=[]
b=[]
c=[]
n=int(input("so luong hoa qua: "))
for i in range(n):
	x=input()
	mang.append(x)
print(mang)
for j in mang:
	if mang.count(j)>1 and j not in a:
		print("số quả",j,"là: ", mang.count(j))
		a.append(j)

		
	elif mang.count(j)==1 and j not in b:
		print('số quả', j,'là: ', mang.count(j))
sqln=None
max_hq=0
for i in mang:
	if mang.count(i)>max_hq :
		max_hq=mang.count(i)
		sqln=i
print("so qua xh nhieu nhat la: ", sqln)
