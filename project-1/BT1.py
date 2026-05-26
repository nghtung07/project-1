mang=[]
a=[]
b=[]
n=int(input("so luong hoa qua: "))
#ham nhap mang:
for i in range(n):
	x=input()
	mang.append(x)
print(mang)
#Dem so lan xuat hien cua cac loai qua:
for j in mang:
	if mang.count(j)>1 and j not in a:
		print("số quả",j,"là: ", mang.count(j))
		a.append(j)		
	elif mang.count(j)==1 and j not in b:
		print('số quả', j,'là: ', mang.count(j))
#Tim so qua xuat hien nhieu nhat:
sqln=None
max_hq=0
for i in mang:
	if mang.count(i)>max_hq :
		max_hq=mang.count(i)
		sqln=i
print("so qua xh nhieu nhat la: ", sqln)
