import numpy as np
# 1. Remove outliers
df_no_outliers = [(df_heart_encoded[col] >=lower) & (df_heart_encoded[col] <=upper)]
print(len(df_no_outliers))

# 2. Cap outliers
df_capped = df_heart_encoded.copy()
df_capped[col] = df_capped[col].clip(lower,upper)

print(df_capped)

# Log tranformation the column (for skewed distribution)
df_log = df_heart_encoded.copy()
df_log[col+"_log"] = np.log(df_log[col]+1)

print(df_log)
