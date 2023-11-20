# MediConnect (Hospital management system)
Team: Techno4

Members:
1. Piyush Raj
2. Gaurav Kumar
3. Priyanshu Raj
4. Praveen Kumar Dhusia

Project made under the guidance of Shri Gopal Krishna, Department of computer science and engineering

National Institute of Technology Patna 

## Introduction

Welcome to the Hospital Management System, MediConnect GitHub repository! This application, built using Django, is designed to streamline and enhance the operations of healthcare facilities. Whether you're a developer contributing to the project or a user exploring its features, this README provides a comprehensive guide to get you started.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)

## Features

- **Patient Management:** Efficiently record and manage patient information.
- **Appointment Scheduling:** Schedule and organize appointments seamlessly.
- **Staff Management:** Keep track of staff details, roles, and responsibilities.
- **Reports management:** Generate insightful reports for better decision-making.
- **AI based disease prediction:** AI based prediction tools to predict multiple diseases.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.x)
- Django
- MySQL server and workbench
- [Additional dependencies listed in requirements.txt]

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/hospital-management-system-django.git
    ```

2. **Install dependencies:**

    ```bash
    cd hospital-management-system-django
    pip install -r requirements.txt
    ```

3. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser account:**

    ```bash
    python manage.py createsuperuser
    ```

## Configuration

Configure the database settings, email configurations, and other settings in the `settings.py` file.

## Usage

To run the application, use:

```bash
python manage.py runserver
```

Visit http://localhost:8000 in your browser to access the Hospital Management System.

## Note

Not for commercial usage. Made as a college project with ❤️ and ☕.
