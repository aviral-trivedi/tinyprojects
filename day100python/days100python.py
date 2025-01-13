

def counter():
    with open("song.txt", "r") as file:
        song = file.read().split()

    checked = []
    most = {}

    for word in song:
        if word in checked:
            continue
        else:
            checked.append(word)
            most[word] = song.count(word)

    for key,value in most.items():
        temp = max(most.values())
        if most[key] == temp:
            print(key,value)



p= 6000000.141519


print(f"k {p:^,.2f} k")
