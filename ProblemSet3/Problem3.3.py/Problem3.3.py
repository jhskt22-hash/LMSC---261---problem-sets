# Prompt user to enter the BPM
BPM = int(input("Enter BPM: "))
# Calculate ms
ms_per_beat = 60000 / BPM
# print both the original BPM value as well as the caculated MS per beat
print(f"a quarter note delay for {BPM} bpm is {ms_per_beat} milliseconds.")