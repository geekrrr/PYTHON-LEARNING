# // # print('hello')
# // # print("hello guys", 69 , "ohh yeah")
# // # print(5^3)
# // # a = input("enter the nummber whose square you want to find out")
# // # b = int(a)**2
# // # print("type of a is",b)
# // # c = "yeeeepp"
# // # d = 'oh yeeepppppp'
# // # e = '''welcome back 
# // # i am here to inform u that i am back
# // #     ohhh yeeepppp
# // #     '''
# // # print(c)
# // # print(d)
# // # print(e)
# // # f = "harry"
# // # print(f[-4:-2])
# // # print(f[1:4])
# // # a = "rohit rana !!!"
# // # print(a.rstrip("a"))
# // # print(a.capitalize())
# // # print(a.upper())
# // # print(a.lower())
# // # print(a.split(" "))
# // # print(len(a))
# // # print(a.center(60))
# // # print(a.count("rana"))
# // # print(a.endswith("!!"))
# // # print(a.endswith("a",2,8))
# // # print(a.find("t"))
# // # print(a.index("s"))

# // # import time

# // # timestamp = time.strftime('%H:%M:%S')
# // # print(timestamp)
# // # hours = int(time.strftime('%H'))
# // # if (hours>=6 and hours<12):
# // #  print("good morning sir")
# // # elif (hours>=12 and hours<16):
# // #  print("good afternoon sir")
# // # elif (hours>16 and hours<20):
# // #  print("good evening sir")
# // # else:
# // #  print("good night sir")
# // # i = int(input("enter the value upto where you want to terminate the loop"))
# // # while (i<=9):
# // #     print("oh yeah boy")
# // #     i = i +1
# // # for i in range(0,31):
# // #     print("yeah buddy light weight buddy")
# // # def fullname(firstname , middlename , lastname ="sir"):
# // #     print(firstname , middlename , lastname)
# // # fullname("rohit","rana")
# // # l = [1,2,3,4,5,6]
# // # for i in range(0,6):
# // #  print(l[i])

# // # l = (1,2,3,4,5,6)
# // # # print(l)
# // # l = ["how many states are there in india","how many people live in india","who is the most terrible neighbour of india in terms of terror attacks"]
# // # l1 = [28,23,25,27]
# // # l2 = ["141 billion","140 billion","152 billion","160 billion"]
# // # l3 = ["pakistan","china","srilanka","bangladesh"]

# // # money = 0
# // # for i in range(0,3):
# // #  print(l[i])
# // #  if(i==0):
# // #   print(l1)
# // #  elif(i==1):
# // #   print(l2)
# // #  else:
# // #   print(l3)
# // #  a = int(input("enter ur answer : "))
# // #  if(a == 1):
# // #   print("right answer")
# // #   money = money + ((i+1)*50000)
# // #  else:
# // #   print("Wrong answer!! No money for this question")
# // # print("congratulations you got",mo
# // name = input("enter ur name")
# // age  = input("enter ur age")
# // print(f"hey {name} i am glad that u visitedd out site . according to ur age i.e. {age} you can drive now")
# exceptional handling
# try:
#     a = int(input("enter the value"))
#     array = [1,2,3]
#     print(array[a])
# except ValueError:
#     print("Wrong answer")
# except IndexError:
#     print("index array")
# finally:              # finally keyword has a great role in functions 
#     print("i am always executed")     
# raise keyword is used to raise error intentionally by the programmer
