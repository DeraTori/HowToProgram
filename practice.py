a= 10
b = 20
c = a + b
print(c)

def saysometing(): #defは関数
    message = "こんにちは、私は小野寺です" #これがローカル変数
    print(message)
#関数の中で定義した関数をローカル変数という。この関数の中でしか使えない
saysometing()

#print(massage)は関数の外なのでできない
message1= "こんばんは私は小野寺です"
def saysometing1():
   print(message1)
saysometing1()
#関数の外で定義して関数の中で呼び出した場合グローバル変数といいどこでも使える

#https://www.youtube.com/watch?v=2WiAu5pjJeQを参照した。