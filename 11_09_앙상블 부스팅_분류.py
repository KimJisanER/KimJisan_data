import warnings
warnings.filterwarnings("ignore")
import pandas as pd
data=pd.read_csv('breast-cancer-wisconsin.csv', encoding='utf-8')
X=data[data.columns[1:10]]
y=data[["Class"]]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X, y, stratify=y, random_state=42)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(X_train)
X_scaled_train=scaler.transform(X_train)
X_scaled_test=scaler.transform(X_test)

from sklearn.ensemble import AdaBoostClassifier
model=AdaBoostClassifier(n_estimators=100, random_state=0)
model.fit(X_scaled_train, y_train)
pred_train=model.predict(X_scaled_train)
print(model.score(X_scaled_train, y_train))

from sklearn.metrics import confusion_matrix
confusion_train=confusion_matrix(y_train, pred_train)
print("훈련데이터 오차행렬:\n", confusion_train)

from sklearn.metrics import classification_report
cfreport_train=classification_report(y_train, pred_train)
print("분류예측 레포트:\n", cfreport_train)

pred_test=model.predict(X_scaled_test)
print(model.score(X_scaled_test,y_test))

from sklearn.ensemble import GradientBoostingClassifier
model=GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=1, random_state=0)
model.fit(X_scaled_train,y_train)
pred_train=model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)

from sklearn.metrics import confusion_matrix
confusion_train=confusion_matrix(y_train, pred_train)
print("훈련데이터 오차행렬:\n", confusion_train)

pred_test=model.predict(X_scaled_test)
print(model.score(X_scaled_test, y_test))

confusion_test=confusion_matrix(y_test, pred_test)
print("테스트데이터 오차행렬: \n", confusion_test)
