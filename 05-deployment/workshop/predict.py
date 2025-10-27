import pickle

with open('model.bin','rb') as f_in:
   pipeline = pickle.load(f_in)

customer = {'gender': 'male',
 'seniorcitizen': 0,
 'partner': 'no',
 'dependents': 'yes',
 'phoneservice': 'no',
 'multiplelines': 'no_phone_service',
 'internetservice': 'dsl',
 'onlinesecurity': 'no',
 'onlinebackup': 'no',
 'deviceprotection': 'yes',
 'techsupport': 'no',
 'streamingtv': 'no',
 'streamingmovies': 'yes',
 'contract': 'month-to-month',
 'paperlessbilling': 'yes',
 'paymentmethod': 'electronic_check',
 'tenure': 6,
 'monthlycharges': 29.65,
 'totalcharges': 129.65}

churn = pipeline.predict_proba(customer)[0,1]
print(f'prob of churning = {churn}')
if churn >=0.5:
    print("send promo email")
else:
    print("don't do anything")