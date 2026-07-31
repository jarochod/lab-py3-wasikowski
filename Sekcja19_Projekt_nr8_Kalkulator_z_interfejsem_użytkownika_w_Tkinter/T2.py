
calc_keyboard = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", "Clear", "=", "/"]
    ]


print('--------')
for row, row_items in enumerate(calc_keyboard):
    for col, char in enumerate(row_items):
        print(char, row, col)

print('--------')
for rom_items in calc_keyboard:
    for item in rom_items:
        print(item, calc_keyboard.index(rom_items), rom_items.index(item))







