import random #импортируем модуль random
pop=1#счетчик
ysl=input("Привет, меня зовут Даниэль, давай поиграем, я загадываю число от 1 до 100, а ты отгадываешь, cогласен? yes/no \n")
if (ysl=="yes"):#если согласен
	daniel=random.randint(1,100)#загадывание числа
	print("Отлично, можешь уже отгадывать")
	user=int(input())
	while (user!=daniel):#до тех пор пока пользователь не отгадает число
		pop+=1
		if (user>daniel):#если число меньше загаданного
			print("Нет, меньше")
		else:#если число больше загаданного
			print("Нет, больше")
		user=int(input())
	pop=str(pop)# меняем тип данных daniel и pop на строковый, чтобы потом вывести вместе с предложением
	daniel=str(daniel)
	print("Поздравляю, ты отгадал число", daniel, "с", pop,"попыток")#поздравление
else:#если не согласен
	print("Я обиделся")
input("\n\n click Enter")#завершение, чтобы программа не закрылась

