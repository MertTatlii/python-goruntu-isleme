import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics

# Veriyi yükleme ve ön işleme
data = pd.read_csv("C:\\Users\\90544\\Desktop\\3.2\\Sayısal Görüntü İşleme\\python-goruntu\\python-goruntu\\mushrooms.csv")
print(data)
mappings = list()
encoder = LabelEncoder()

for column in range(len(data.columns)):
    data[data.columns[column]] = encoder.fit_transform(data[data.columns[column]])
    mappings_dict = {index: label for index, label in enumerate(encoder.classes_)}
    mappings.append(mappings_dict)

y = data['class'] #asdklsadkjlsdkfjkldfkdfgfıtı fıtı
X = data.drop('class', axis=1)
print(X)
scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=0)

dtree = tree.DecisionTreeClassifier(criterion='entropy', random_state=0)
dtree.fit(x_train, y_train)

from sklearn.tree import plot_tree
# Karar ağacını görselleştirme
plt.figure(figsize=(23,30))
plot_tree(dtree, filled=True, feature_names=X.columns, class_names=['edible', 'poisonous'], rounded=True)
plt.show()

# Print the training metrics
print("Train accuracy:", metrics.accuracy_score(y_train, dtree.predict(x_train)))
print("Train confusion matrix:\n", metrics.confusion_matrix(y_train, dtree.predict(x_train)))
print("Train classification report:\n", metrics.classification_report(y_train, dtree.predict(x_train)))

# Print the testing metrics
print("Test accuracy:", metrics.accuracy_score(y_test, dtree.predict(x_test)))
print("Test confusion matrix:\n", metrics.confusion_matrix(y_test, dtree.predict(x_test)))
print("Test classification report:\n", metrics.classification_report(y_test, dtree.predict(x_test)))