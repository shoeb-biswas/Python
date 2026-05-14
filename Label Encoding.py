# Label Encoding for binary categorical columns -> Sex and ExerciseAngina

le = LabelEncoder()
df_heart["Sex"] = le.fit_transform(df_heart["Sex"])
df_heart["ExerciseAngina"] = le.fit_transform(df_heart["ExerciseAngina"])
df_heart.head(10)
