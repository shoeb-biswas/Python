# Start with los [print all Los]
df.loc[df['City'].str.contains(r"Los")]
# Print just start with Los
df.loc[df['City'].str.contains(r"^Los")]
