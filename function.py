def sayHello():
    print("Selamat Datang")
    sayHello

def sayHello():
    return "Selamat Datang"
    print (sayHello()) 

def sayHello(name):
    return "Selamat Datang" + name
    print (sayHello("Ahmad"))

def addition(num1, num2):
    result = num1 + num2
    print(num1, "+", num2, "=", result)
    addition(15,16)



def sayHello(name=""):
    return "Selamat Datang" + name    
    print (sayHello()) 

def fullname(fname, lname=""):
    return fname + " " + lname
    print (fullname(lname="Saputra", fname="Cahyo")) 

def addition(*numbers):
    result = 0
    for n in numbers:
        result += n
        return result
    
def fullname(**kwargs):
    values = kwargs.values()
    print(" ".join(values))
    fullname (a= "Ahmad", b= "Dwi", c= "Santoso")
