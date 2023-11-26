from microbit import *
import radio

mic = 0                                              # 音を感知したかどうかのフラグ
radio.config(group=0)                                # 無線グループを0に設定
radio.on()                                           # 無線をオン
display.show('A')                                    # ディスプレイにAと表示
microphone.set_threshold(SoundEvent.LOUD, 1)         # マイクのしきい値を1に設定

# メインループ
while True:
    # マイクが音を拾った時の処理
    if microphone.current_event() == SoundEvent.LOUD:
        mic = 1
        radio.send('A')

    # リセットされるまでの処理
    if mic == 1:
        display.clear()
        sleep(500)
        display.show('A')
        sleep(500)

    # タッチセンサがタッチされたらリセット
    if pin_logo.is_touched():
        mic = 0
        display.show('A')
