"""
print emojis
"""
print("enter your message")
message = input().split(" ")

emojis = {
    ":)": "😄",
    "(": "😕",
}

display = ""
for word in message:
    display = display + emojis.get(word, word) + " "

print(display)
