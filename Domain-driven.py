# Domain-driven risk categories for RestingBP and Oldpeak

def bp_risk(bp):
    if bp < 120:
        return "Normal"
    elif bp < 140:
        return "Elevated"
    else:
        return "High"

def oldpeak(op):
    if op == 0:
        return "No Stress"
    elif op < 2:
        return "Moderate Stress"
    else:
        return "High Stress"

df_heart_encoded["BP_Risk"] = df_heart_encoded["RestingBP"].apply(bp_risk)

df_heart_encoded["Oldpeak_Risk"] = df_heart_encoded["Oldpeak"].apply(oldpeak)

df_heart_encoded[["RestingBP", "BP_Risk", "Oldpeak", "Oldpeak_Risk"]]
