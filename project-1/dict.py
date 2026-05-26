#Nhap lan luot cac cau thu, ban thang va kien tao cua ho/ tu do tim ra vua pha luoi va vua kien tao:
dsach=[]
#Ham nhap cau thu:
def VAR():
	while True:
		name=str(input('Ten: '))
		if name.lower()=='stop': break
		goal=int(input('ban thang: '))
		assist=int(input('kien tao: '))
		player={'name':name, 
		'goal':goal, 
		'assist':assist}
		dsach.append(player)	
if __name__=='__main__':
	VAR()
	maxgoal=0
	maxass=0
	vpl=" "
	vkt=" "
	#Tim vua kien tao va vua pha luoi:
	for player in dsach:
		if player['goal']>maxgoal:
			maxgoal=player['goal']
			vpl=player['name']
		if player['assist']>maxass:
			maxass=player['assist']
			vkt=player['name']
	print(vpl,"la vua pha luoi")
	print(vkt, "la vua kien tao")
