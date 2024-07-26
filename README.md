# Food Delivery App using Django

This project is a food delivery web application built with Django, MySQL, and Bootstrap. It allows customers to browse restaurants, place orders, and track their status. Delivery boys can view assigned orders and update their status, while restaurants can manage their menus and incoming orders.

### Technologies Used

- Python
- Django
- MySQL
- Bootstrap
- bdbootstrap
  
### Features
- User authentication (login, signup) for customers, delivery boys, and restaurants.
- Separate interfaces for customers, delivery boys, and restaurants.
- Order placement and tracking with real-time updates.
- Responsive design using Bootstrap for a seamless experience across devices.

  
## Development Setup

To set up backend codebase for development follow these steps:


1.Clone the project.

```bash
  https://github.com/jojijose101/EatRoot.git
```

2.Go to the project directory

```bash
  cd EatRoot
```
3.Create Virtual envirolment for python3.10
   
   ```bash
      mkvirtualenv venv usr/bin/python3.10
   ```

4. Install dependencies

```bash
   pip install Django
   pip install pymysql
   pip install pillow

```
- **User Interfaces:**
  - **Customer Interface:** Allows browsing restaurants, placing orders, and tracking order status.
    - Access at [http://localhost:8000/](http://localhost:8000/)
  - **Delivery Boy Interface:** Enables viewing assigned orders and updating order status.
    - Access at [http://127.0.0.1:8000/auth/authentication_userhome/signin/delivery-signin](http://127.0.0.1:8000/auth/authentication_userhome/signin/delivery-signin)
  - **Restaurant Interface:** Allows managing restaurant profiles, menus, and orders.
    - Access at [http://127.0.0.1:8000/auth/authentication_userhome/signin/hotel-signin](http://127.0.0.1:8000/auth/authentication_userhome/signin/hotel-signin)

- **Admin Interface:** Offers administrative functionalities for managing users, orders, and site configurations.
  - Access at [http://localhost:8000/admin/](http://localhost:8000/admin/)
  - Use superuser credentials created during setup.

## Screenshots


![App Screenshot](https://github.com/jojijose101/Anti-sosh/blob/main/screenshot/Screenshot%20from%202024-04-03%2019-36-39.png)
![App Screenshot](https://github.com/jojijose101/Anti-sosh/blob/main/screenshot/Screenshot%20from%202024-04-03%2019-42-17.png)
![App Screenshot](https://github.com/jojijose101/Anti-sosh/blob/main/screenshot/Screenshot%20from%202024-04-03%2019-44-21.png)
