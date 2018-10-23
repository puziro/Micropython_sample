from microbit import *
import radio
# 最初だけ
radio.on()
radio.config(group=1, power=7)
msg1 = "Hello"
msg2 = "Hi"
display.show(Image.HEART)
# ずっと
while True:
    # 変数名を送信
    if button_a.was_pressed():
        radio.send("msg1")
    if button_b.was_pressed():
        radio.send("msg2")     
        # 受信した変数名に応じてメッセージ表示
    rcv_msg = radio.receive()
    if rcv_msg == "msg1":
        display.scroll(msg1)
        display.show(Image.HEART)
    if rcv_msg == "msg2":
        display.scroll(msg2) 
        display.show(Image.HEART)        