from microbit import *
import radio

radio.config(group=0)                                 # 無線グループを0に設定する
radio.on()                                            # 無線をオンにする
mode = pin0.read_digital()                            # Pin0を読み取りモードにする
timerflag = 0                                         # タイマーフラグを0にする 0:目覚まし未動作 1:目覚まし動作
mode = 0                                              # 動作モードを0にする 0:家電モード 1:目覚ましモード
timer = 0                                             # 設定時間を0にする
display.show(Image.HAPPY)                             # 笑顔を表示する

while True:
    
    if mode == 0:                                     # モード0の時の処理、タイマーフラグを1にする（タイマーアップしていない）
        timerflag = 1
    message = radio.receive()                         # 無線を読み取る
    if message:                                       # 無線を受信していた時の処理
        if mode == 0:                                 # 家電モードだった時の処理
            if message == '0':                        # 無線のメッセージが0（ポット）の時
                display.show(Image('00900:'
                                   '00000:'
                                   '00000:'
                                   '00000:'
                                   '00000:'))
            if message == '1':                        # 無線のメッセージが1（炊飯器）の時
                display.show(Image('00090:'
                                   '00000:'
                                   '00000:'
                                   '00000:'
                                   '00000:'))
            if message == '2':                        # 無線のメッセージが2（トースター）の時
                display.show(Image('00009:'
                                   '00000:'
                                   '00000:'
                                   '00000:'
                                   '00000:'))
            if message == 'A':                        # 無線のメッセージがA（冷蔵庫）の時
                display.show(Image('90000:'
                                   '00000:'
                                   '00000:'
                                   '00000:'
                                   '00000:'))
            if message == 'B':                        # 無線のメッセージがB（インターホン）の時
                display.show(Image('00000:'
                                   '00000:'
                                   '00000:'
                                   '00009:'
                                   '00000:'))

    if pin_logo.is_touched():
        display.show(Image.HAPPY)
        
    mode = pin0.read_digital()                        # Pin0を読んで、モードを設定する。 

    if mode == 1:                                     # モード1の時の処理
        if timerflag == 1:                            # タイマーフラグが1（タイマーアップしていない）の時の処理      
            sleep(timer * 1000)                       # timer * 1000 * 60 * 60時間sleep（デモの時はtimer * 1000秒）
            pin1.write_digital(1)                     # Pin1をオンにする（アロマを動かす）
            display.show(Image('09990:'
                               '90009:'
                               '90009:'
                               '90009:'
                               '09990:'))
            sleep(1000)
            timerflag = 0                             # タイマーフラグを0（タイマーアップした）にする
            display.show(Image.HAPPY)
            
    if pin2.is_touched():                             # Pin2がタッチされたときの処理、Pin1をオフにする（アロマを止める）
        pin1.write_digital(0)
        
    if button_a.was_pressed():                        # ボタンAが押されたとき、目覚ましタイマー時間を減らす
        timer -= 1 
        if timer < 0:
            timer = 0
        display.show(timer)
        
    if button_b.was_pressed():                        # ボタンBが押されたとき、目覚ましタイマー時間を増やす
        timer += 1
        if timer > 9:
            timer = 9
        display.show(timer)
               
               
