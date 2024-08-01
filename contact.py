from flask import Flask, render_template, request, redirect, url_for
import pickle
import os

app = Flask(__name__)

# File to store contact data
DATA_FILE = "contacts.pkl"

# Load contacts from file
def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as file:
            return pickle.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(DATA_FILE, "wb") as file:
        pickle.dump(contacts, file)

# Initialize contacts
contacts = load_contacts()

@app.route('/')
def index():
    return render_template('contact_book.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    
    if name and phone:
        contacts[name] = phone
        save_contacts(contacts)
    return redirect(url_for('index'))

@app.route('/delete/<name>', methods=['POST'])
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search_contact():
    query = request.form.get('query').lower()
    filtered_contacts = {name: phone for name, phone in contacts.items() if query in name.lower() or query in phone}
    return render_template('contact_book.html', contacts=filtered_contacts)

if __name__ == '__main__':
    app.run(debug=True)
