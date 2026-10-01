# prompt user for the song duration
duration = float(input("Enter the song duration in minutes:"))
# define song lengths using the inputted song duration
if duration < 2:
    print("this song is short!")
elif duration <= 4:
    print("this song is not long or short")
else:
    print("this song is long!")