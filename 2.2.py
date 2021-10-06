text_one = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
text_two = []

for i in text_one:
    if i.replace('+', "").isdigit():
        if i.isdigit():
            text_two.append(f'"{int(i):02}"')
        else:
            text_two.append(f"{i[0]}{int(i[1:]):02}")
    else:
        text_two.append(i)
print(text_two)
print(" ".join(text_two))