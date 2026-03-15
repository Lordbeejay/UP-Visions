import os
path = r"c:\Users\josaiah\Desktop\TAPOSON 1 week\UP-Visions\game\script.rpy"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

to_remove = """    if _action == \"phone\":
        call phone_check

    if _action == \"inventory\":
        if inventory_unlocked:
            call screen inventory_screen()

"""
text = text.replace(to_remove, "")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("Updated script.rpy")
