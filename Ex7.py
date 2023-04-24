#Train the Model
# Gitika Chouksey 0827CI201068
fromsklearn.linear_modelimportLogisticRegression
  
classifier =LogisticRegression(random_state=0)
classifier.fit(xtrain, ytrain)


#Evaluation Metrics

# Gitika Chouksey 0827CI201068
fromsklearn.metricsimportconfusion_matrix
  
cm =confusion_matrix(ytest, y_pred)
print("Confusion Matrix : \n", cm)
#Visualizing the performance of Model.

# Gitika Chouksey 0827CI201068
frommatplotlib.colorsimportListedColormap
  
X_set, y_set=xtest, ytest
X1, X2 =np.meshgrid(np.arange(start =X_set[:, 0].min() -1, 
                               stop =X_set[:, 0].max() +1, step =0.01),
                     np.arange(start =X_set[:, 1].min() -1, 
                               stop =X_set[:, 1].max() +1, step =0.01))
  
plt.contourf(X1, X2, classifier.predict(
             np.array([X1.ravel(), X2.ravel()]).T).reshape(
             X1.shape), alpha =0.75, cmap=ListedColormap(('red', 'green')))
  
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
  
fori, j inenumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j, 0], X_set[y_set==j, 1],
                c =ListedColormap(('red', 'green'))(i), label =j)
      
plt.title('Classifier (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

