#nhap ten, so ban thang, so kien tao, vi tri cua cac cau thu va in ra vua pha luoi, vua kien tao va qua bong vang


dic=[]
#vong lap vo han
def Fifacheck():
	while True:
		name=input('ten cau thu: ')
		if name.lower() == "stop": 
			break
		goal=int(input('so ban thang: '))
		assist=int(input("so kien tao: "))
	player={ "name":name, "goal":goal, "assist":assist }
	dic.append(player)

if __name__=='__main__':
	Fifacheck()
	vuaphaluoi=" "
	vuakientao=" "
	maxg=-1
	maxa=-1
	for d in dic:
		#vua pha luoi
		if d['goal']>maxg:
			maxg=d['goal']
			vuaphaluoi=d['name']
			print(vuaphaluoi,"la vpl")
		#vua kien tao
		if d['assist']>maxa:
			maxa=d['assist']
			vuakientao=d['name']
			print(vuakientao, "la vkt")



