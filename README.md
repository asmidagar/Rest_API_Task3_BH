# Flask REST API – User Management (In-Memory)

This project is a simple REST API built using **Flask** that performs basic CRUD operations to manage user data. It uses an **in-memory dictionary** to store user records, fulfilling the requirement of not using a database. Ideal for learning how RESTful APIs work with Flask.

---

## 🚀 Features

- `GET /api/users/` – Fetch all users  
- `GET /api/users/<id>` – Fetch a specific user by ID  
- `POST /api/users/` – Add a new user  
- `PATCH /api/users/<id>` – Update an existing user's name and/or email  
- `DELETE /api/users/<id>` – Delete a user  

---

## 🛠 Tech Stack

- Python 3.x  
- Flask  
- curl or Postman (for API testing)

---

## 📁 Project Structure

```
.
├── .gitignore
├── api.py              # Main Flask application
├── requirements.txt    # Dependencies
└── .venv/              # Virtual environment (not pushed to GitHub)
```

---

## 🔧 Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/flask-rest-api-task.git
cd flask-rest-api-task
```

2. **Create and activate virtual environment (optional but recommended):**

```bash
python -m venv .venv
source .venv/bin/activate     # On macOS/Linux
.venv\Scripts\activate        # On Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app:**

```bash
python api.py
```

5. **Test the API using Postman or curl.**

---

## 🧪 Example curl Commands

**Create a user:**
```bash
curl -X POST http://127.0.0.1:5000/api/users/ -H "Content-Type: application/json" -d '{"name":"Asmi Dagar","email":"asmi@example.com"}'
```

**Get all users:**
```bash
curl http://127.0.0.1:5000/api/users/
```

**Get a user by ID:**
```bash
curl http://127.0.0.1:5000/api/users/1
```

**Update a user:**
```bash
curl -X PATCH http://127.0.0.1:5000/api/users/1 -H "Content-Type: application/json" -d '{"name":"Asmi Updated","email":"updated@example.com"}'
```

**Delete a user:**
```bash
curl -X DELETE http://127.0.0.1:5000/api/users/1
```

---

## 📝 Notes

- Data is **not persistent** — restarting the server resets all users.
- Meant for **learning and development purposes only**, not production.

---

## 📚 Outcome

- Learned how to build a REST API using Flask
- Understood CRUD operations
- Gained experience in using in-memory data structures and testing with tools like curl/Postman

---

## Author

- Asmi Dagar(Python Intern at Broskies Hub)

---

## Snapshots 

<img width="1920" height="1020" alt="Screenshot 2025-07-21 130001" src="https://github.com/user-attachments/assets/1fa6266d-2bd6-4cc2-a696-b5dc9ba4c801" />

<img width="1920" height="1020" alt="Screenshot 2025-07-21 130202" src="https://github.com/user-attachments/assets/526f405a-cde1-46ab-b854-f3f39b84ab0a" />

<img width="1920" height="1020" alt="Screenshot 2025-07-21 130346" src="https://github.com/user-attachments/assets/cbb29906-0c3d-4701-b20c-50035e1a69ef" />

---

## 🔗 License

This project is open-source and available under the [MIT License](LICENSE).
