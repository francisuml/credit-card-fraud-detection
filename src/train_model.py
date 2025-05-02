

# Create a model in a dictionary
models = {
    'Logistic Regression': LogisticRegression(max_iter=10000),
    'KNN': KNeighborsClassifier(),
    'RandomForestClassifier': RandomForestClassifier(),
    'Naive Bayes': GaussianNB(),
    'LinearSVC' : LinearSVC(max_iter=10000)
}

#Create a function to fit and score models
def fit_and_score(models, X_train, X_test, y_train, y_test):
    """
    Fits and evaluate given machine learning mdoels
    """

    #Set random seed
    np.random.seed(42)

    model_scores = {}

    for names, model in models.items():
        model.fit(X_train, y_train)
        model_scores[names] = model.score(X_test, y_test)
    return model_scores

#Evaluate the model
model_scores = fit_and_score(models=models,
                             X_train=X_train,
                             X_test=X_test,
                             y_train=y_train,
                             y_test=y_test)
model_scores