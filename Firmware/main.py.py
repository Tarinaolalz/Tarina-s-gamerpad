
import board


from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler



keyboard = KMKKeyboard()


encoder_handler = EncoderHandler()

PINS = [board.D7, board.D8, board.D9, board.D10, board.D11]


keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)
keyboard.extensions.append(MediaKeys())

encoder_handler.pins = ((board.D5, board.D6, board.D13),)


keyboard.keymap = [
    [KC.W, KC.A, KC.S, KC.D, KC.ESC],
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),)
]


if __name__ == '__main__':
    keyboard.go()