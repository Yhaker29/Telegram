from enum import StrEnum


class Style(StrEnum):
    success='success'
    primary='primary'
    danger='danger'

class Buttons(StrEnum):
    hello = "привіт"
    goodbye = "пока"
    roblox="Roblox🔲"
#
admin_buttons= {
    Buttons.hello.value: Style.success,
    Buttons.goodbye.value: Style.danger,
    Buttons.roblox: None
}

