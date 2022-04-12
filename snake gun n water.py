import random
def game(comp,u):
	if comp=="snake"or comp=="Snake":
		if u=="water"or u=="Water":
			return False
		elif u=="gun"or u=="Gun":
			return True
		elif comp==u:
			return "t"
		else:
			print("Please! enter valid option.")
	elif comp=="gun"or comp=="Gun":
		if u=="snake"or u=="Snake":
			return False
		elif u=="water"or u=="Water":
			return True
		elif comp==u:
			return "t"
		else:
			print("Please! enter valid option.")
	elif comp=="water"or comp=="Water":
		if u=="gun" or u=="Gun":
			return False
		elif u=="snake"or u=="Snake":
			return True
		elif comp==u:
			return "t"
		else:
			print(f"You choose --> {u}")
			print("Please! enter valid option.")
pscore=0
cscore=0
highscore=0

print("            -----------Rules-----------\n1.) 10 points for winning a round.\n2.)If round tied then 3 point will given to each.\n3.)if you enter invalid choice then that round will not be counted.\n ")
n=int(input("how many round do you want to play ?"))
r=1
while r<=n:
	print(29*"*",end="")
	print(f"Round-->{r}",end="")
	print(29*"*")
	randomno=random.randint(1,3)
	if randomno==1:
		computer="gun"
	elif randomno==2:
		computer="water"
	elif randomno==3:
		computer="snake"
	you=str(input("\nchoose any one gun, water, or snake -->"))
	a=game(computer,you)
	print(f"You choose --> {you}")
	print(f"Computer choose --> {computer}")
	if a=="t":
		print("Round tie.")
		r=r+1
		pscore=pscore+3
		cscore=cscore+3
	elif a==True:
		print("You won.")
		pscore=pscore+10
		r=r+1
	elif a==False:
		print("You lose.")
		cscore=cscore+10
		r=r+1
	else:
		pass
	print("Your score-->",pscore)
	print("Computer score-->",cscore)
	print()
d=abs(pscore-cscore)
if pscore<cscore:
	print(f"you lost by-->{d} points.")
elif cscore<pscore:
	print(f"you won by-->{d} points.")
else:
	print("Game tied")

	