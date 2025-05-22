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


#変数名は英数字とアンダーバーをつかう
#数字で始めないで

#シングルクォートとダブルクォートの使い分け
message = 'He said, "Hello!"'
print(message)
#シングルクォートでダブルクォート囲む。逆もできる

#数値型
#整数型intと浮動小数点型float
age = 25 #整数型
height = 5.9 #浮動小数点型
print(age)
print(height)

#真偽型 bool
#TrueかFalseの二つの値をとる

is_active = True
print(is_active)
#リスト
numbers = [1, "two" , 3.0]
print(numbers[1])
#異なる型の要素を使える

#性的型つけ言語と動的型つけ言語
#型変換
x = 10
x_str = str(x)
print(x_str)

#Pythonでは、変数を宣言する際に型を指定する必要はありません。代入するだけで変数が作成されます。
x = 5
y = x +10
print(y)

#p = 10
#def update p():
    #global p
    #p =20
#update_p()
#print(p)


name1 = "Alice"
print(name1)




x = 5

def test_scope():
    x = 10
    print(x)  # このxは何を指しているでしょうか？

test_scope()
print(x)  # このxは何を指しているでしょうか？
#x =10はローカル変数なのでアクセスできない。違う関数の中にあるから
x = 3.14
print(type(x))
