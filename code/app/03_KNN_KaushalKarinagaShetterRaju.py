from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=5,metric = 'minkowski',p = 2).fit(x_train,y_train)

y_hat = neigh.predict(x_test)

from sklearn import metrics
metrics.accuracy_score(y_test,y_hat)

fpr1, tpr1, _ = metrics.roc_curve(y_test,  y_hat)

#create ROC curve
plt.plot(fpr1,tpr1)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

#define metrics

fpr1, tpr1, _ = metrics.roc_curve(y_test, y_hat)
auc = metrics.roc_auc_score(y_test, y_hat)

#create ROC curve
plt.plot(fpr1,tpr1,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()

# selcting the best k value
Ks=30
mean_acc = np.zeros((Ks-1))
std_acc = np.zeros((Ks-1))

for n in range(1,Ks):
    neigh = KNeighborsClassifier(n_neighbors = n).fit(x_train,y_train)
    y_hat = neigh.predict(x_test)
    mean_acc[n-1] = metrics.accuracy_score(y_test,y_hat)
    std_acc[n-1] = np.std(y_hat==y_test)/np.sqrt(y_hat.shape[0])
    
mean_acc

plt.plot(range(1,Ks),mean_acc,'g',marker='o')
plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
plt.legend(('Accuracy ', '+/- 3xstd'))
plt.ylabel('Accuracy ')
plt.xlabel('Number of Neighbours (K)')
plt.tight_layout()
plt.show()

neigh = KNeighborsClassifier(n_neighbors=20).fit(x_train,y_train)
y_hat = neigh.predict(x_test)
metrics.accuracy_score(y_test,y_hat)

print(classification_report(y_test, y_hat))

from sklearn.metrics import plot_confusion_matrix, confusion_matrix
confusion_matrix(y_test, y_hat)

plot_confusion_matrix(neigh,x_test,y_test)