# Car Dealer

A full‑stack Django web application for browsing, managing, and displaying car listings. The project is designed with a modular structure, clean templates, and reusable Django apps, making it suitable for learning, portfolio use, or further extension into a production‑ready system.

---

## 🚗 Overview

Car Dealer provides a complete platform for showcasing vehicle inventory, managing inquiries, and handling user authentication. Built with Django’s MTV architecture, it emphasizes clean code organization, maintainability, and scalability.

---

## ✨ Features

* **Car Listings** – Add, update, delete, and display cars with details such as brand, model, mileage, price, year, transmission, and images.
* **User Authentication** – Secure login, logout, and registration using Django’s built‑in auth system.
* **Contact & Inquiry System** – Users can send inquiries directly from car detail pages.
* **Admin Dashboard** – Manage all site data through Django Admin.
* **Responsive Frontend** – Clean Bootstrap‑based UI built with Django templates.
* **SEO‑Friendly Pages** – Includes Home, About, Cars, and Contact pages.
* **Production Setup** – Includes `Procfile`, `runtime.txt`, and `requirements.txt` for deployment.

---

## 🛠 Technologies Used

### **Backend**

* Python
* Django Framework
* Django ORM
* MTV Architecture

### **Frontend**

* HTML5, CSS3
* Bootstrap
* Django Template Language (DTL)

### **Database**

* SQLite (development)
* JSON Data Fixtures

### **Deployment / DevOps**

* Gunicorn
* Heroku‑style configuration files
* Virtual environment management

---

## 📂 Project Structure

```
car_dealer/
│
├── cars/                 # Car listings app
├── pages/                # Static pages (Home, About, etc.)
├── accounts/             # User authentication app
├── contacts/             # Inquiry/contact app
│
├── car_dealer/           # Main project configuration
├── media/                # Uploaded images
├── env/                  # Virtual environment (ignored in Git)
├── project_dump.json     # Database dump / fixtures
│
├── requirements.txt      # Dependencies
├── Procfile              # Deployment process config
├── runtime.txt           # Python runtime version
└── manage.py             # Django management script
```

---

## 🚀 Getting Started

These instructions help you run the project locally.

### **1. Clone the Repository**

```
git clone https://github.com/yourusername/car_dealer.git
cd car_dealer
```

### **2. Create a Virtual Environment**

```
python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows
```

### **3. Install Dependencies**

```
pip install -r requirements.txt
```

### **4. Apply Migrations**

```
python manage.py migrate
```

### **5. Load Sample Data (Optional)**

```
python manage.py loaddata project_dump.json
```

### **6. Run the Server**

```
python manage.py runserver
```

Visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧪 Running Tests

(If tests are added later)

```
python manage.py test
```

---

## 📦 Deployment

This project includes configuration for platforms like Heroku.

* `Procfile` defines the web server (Gunicorn).
* `runtime.txt` sets the Python version.
* Add environment variables as needed.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Create a pull request

---

## 🖼️ Screenshots / Gallery

> Add your project screenshots to the `screenshots/` folder and link them here. Examples:

### **Home Page**

![Home Page](<img width="1866" height="841" alt="Screenshot 2025-12-11 120553" src="https://github.com/user-attachments/assets/c198afc7-72dd-46db-a042-ba05bd2703de" />
)

### **Car Listings**

![Car Listings](screenshots/cars.png)

### **Car Detail Page**

![Car Detail](screenshots/car_detail.png)


---

## 📬 Contact

If you have questions or suggestions, feel free to reach out or open an issue on GitHub.

---
# Car Dealer

A full‑stack Django web application for browsing, managing, and displaying car listings. The project is designed with a modular structure, clean templates, and reusable Django apps, making it suitable for learning, portfolio use, or further extension into a production‑ready system.

---

## 🚗 Overview

Car Dealer provides a complete platform for showcasing vehicle inventory, managing inquiries, and handling user authentication. Built with Django’s MTV architecture, it emphasizes clean code organization, maintainability, and scalability.

---

## ✨ Features

* **Car Listings** – Add, update, delete, and display cars with details such as brand, model, mileage, price, year, transmission, and images.
* **User Authentication** – Secure login, logout, and registration using Django’s built‑in auth system.
* **Contact & Inquiry System** – Users can send inquiries directly from car detail pages.
* **Admin Dashboard** – Manage all site data through Django Admin.
* **Responsive Frontend** – Clean Bootstrap‑based UI built with Django templates.
* **SEO‑Friendly Pages** – Includes Home, About, Cars, and Contact pages.
* **Production Setup** – Includes `Procfile`, `runtime.txt`, and `requirements.txt` for deployment.

---

## 🛠 Technologies Used

### **Backend**

* Python
* Django Framework
* Django ORM
* MTV Architecture

### **Frontend**

* HTML5, CSS3
* Bootstrap
* Django Template Language (DTL)

### **Database**

* SQLite (development)
* JSON Data Fixtures

### **Deployment / DevOps**

* Gunicorn
* Heroku‑style configuration files
* Virtual environment management

---

## 📂 Project Structure

```
car_dealer/
│
├── cars/                 # Car listings app
├── pages/                # Static pages (Home, About, etc.)
├── accounts/             # User authentication app
├── contacts/             # Inquiry/contact app
│
├── car_dealer/           # Main project configuration
├── media/                # Uploaded images
├── env/                  # Virtual environment (ignored in Git)
├── project_dump.json     # Database dump / fixtures
│
├── requirements.txt      # Dependencies
├── Procfile              # Deployment process config
├── runtime.txt           # Python runtime version
└── manage.py             # Django management script
```

---

## 🚀 Getting Started

These instructions help you run the project locally.

### **1. Clone the Repository**

```
git clone https://github.com/yourusername/car_dealer.git
cd car_dealer
```

### **2. Create a Virtual Environment**

```
python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows
```

### **3. Install Dependencies**

```
pip install -r requirements.txt
```

### **4. Apply Migrations**

```
python manage.py migrate
```

### **5. Load Sample Data (Optional)**

```
python manage.py loaddata project_dump.json
```

### **6. Run the Server**

```
python manage.py runserver
```

Visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧪 Running Tests

(If tests are added later)

```
python manage.py test
```

---

## 📦 Deployment

This project includes configuration for platforms like Heroku.

* `Procfile` defines the web server (Gunicorn).
* `runtime.txt` sets the Python version.
* Add environment variables as needed.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Create a pull request

---

## 🖼️ Screenshots / Gallery

> Add your project screenshots to the `screenshots/` folder and link them here. Examples:

### **Home Page**

![Home Page](screenshots/home.png)

### **Car Listings**

![Car Listings](screenshots/cars.png)

### **Car Detail Page**

![Car Detail](screenshots/car_detail.png)


---

## 📬 Contact

If you have questions or suggestions, feel free to reach out or open an issue on GitHub.

---
