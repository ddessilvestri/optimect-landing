# Optimec Landing Page Project

This is a real-world landing page project for Optimec SRL, a company that specializes in CNC machining. The project includes:

- A frontend landing page with a contact form
- A Flask backend API to receive and store contact data
- PostgreSQL database
- File upload support (PDF, DOC, XLSX)

---

## 🖥 Run Locally (macOS)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/optimec-landing.git
cd optimec-landing
```

### 2. Set Up Python Environment

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Install and Start PostgreSQL

```bash
brew install postgresql@17
brew services start postgresql@17
export PATH="/opt/homebrew/opt/postgresql@17/bin:$PATH"
echo 'export PATH="/opt/homebrew/opt/postgresql@17/bin:$PATH"' >> ~/.zshrc
```

### 4. Create Database and Table

```bash
createdb optimec
psql -U postgres -d optimec -f ../db/init.sql
```

### 5. Run Flask App

```bash
python app.py
```

Visit the frontend form in `frontend/index.html`, fill it out, and submit to test.

---

## ☁️ Deploy to AWS EC2 (Ubuntu)

### 1. Launch EC2 Instance

- Choose Ubuntu 24.04
- Instance type: t2.micro (free tier eligible)
- Architecture: x86
- Assign public IP
- Open ports 22 (SSH), 80 (HTTP), 443 (HTTPS)

### 2. Connect to the EC2

```bash
ssh -i /path/to/key.pem ubuntu@your-ec2-public-ip
```

### 3. Set Up the Environment

```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx postgresql postgresql-contrib
```

### 4. Clone and Set Up the Project

```bash
git clone https://github.com/yourusername/optimec-landing.git
cd optimec-landing/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Set Up PostgreSQL on EC2

```bash
sudo -u postgres psql
CREATE DATABASE optimec;
\q
psql -U postgres -d optimec -f ../db/init.sql
```

### 6. Configure NGINX (optional)

Point NGINX to serve your Flask app using `gunicorn` or `uwsgi`. Enable SSL later using Certbot and Let's Encrypt.

---

## 🔜 Next Steps

- Create a Docker setup for consistent deployment
- Add Jenkins integration for CI/CD
- Secure NGINX with SSL (HTTPS)
- Use a real domain (e.g. from NIC.ar or AWS Route 53)
- Connect PostgreSQL via VPN or private networking for external access

---

## 📂 Project Structure

```
optimec-landing/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── uploads/
├── db/
│   └── init.sql
├── frontend/
│   └── index.html
```
