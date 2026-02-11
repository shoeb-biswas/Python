df.loc[df['City'].str.contains("New")]
# To false down the case sensativeness
df.loc[df['City'].str.contains("new",case = False)]
