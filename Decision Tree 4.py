# Predicted probabilities
y_proba_h = tree_heart.predict_proba(x_test_h)[:,1]
y_proba_h[:10]

# ROC curve and AUC
fpr, tpr, thresholds = roc_curve(y_test_h, y_proba_h)
roc_auc = auc(fpr,tpr)
print('AUC: ', round(roc_auc,3))

# Plot
plt.figure()
plt.plot(fpr,tpr, label = f'ROC curve (AUC = {roc_auc: .3f})')
plt.plot([0,1], [0,1],linestyle ='--', label= 'Random model')
plt.xlabel('False Positive Rate (fpr)')
plt.ylabel('True Positive Rate (tpr)')
plt.title("Roc Curve")
plt.legend()
plt.show()
