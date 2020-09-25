#Random Password Generator program
import random
def RandomPasswordGenerator(x):
    lst=[]
    password=""
    for i in range(65,91):
        lst.append(i)
    for i in range(97,123):
        lst.append(i)
    password+=chr(random.choice(lst))
    for i in 33,64,35,36,37,94,38,42:
        lst.append(i)
    for i in range(48,58):
        lst.append(i)
    random.shuffle(lst)
    for i in range(x-1):
        password+=chr(random.choice(lst))
    return password
if __name__ == '__main__':
    try:
        x = int(input("enter length of password to be generated:"))
        if x<1:
            quit()
        print(RandomPasswordGenerator(x))
    except:
        print("Not a number!")
        quit()
    


