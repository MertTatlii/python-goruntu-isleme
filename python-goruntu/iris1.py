import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import metrics
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Load the dataset
iris = datasets.load_iris()
x = iris.data
y = iris.target

# Standardize the data
ss = StandardScaler()
ss.fit(x)
x = ss.transform(x)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Train the decision tree classifier
dtree = tree.DecisionTreeClassifier(criterion='entropy', random_state=0)
dtree.fit(x_train, y_train)

# Print the training metrics
print("Train accuracy:", metrics.accuracy_score(y_train, dtree.predict(x_train)))
print("Train confusion matrix:\n", metrics.confusion_matrix(y_train, dtree.predict(x_train)))
print("Train classification report:\n", metrics.classification_report(y_train, dtree.predict(x_train)))

# Print the testing metrics
print("Test accuracy:", metrics.accuracy_score(y_test, dtree.predict(x_test)))
print("Test confusion matrix:\n", metrics.confusion_matrix(y_test, dtree.predict(x_test)))
print("Test classification report:\n", metrics.classification_report(y_test, dtree.predict(x_test)))

# Import necessary libraries for visualization
import graphviz
from sklearn.tree import plot_tree

# Visualize the decision tree using matplotlib
plt.figure(figsize=(20,10))
plot_tree(dtree, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, rounded=True)
plt.show()
