# Tune the hyperparameter with class_weight balanced
rfc = RandomForestClassifier(class_weight='balanced', random_state=42)

rfc_random = RandomizedSearchCV(estimator=rfc,
                                param_distributions=rfc_grid,
                                n_iter=50,
                                cv=5,
                                verbose=2,
                                random_state=42,
                                n_jobs=-1)

rfc_random.fit(X_train, y_train)

#Evaluate
rfc_balanced_score = rfc_random.score(X_test, y_test)

rfc_balanced_score