def on_button_pressed_a():
    global H
    if H < 23:
        H += 1
    else:
        H = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("" + str(H) + ":" + fommat_m)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global M, fommat_m
    if M < 59:
        M += 1
    else:
        M = 0
    if M < 10:
        fommat_m = "0" + str(M)
    else:
        fommat_m = "" + str(M)
input.on_button_pressed(Button.B, on_button_pressed_b)

fommat_m = ""
M = 0
H = 0
H = 19
M = 38
if M < 10:
    fommat_m = "0" + str(M)
else:
    fommat_m = "" + str(M)

def on_forever():
    global M, H, fommat_m
    basic.pause(60 * 1000)
    if M < 59:
        M += 1
    else:
        M = 0
    if H < 23:
        H += 1
    else:
        H = 0
    if M < 10:
        fommat_m = "0" + str(M)
    else:
        fommat_m = "" + str(M)
basic.forever(on_forever)
