import datetime

# OWRNGプログラム一式の設定をするファイルです。

# -----編集範囲-----

# OWRNG1
wait_yasei = 2.9 # 野生の～　からの待機時間

# OWRNG1/OWRNG2共通
motion_full = 130 # 128回のモーションを出す場合の試行回数

# OWRNG1~4共通
wait_Lstick = 1.5 # Lstick入力後の待機時間

# OWRNG4
motion_state = 30 # 現在地特定の試行回数

# OWRNG5
# coming soon

# OWRNG6
frame_ts = 5000 #雷雨で消費したいフレーム
frame_sec = 230 #1秒当たりの消費フレーム
waiting_sec = int(frame_ts / frame_sec) # 待機時間小数点以下切り捨て

# OWRNG7
frame_Lstick = 4800 #Lstick連打で消費したい回数
Lstick_freq = 0.05 #クリック時間と待機時間
time_estimate = int(frame_Lstick*Lstick_freq*2) 

# -----以下は、編集不要-----

print("")
print("--------OWRNG Config--------")
print("")

print("- OWRNG1:リポップ色違い判定->128回モーション測定 -")
print("野生の～からの待機時間 ",wait_yasei,"秒")
print("測定回数 ",motion_full,"回")
print("")

print("- OWRNG2:ソフト起動から128回モーションの測定をします -")
print("測定回数 ",motion_full,"回")
print("Lstickからの待機時間 ",wait_Lstick,"秒")
print("")

print("- OWRNG3:128回モーションの測定をします -")
print("測定回数->",motion_full,"回")
print("Lstickからの待機時間 ",wait_Lstick,"秒")
print("")

print("- OWRNG4: 現在地の特定 -")
print("測定回数 ",motion_state,"回")
print("Lstickからの待機時間 ",wait_Lstick,"秒")
print("")

print("- OWRNG5: 日付変更 -")
print("coming soon")
print("")

print("- OWRNG6: 雷雨での待機 -")
print("目標消費数",frame_ts,"F")
print("1秒あたりの消費数",frame_sec,"F")
print("待機時間",waiting_sec,"秒")
print("")

print("- OWRNG7: Lclickでの消費 -")
print(frame_Lstick,"F消費")
print(Lstick_freq*2,"sec/click")
print("予測時間",datetime.timedelta(seconds=time_estimate))
print("")
print("")
print("- Development by.じゃんきー/アキルノ/お修羅 -")
print("-------------------------")
print("")