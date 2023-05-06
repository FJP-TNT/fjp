input.onButtonPressed(Button.A, function () {
    if (H < 23) {
        H += 1
    } else {
        H = 0
    }
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("" + H + ":" + fommat_m)
})
input.onButtonPressed(Button.B, function () {
    if (M < 59) {
        M += 1
    } else {
        M = 0
    }
    if (M < 10) {
        fommat_m = "0" + ("" + M)
    } else {
        fommat_m = "" + M
    }
})
let fommat_m = ""
let M = 0
let H = 0
H = 19
M = 55
if (M < 10) {
    fommat_m = "0" + ("" + M)
} else {
    fommat_m = "" + M
}
basic.forever(function () {
    basic.pause(60 * 1000)
    if (M < 59) {
        M += 1
    } else {
        M = 0
    }
    if (H < 23) {
        H += 1
    } else {
        H = 0
    }
    if (M < 10) {
        fommat_m = "0" + ("" + M)
    } else {
        fommat_m = "" + M
    }
})
