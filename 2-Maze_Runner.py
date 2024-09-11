import redboard
import ultrasonic

done = True

def Forward():
	print("Forward")
	redboard.M1(25)
	redboard.M2(20)
def Right(sleep):
	redboard.M1(-15)
	redboard.M2(-15)
	redboard.time.sleep(.25)
	redboard.M1(0)
	redboard.M2(0)
	redboard.time.sleep(.15)
	redboard.M1(75)
	redboard.M2(-75)
	redboard.time.sleep(sleep)
	redboard.M1(0)
	redboard.M2(0)
def Left(sleep):
	redboard.M1(-15)
	redboard.M2(-15)
	redboard.time.sleep(.25)
	redboard.M1(0)
	redboard.M2(0)
	redboard.time.sleep(.15)
	redboard.M1(-75)
	redboard.M2(75)
	redboard.time.sleep(sleep)
	redboard.M1(0)
	redboard.M2(0)

turnCount = 0
dist = 100
done = True
ultrasonic.Cleanup()

while False:
	dist = ultrasonic.GetDistance()	
	print(f'First distance {dist}')
	if dist < 20:
		print(f'Under 30 Distance {dist}')
		if turnCount == 0:
			print("R")
			Right(.54)
			turnCount = turnCount + 1
		elif turnCount == 1:
			print("R")
			Right(.5)
			turnCount = turnCount + 1
		elif turnCount == 2:
			print("L")
			Left(.44)
			turnCount = turnCount + 1
		elif turnCount == 3:
			print("L")
			Left(.43)
			turnCount = turnCount + 1
		elif turnCount == 4:
			print("R")
			Right(.45)
			turnCount = turnCount + 1
		elif turnCount == 5:
			redboard.M1(-15)
			redboard.M2(-15)
			redboard.time.sleep(.1)
			redboard.M1(0)
			redboard.M2(0)
			break
	else:
		Forward()
		
while True:
	redboard.M1(5)
	redboard.M2(75)
	redboard.time.sleep(.5)
	redboard.M1(0)
	redboard.M2(0)
	redboard.time.sleep(6)


ultrasonic.Cleanup()
