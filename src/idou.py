from microbit import *
import radio

microphone.set_threshold(SoundEvent.LOUD, 1)       # マイクの閾値を1に設定
mic = 0                                            # 音を感知したかどうかのフラグ
radio.config(group=0)                              # 無線グループを0に設定
radio.on()                                         # 無線をオン
number = 0                                         # 場所番号を0に設定
display.show(number)                               # LEDに場所番号を表示

while True:
    # ボタンAが押されたら、場所番号を1減らす
    if button_a.was_pressed():
        number -= 1
        if number < 0:
            number = 0
        display.show(number)
    # ボタンBが押されたら、場所番号を1増やす
    if button_b.was_pressed():
        number += 1
        if number > 2:
            number = 2
        display.show(number)
    # ロゴマークがタッチされたらリセットする
    if pin_logo.is_touched():
        mic = 0
    # マイクが音を感知したらフラグを立てて場所番号を送信する
    if microphone.current_event() == SoundEvent.LOUD:
        mic = 1
        radio.send(str(number))
    # フラグが立っている場合、ディスプレイに場所番号を表示する
    if mic == 1:
        display.clear()
        sleep(500)
        display.show(number)
        sleep(500)
