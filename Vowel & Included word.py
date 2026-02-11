# Start with Vowel
df.loc[df['Name'].str.contains(r"^[AEIOU]")]
# Include New or Los
df.loc[df['City'].str.contains(r"New|Los")]
