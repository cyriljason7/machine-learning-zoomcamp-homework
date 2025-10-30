import requests

url = 'http://localhost:9696/prediction'

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

response = requests.post(url, json=customer)
churn = response.json()

print(f'prob of churning = {churn}')
if churn['churn_probability'] >=0.5:
    print("send promo email")
else:
    print("don't do anything")

