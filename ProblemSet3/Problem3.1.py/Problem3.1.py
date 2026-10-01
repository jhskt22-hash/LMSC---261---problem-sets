# Ask user for total duration of the song in seconds
song_duration_in_seconds = int(input("Song duration in seconds"))

# Calculate minutes w/ integer division!
minutes = song_duration_in_seconds // 60

# Calculate remaining seconds using modulo operator
seconds = song_duration_in_seconds % 60

# Print the result.
print(f"{minutes} minutes and {seconds} seconds")