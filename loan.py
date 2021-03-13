import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, confusion_matrix

data = pd.read_csv('lending_club_loan_two.csv')
data = data.iloc[:1000]

data['term'] = data['term'].apply(lambda x: float(x[:3]))

dummy_data_1 = pd.get_dummies(data['grade'], drop_first=True)  # add this to data
dummy_data_2 = pd.get_dummies(data['sub_grade'], drop_first=True)  # add this to data
dummy_data_3 = pd.get_dummies(data['verification_status'], drop_first=True)  # add this to data
dummy_data_5 = pd.get_dummies(data['loan_status'], drop_first=True)  # add this to data
dummy_data_6 = pd.get_dummies(data['purpose'], drop_first=True)  # add this to data
dummy_data_7 = pd.get_dummies(data['initial_list_status'], drop_first=True)  # add this to data


def checknum(num):
    if type(num) != str:
        return None
    temp = []
    for i in list(num):
        if i.isdigit():
            temp.append(i)
    return float("".join(temp))


def check_ownership(value):
    if value == 'NONE':
        return 'OTHER'
    else:
        return value


def year_issued(date):
    return float(date[-4:])


data['emp_length'] = data['emp_length'].apply(checknum)
data['home_ownership'] = data['home_ownership'].apply(check_ownership)
dummy_data_4 = pd.get_dummies(data['home_ownership'], drop_first=True)  # add this to data
data['emp_length'] = data['emp_length'].fillna(data['emp_length'].mean())
data['issue_d'] = data['issue_d'].apply(year_issued)
data['earliest_cr_line'] = data['earliest_cr_line'].apply(year_issued)
data['mort_acc'] = data['mort_acc'].fillna(data['mort_acc'].mean())
data['address'] = data['address'].apply(lambda x : float(x[-5:]))
# dummy_data_8 = pd.get_dummies(data['address'], drop_first=True)  # add this to data


data.drop(['grade', 'sub_grade', 'emp_title', 'emp_length', 'home_ownership', 'verification_status',
           'issue_d', 'initial_list_status', 'application_type',
           'loan_status', 'purpose', 'title', 'address'], axis=1, inplace=True)

data.dropna(inplace=True)

data = pd.concat([data, dummy_data_1, dummy_data_2, dummy_data_3, dummy_data_4,
                  dummy_data_5, dummy_data_6, dummy_data_7], axis=1)

# print(data.to_string())

data.dropna(inplace=True)

sns.countplot(data['Fully Paid'])
plt.show()

scaler = MinMaxScaler()

# X = scaler.fit_transform(data.drop('Fully Paid', axis=1))
y = data['Fully Paid'].values

X = data.drop('Fully Paid', axis=1).values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = Sequential()

model.add(Dense(81,  activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(39, activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(19, activation='relu'))
model.add(Dropout(0.2))

# output layer
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam')

early_stopping = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=80)

model.fit(x=X_train,
          y=y_train,
          epochs=1000,
          batch_size=256,
          validation_data=(X_test, y_test),
          callbacks=[early_stopping]
          )

model.save('full_data_project_model.h5')

# predictions = model.predict_classes(X_test)
# predictions = (model.predict(X_test) > 0.5).astype("int32")

print(classification_report(y_test, predictions))