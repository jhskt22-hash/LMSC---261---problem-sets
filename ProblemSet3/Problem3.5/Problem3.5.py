# Prompt user for BPM and song duration inputs
bpm = float(input("Enter the BPM of the song:"))
duration = int(input("Enter the duration of the song in seconds"))
# Calculate beats per second
beats_per_sec = bpm / 60
# While loop statement, tracking beats by second
second = 1 
while second <= duration:
    total_beats = second * beats_per_sec
    print(f"at second {second}, total beats:{total_beats}")
    second += 1