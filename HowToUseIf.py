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

#連想配列とは

#pythonでは辞書のこと。名前がついていて取り出すことができる。
original_array = [
  { 'key': 'A', 'date': '2023/05/01', 'regiDate': '2023/04/25' },
  { 'key': 'B', 'date': '2023/05/02', 'regiDate': '2023/04/26' },
  { 'key': 'C', 'date': '2023/05/03', 'regiDate': '2023/04/27' },
  { 'key': 'A', 'date': '2023/05/04', 'regiDate': '2023/04/28' }, # Aの新しいdate
  { 'key': 'D', 'date': '2023/05/05', 'regiDate': '2023/04/29' },
  { 'key': 'B', 'date': '2023/05/02', 'regiDate': '2023/04/30' }, # Bのdateは同じだがregiDateが新しい
  { 'key': 'E', 'date': '2023/05/07', 'regiDate': '2023/05/01' },
  { 'key': 'D', 'date': '2023/05/08', 'regiDate': '2023/05/02' }, # Dの新しいdate
  { 'key': 'C', 'date': '2023/05/09', 'regiDate': '2023/05/03' }, # Cの新しいdate
  { 'key': 'A', 'date': '2023/05/04', 'regiDate': '2023/05/04' }  # Aのdateは同じだがregiDateが新しい
]

def deduplicate_array_python(arr):
    # 日付文字列を比較可能なdatetimeオブジェクトに変換するためのヘルパー関数
    def to_datetime(date_str):
        # datetimeオブジェクトは直接比較が可能
        from datetime import datetime
        return datetime.strptime(date_str, '%Y/%m/%d')

    # keyをキーとし、最新の要素を値とする辞書を作成
    latest_items = {}

    for item in arr:
        key = item['key']
        current_date_obj = to_datetime(item['date'])
        current_regi_date_obj = to_datetime(item['regiDate'])

        if key not in latest_items:
            # まだ辞書にこのkeyの要素がなければ、そのまま追加
            latest_items[key] = item
        else:
            # 既に辞書にこのkeyの要素が存在する場合、日付を比較
            existing_item = latest_items[key]
            existing_date_obj = to_datetime(existing_item['date'])
            existing_regi_date_obj = to_datetime(existing_item['regiDate'])

            if current_date_obj > existing_date_obj:
                # 現在のアイテムのdateが新しければ、置き換える
                latest_items[key] = item
            elif current_date_obj == existing_date_obj:
                # dateが同じ場合はregiDateを比較
                if current_regi_date_obj > existing_regi_date_obj:
                    # 現在のアイテムのregiDateが新しければ、置き換える
                    latest_items[key] = item
    
    # 辞書の値（最新の要素のリスト）を返す
    return list(latest_items.values())

deduplicated_array_py = deduplicate_array_python(original_array)
for item in deduplicated_array_py:
    print(item)