# 🔐 Flask Supabase Authentication System
A secure authentication system built using **Flask**, **Supabase Auth**, and **session-based login management**.
This project provides a modern login, signup, and password reset UI integrated with Supabase backend authentication.
---
## 🚀 Features
* User Login & Signup system
* Password reset functionality
* Session-based authentication (Flask session)
* Supabase authentication integration
* Secure token verification
* Clean and modern UI (HTML/CSS/JS)
* Logout functionality
* API-based backend structure
---
## 🛠️ Tech Stack
* Python
* Flask
* Supabase (Auth Service)
* HTML5
* CSS3
* JavaScript
* dotenv (Environment Variables)
---
## 📁 Project Structure
```text id="authproj1"
|-- screenshots/
|-- src/
|   |-- db.py
|-- templates/
|   |-- login.html
|   |-- login.css
|   |-- login.js
|-- .env
|-- .gitignore
|-- .env.example
|-- app.py
|-- requirements.txt
|-- README.md
```
---
## ⚙️ Environment Variables
Create a `.env` file in the root directory and add:
```env id="env1"
SUPABASE_URL="your_supabase_project_url"
SUPABASE_KEY="your_supabase_anon_or_service_key"
SECRET_KEY="your_flask_secret_key"
```
---
## 📦 Installation
### 1. Clone the Repository
```bash id="install1"
git clone https://github.com/your-username/flask-supabase-auth.git
cd flask-supabase-auth
```
---
### 2. Create Virtual Environment
```bash id="install2"
python -m venv venv
```
Activate it:
#### Windows
```bash id="install3"
venv\Scripts\activate
```
#### Linux / Mac
```bash id="install4"
source venv/bin/activate
```
---
### 3. Install Dependencies
```bash id="install5"
pip install -r requirements.txt
```
---
## ▶️ Run the Project
```bash id="run1"
python app.py
```
The server will start at:
```
http://127.0.0.1:5000
```
---
## 🔐 Authentication Flow
### 1. Login / Signup
* User enters credentials in frontend form
* Supabase handles authentication securely
### 2. Session Creation
* After login, frontend sends access token to:
```
POST /set-session
```
* Backend verifies token using Supabase
* Flask session is created with user ID
### 3. Get Current User
```
GET /me
```
Returns logged-in user ID from session.
### 4. Logout
```
GET /logout
```
Clears session.
---
## 📡 API Endpoints
| Endpoint       | Method | Description                 |
| -------------- | ------ | --------------------------- |
| `/`            | GET    | Health check                |
| `/set-session` | POST   | Create session after login  |
| `/me`          | GET    | Get current logged-in user  |
| `/logout`      | GET    | Logout user (clear session) |
---
## 🧠 How It Works
1. User logs in via Supabase Auth (frontend)
2. Supabase returns `access_token`
3. Token is sent to Flask backend
4. Backend verifies token using Supabase SDK
5. Flask session stores user ID
6. Session is used for authentication in future requests
---
## 🔒 Security Features
* Environment variables for sensitive keys
* Supabase token verification
* Flask session management
* Secure authentication flow
* No password stored in backend
---
## 🎨 UI Overview
* Modern login/signup UI
* Smooth form switching (Login / Signup / Forgot Password)
* Responsive design
* Clean user experience
---
## 📸 Screenshots
(Add your screenshots inside `/screenshots` folder)
Example:
* Login Page
* Signup Page
* Password Reset Page
---
## 🚀 Future Improvements
* JWT-based authentication (optional upgrade)
* Google OAuth login
* User profile dashboard
* Database user table integration
* Email verification system
* Role-based access control (Admin/User)
---
## 👨‍💻 Author
**Abaid-ur-Rehman**
Python & Machine Learning Developer
Focused on AI, Flask, and Backend Development
---
## 📜 License
This project is open-source and available under the MIT License.
