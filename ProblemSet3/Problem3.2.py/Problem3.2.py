# Prompt user for midi note between 0 and 127
midi_note = int(input("Enter a midi note between 0 and 127: "))
# Calculate frequency!
frequency = 440 * (2 **((midi_note - 69) / 12))
# print both the original midi number and the calculated frequency.
print(f"the frequency of the midi note number {midi_note} is {frequency} hz.")