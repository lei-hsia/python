
# implement SVM

# import library
from sklearn import svm 
# assume you have X(predictor) and Y(target) for training data set
# and test(predictor) of test_dataset

# create svm classification object
model = svm.svc(kernel='linear',c=1, gamma=1)

model.fit(X, y)
model.score(X,y)

# predict output for test set
predicted = model.predict(x_test)

