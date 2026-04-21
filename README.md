# Cars Dealership - Full Stack Capstone Project

## Project Name: Cars Dealership Web Application

A full-stack web application for **Cars Dealership**, a national car retailer in the U.S. This application allows users to:
- Browse dealership branches across the United States
- View customer reviews for specific dealerships
- Submit reviews for dealerships (when logged in)
- Analyze sentiment of reviews using IBM Watson NLP

## Tech Stack

### Frontend
- **React.js** - Component-based UI framework
- **HTML5 / CSS3** - Responsive static pages
- **Bootstrap** - Styling and responsive layout

### Backend
- **Django** - Main web framework (Python)
- **Django REST Framework** - RESTful API endpoints
- **SQLite** - Primary database for car makes/models and user data

### Microservices
- **Node.js + Express + MongoDB** - Dealer and Review microservice
- **Flask + IBM Watson NLP** - Sentiment analysis microservice

### DevOps & Deployment
- **Docker** - Containerization of all services
- **Docker Compose** - Local multi-container orchestration
- **Kubernetes** - Container orchestration (IBM Cloud)
- **IBM Cloud Code Engine** - Serverless deployment
- **GitHub Actions** - CI/CD pipeline

## Project Structure

```
xrwvm-fullstack_developer_capstone/
├── server/                          # Django backend
│   ├── djangoapp/                   # Main Django app
│   │   ├── models.py                # CarMake, CarModel models
│   │   ├── views.py                 # All view functions
│   │   ├── urls.py                  # URL routing
│   │   └── restapis.py              # External API calls
│   ├── frontend/                    # React frontend
│   │   ├── src/
│   │   │   └── components/
│   │   │       ├── Register/        # User registration
│   │   │       ├── Login/           # User login
│   │   │       ├── Dealers/         # Dealer listing
│   │   │       └── Dealer/          # Dealer detail & reviews
│   │   └── static/                  # Static HTML pages
│   │       ├── About.html
│   │       └── Contact.html
│   └── database/                    # SQLite database files
├── functions/                       # IBM Cloud Functions
│   └── sentiment-analyzer/          # Flask sentiment service
└── .github/
    └── workflows/                   # GitHub Actions CI/CD
```

## Features

1. **Dealer Listings** - View all dealerships with state filtering
2. **Dealer Reviews** - Read reviews with sentiment analysis badges
3. **User Authentication** - Register, Login, Logout
4. **Review Submission** - Authenticated users can post reviews
5. **Sentiment Analysis** - Automatic review sentiment scoring
6. **Admin Panel** - Django admin for managing car inventory

## Installation & Setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- MongoDB
- Docker & Docker Compose

### Local Development

```bash
# Clone the repository
git clone https://github.com/bilgehankiso/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone

# Install Python dependencies
pip install -r requirements.txt

# Run Django server
cd server
python manage.py migrate
python manage.py runserver

# In another terminal, run Node.js microservice
cd server/database
node app.js

# In another terminal, run sentiment analyzer
cd functions/sentiment-analyzer
pip install -r requirements.txt
python app.py
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/djangoapp/get_dealers` | GET | Get all dealers |
| `/djangoapp/get_dealers/{state}` | GET | Get dealers by state |
| `/djangoapp/dealer/{id}` | GET | Get dealer by ID |
| `/djangoapp/reviews/dealer/{id}` | GET | Get dealer reviews |
| `/djangoapp/add_review` | POST | Submit a review |
| `/djangoapp/login` | POST | User login |
| `/djangoapp/logout` | GET | User logout |
| `/djangoapp/register` | POST | User registration |
| `/djangoapp/get_cars` | GET | Get all car makes/models |

## Deployment

The application is deployed on **IBM Cloud Code Engine**:
- **Frontend + Django**: https://cars-dealership.example.com
- **Node.js Microservice**: Internal service
- **Sentiment Analyzer**: Internal service

## Author

**Bilgehan Kışo**  
Full-Stack Developer  
IBM Full-Stack Development Professional Certificate - Capstone Project

## License

This project is licensed under the Apache 2.0 License.
