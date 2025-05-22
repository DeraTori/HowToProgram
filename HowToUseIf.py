#HowToUseIf
#10より大きいか小さいか
# ==が本来の意味のイコールです
x = 10
if x >10:
    print("Xは10より大きい")
elif x ==10:
    print("xは10である")
else:
    print("Xは10より小さい")

#70点以上で合格、90点以上で優秀、70点より低ければ不合格
score = 85
if score >=70:
    print("合格")
elif score >= 90:
    print("優秀")
else:
    print("不合格")

#ネスト
x = 10
if x > 0:
    if x % 2 == 0:
        print("xは正の偶数")
    else:
        print("xは正の奇数")
#xが正の偶数か確かめるプログラム

x = 10 
if x >=0:
    if x % 2 == 0:
        print("正の偶数")
else:
    print("正の偶数ではない")


#三項演算子

# Pythonでは、簡単な条件分岐を1行で記述することができます。これを三項演算子と呼びます。
#書く順番
#値1 if 条件式 else 値2

x =10

result = "偶数" if x%2 == 0 else "奇数"
print(result)

x = 70
y = 69

diff = y - x

if  (diff<=2) and (diff > 0): # ← ここの構文と条件に修正が必要です
    print("階段を利用")
elif (diff >= -3) and (diff <0): # ← この下りの条件はかなり良い線いっています！
    print("階段を利用")
else:
    print("エレベーターを利用")

age= int (input())
if (age >=6) and (age <=12):
    print("500円")
elif (age >12) and (age <=17):
    print("1000円")
elif age>=18:
    print("1800円")
else:
    print("無料")

#スコープとは
x = 10  # グローバルスコープ

def my_function():
    y = 5  # ローカルスコープ
    print(x)  # グローバル変数にアクセス可能
    print(y)  # ローカル変数にアクセス可能

my_function()
# print(y)  # エラー: yは関数内でのみ有効

username = hitoshi
def change_username():
    username = input()
def display_username()
username()
