import pickle

data = {
    'name': 'Alice',
    'age': 30,
    'is_admin': True
}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

print("Data saved.")

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print("Loaded data:", loaded_data)