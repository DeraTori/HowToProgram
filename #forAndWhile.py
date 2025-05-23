#forAndWhile
numbers = [1,2,3,4,5]
for num in numbers:
    print(num)

while True:
    user_input = input("正しい値を入力してください:")
    if user_input == "OK":
        print("入力完了")
        break
        
#whileはループ構文なので、終了させる必要がある。
#それがbreak
for i in range(1, 11):
    print(i)
    
while True:
    username =input("値を入力")
    if username== ("OK"):
        print("入力完了")
    break

count = 0
while count < 5:
    print(count)

#ループから抜けたいときbreak

count = 0
while count < 5:
    print(count)
    count +=1
else:
    print("完了")




while True:
    userinput =input("名前を入力")
    if userinput ==("小野寺仁志") or userinput ==("こじま"):
        print("やり")
    break

#while文を使った繰り返し
count = 0
while count < 5:
    print(count)
    count +=1

count = 0
while count <5: #5より小さい間ループする
    print(count)
    count+=1
    
#ATcorder

#シカのAtCoDeerくんは二つの正整数 
#a,b を見つけました。 
#a と 
#b の積が偶数か奇数か判定してください。

a = int(input())
b = int(input())

