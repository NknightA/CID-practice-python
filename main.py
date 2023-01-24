
print('お金を入れてください．(半角数字で!!)')

money = input()

payment_type = type(money)
payment = int(money)
payment_error = money [-1]

print(payment_error)
print(payment)

"""以下1or5円エラー判定"""
if payment_error == "0" :
  print('商品を選んでください')
  drink_num = int(input())

  """判定後商品選択およびエラー処理"""
  if drink_num == 1:
    print('お茶 \\100')
    
    """釣銭計算"""
    change = payment - 100
    if change == 0:
      print('ありがとうございます。')
    elif change > 0:
      print('おつりは'+ str(change) + '円です。ありがとうございます。')
    else:
      print("お金が足りません。")
  elif drink_num == 2:
    print('オレンジ \\100')
    
    """釣銭計算"""
    change = payment - 100
    if change == 0:
      print('ありがとうございます。')
    elif change > 0:
      print('おつりは'+ str(change) + '円です。ありがとうございます。')
    else:
      print("お金が足りません。")
  elif drink_num == 3:
    print('モンスターエナジー \\180')
    change = payment - 180
    if change == 0:
      print('ありがとうございます。')
    elif change > 0:
      print('おつりは'+ str(change) + '円です。ありがとうございます。')
    else:
      print("お金が足りません。")
  else:
    print('終了')

else:
  print('NG')

