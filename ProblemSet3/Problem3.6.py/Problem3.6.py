for beat in range(1,17):
    if beat == 1:
        sound = "B"
    elif beat % 4 == 3:
        sound = "K"
    elif beat % 4 == 2 and beat > 2:
        sound = "b"
    else:
        sound = "t"
    print (sound, end=" ")

print() #clean new line after the loop