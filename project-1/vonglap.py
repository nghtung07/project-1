#nhap ten, so ban thang, so kien tao, vi tri cua cac cau thu va in ra vua pha luoi, vua kien tao va qua bong vang


player={}
#vong lap vo han
def Fifacheck():
	while True:
		name=str(input("Ten cau thu: "))
		if (name.lower() == "stop"): 
			break
		goal=int(input('so ban thang: '))
		assist=int(input("so kien tao: "))


if __name__=='__main__':
	Fifacheck()
	max_goal=0
	max_assist=0
	vuaphaluoi= " "
	vuakientao= " "
	for name in player:
		#vua pha luoi
		if player[goal]>max_goal:
			max_goal=player[goal]
			vuaphaluoi=player[name]

		#vua kien tao
		if player[assist]>max_assist:
			max_assist=player[assist]
			vuakientao=player[name]
	print(vuakientao, "la vkt")
	print(vuaphaluoi, "la vpl")


