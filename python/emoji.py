"""
print emojis
"""


def display_msg():
    print("enter your message:\n")
    message = input().split(" ")

    emojis = {
        ":)": "😄",
        "(": "😕",
    }

    display = ""
    for word in message:
        display = display + emojis.get(word, word) + " "

    print(display)


display_msg()
