# E-Commerce Backend

Welcome to the **E-Commerce Backend** project! This is a robust and scalable backend system built with **Django** and **Django REST Framework** to support an e-commerce platform. It includes features for user authentication, product catalog management, order processing, and more.

![E-Commerce Backend](https://img.freepik.com/free-photo/shopping-concept-close-up-portrait-young-beautiful-attractive-redhair-girl-smiling-looking-camera_1258-119090.jpg?t=st=1744315927~exp=1744319527~hmac=bd887274e772e49f82a21f91ce7e37dbd373bce3b7156d86ee65f02d7cd407f5&w=1380)

---

## 🛠️ Features

- **User Authentication**: Secure user registration, login, and JWT-based authentication.
- **Product Catalog Management**: CRUD operations for products and categories.
- **Order Management**: Place orders, manage order items, and handle user-specific orders.
- **Token-Based Authentication**: Access control using JWT (JSON Web Tokens).
- **API-First Design**: Fully RESTful API design for seamless integration.

---

## 🏗️ Technologies Used

| Technology             | Purpose                                |
|-------------------------|----------------------------------------|
| **Django**             | Backend framework                     |
| **Django REST Framework** | API development                     |
| **Simple JWT**         | Authentication and token management   |
| **SQLite**             | Default database (can be replaced)    |
| **Postman**            | API testing and debugging             |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:
- **Python 3.10+**
- **pip** (Python package manager)
- **virtualenv** (Optional but recommended)

---

### Local Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ecommerce-backend.git
   cd ecommerce-backend
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   - Open your browser and navigate to: `http://127.0.0.1:8000`

---

### Folder Structure

```
ecommerce_backend/
├── ecommerce_backend/    # Main project folder
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL configuration
├── users/                # User authentication app
│   ├── models.py         # Custom User model
│   ├── serializers.py    # User-related serializers
│   ├── views.py          # User views and authentication
├── products/             # Product management app
│   ├── models.py         # Product and Category models
│   ├── serializers.py    # Product-related serializers
│   ├── views.py          # Product views
├── orders/               # Order management app
│   ├── models.py         # Order and OrderItem models
│   ├── serializers.py    # Order-related serializers
│   ├── views.py          # Order views
└── requirements.txt      # Project dependencies
```

---

## 🔑 API Documentation

### User Authentication

| Endpoint                    | Method | Description                     |
|-----------------------------|--------|---------------------------------|
| `/api/users/register/`      | POST   | Register a new user             |
| `/api/users/login/`         | POST   | Log in and receive JWT tokens   |
| `/api/users/token/refresh/` | POST   | Refresh access token            |

---

### Product Management

| Endpoint                     | Method | Description                     |
|------------------------------|--------|---------------------------------|
| `/api/products/categories/`  | GET    | List all categories             |
| `/api/products/categories/`  | POST   | Create a new category           |
| `/api/products/products/`    | GET    | List all products               |
| `/api/products/products/`    | POST   | Create a new product            |

---

### Order Management

| Endpoint                       | Method | Description                     |
|--------------------------------|--------|---------------------------------|
| `/api/orders/orders/`          | GET    | List all orders for a user      |
| `/api/orders/orders/`          | POST   | Create a new order              |
| `/api/orders/orders/<id>/`     | GET    | Retrieve order details          |
| `/api/orders/orders/<id>/`     | PUT    | Update an order                 |
| `/api/orders/orders/<id>/`     | DELETE | Delete an order                 |
| `/api/orders/orders/<id>/items/` | POST | Add an item to an order         |

---

## 🧪 Testing

1. **Run Tests**
   ```bash
   python manage.py test
   ```

2. **Test API Endpoints**
   - Use **Postman** or **cURL** to test the API endpoints.
   - Example cURL command to create a product:
     ```bash
     curl -X POST http://127.0.0.1:8000/api/products/products/ \
     -H "Content-Type: application/json" \
     -d '{
         "name": "Smartphone",
         "description": "A high-end smartphone",
         "price": 699.99,
         "stock": 50,
         "category": 1
     }'
     ```

---

## 📂 Deployment

### Deploy to Heroku (Optional)

1. **Install Heroku CLI**:
   ```bash
   brew tap heroku/brew && brew install heroku
   ```

2. **Login to Heroku**:
   ```bash
   heroku login
   ```

3. **Create a Heroku App**:
   ```bash
   heroku create ecommerce-backend
   ```

4. **Deploy the Project**:
   ```bash
   git push heroku main
   ```

5. **Access the Live App**:
   ```bash
   heroku open
   ```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Commit your changes and push to your fork.
4. Open a Pull Request describing your changes.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

Special thanks to:
- Django and Django REST Framework teams for providing excellent tools.
- The open-source community for inspiration and support.

---

### 📧 Contact

For questions or feedback, feel free to reach out:
- **Email**: nallapaneni.niklesh@gmail.com
- **GitHub**: [nikleshclark](https://github.com/nikleshclark)

---