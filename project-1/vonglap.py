#nhap vao mot day so, kiem tra cac so nao la chan le/ so nguyen to, so luong so nguyen to
import math
a=[]
b=[]
c=[]
d=[]
n=int(input("do dai day so:"))
#nhap day so:
for i in range(n):
	x=int(input())
	a.append(x)
print('Day so:', a)
#kiem tra chan le:
def check1(m):
		if m%2==0:
			return True
		else:
			return False
#kiem tra so nguyen to:
def check2(n):
	if n<2:
		return False
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True
#ham main
if __name__=='__main__':
	print('KIEM TRA SO NGUYEN TO: ')
	for x in a:
		if check2(x):
			print(x, "la snt")
			b.append(x)
		else:
			print(x, "ko la snt")
	print("KIEM TRA SO CHAN LE: ")
	for y in a:
		if check1(y):
			print(y, "la so chan")
			c.append(y)
		else:
			print(y, "la so le")
			d.append(y)
print("cac snt la", b)
print('so cac snt la:', len(b))
print("day cac so chan", c)
print("day cac so le", d)