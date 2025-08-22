lambda name : print("Selamat Datang", name)
SayHello  = lambda name : print("Selamat Datang", name)
SayHello("Ahmad")

(lambda : print("Selamat Datang"))()
(lambda name : print("Selamat Datang"))("Ahmad")
(lambda name= " " : print("Selamat Datang", name))()