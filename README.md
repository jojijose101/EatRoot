# Food Delivery App using Django

This project is a food delivery web application built with Django, MySQL, and Bootstrap. It allows customers to browse restaurants, place orders, and track their status. Delivery boys can view assigned orders and update their status, while restaurants can manage their menus and incoming orders.

 - **Deploy Link:** 
    - Access at [(https://eatroot101.pythonanywhere.com/auth/authentication_userhome/choose/choose](https://eatroot101.pythonanywhere.com/auth/authentication_userhome/choose/choose)

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


![App Screenshot](https://github.com/jojijose101/EatRoot/blob/main/screenshot/Screenshot%20from%202024-07-25%2015-06-46.png)
![App Screenshot](https://github.com/jojijose101/EatRoot/blob/main/screenshot/Screenshot%20from%202024-07-26%2009-16-40.png)
![App Screenshot](https://github.com/jojijose101/EatRoot/blob/main/screenshot/Screenshot%20from%202024-07-26%2009-17-57.png)
![App Screenshot](https://github.com/jojijose101/EatRoot/blob/main/screenshot/Screenshot%20from%202024-07-26%2009-18-42.png)
![App Screenshot](https://github.com/jojijose101/EatRoot/blob/main/screenshot/Screenshot%20from%202024-07-26%2009-18-58.png)
![App Screenshot](https://github.com/jojijose101/EatRoot/blob/main/screenshot/Screenshot%20from%202024-07-26%2009-46-22.png)
![App Screenshot](https://github.com/jojijose101/EatRoot/blob/main/screenshot/Screenshot%20from%202024-07-26%2009-49-12.png)
![App Screenshot](https://github.com/jojijose101/EatRoot/blob/main/screenshot/Screenshot%20from%202024-07-26%2009-55-09.png)
![App Screenshot](https://github.com/jojijose101/EatRoot/blob/main/screenshot/Screenshot%20from%202024-07-26%2009-56-13.png)
