
# MyRent

MyRent is a web application designed to streamline rental property management for landlords and tenants. It provides a centralized platform for tracking rental payments, handling maintenance requests, and communicating important announcements.

## Features

- **User Authentication**: Separate login portals for tenants and administrators
- **Rent Payment Tracking**: Tenants can upload payment receipts, and landlords can verify and manage payments
- **Digital Complaint System**: Simplified submission and tracking of maintenance issues and complaints
- **Announcement Platform**: Centralized system for landlords to share important updates with tenants
- **FAQ Management**: Dynamic FAQ section that can be updated by administrators
- **User Management**: Admin tools to create and manage tenant accounts

## Technologies Used

- **Backend**: Python + Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: MySQL (with phpMyAdmin)
- **Server**: XAMPP
- **Development Environment**: Visual Studio Code

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/myrent.git
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Start XAMPP and ensure MySQL service is running
   - Create a new database named `myrent_db`
   - Import the database schema from `database/schema.sql`

4. Configure the application:
   - Update database connection details in `__init__.py`

5. Run the application:
   ```
   python main.py
   ```

6. Access the application at `http://localhost:5000`

## Project Structure

- **`__init__.py`**: Application initialization and configuration
- **`models.py`**: Database models and schema
- **`views.py`**: User-facing route handlers
- **`auth.py`**: Authentication logic
- **`admin.py`**: Administrator route handlers
- **`templates/`**: HTML templates for the application
- **`static/`**: CSS, JavaScript, and other static assets

## Default Login Credentials

- **Admin:**
  - Email: admin@myrent.com
  - Password: admin123

## Screenshots

![image](https://github.com/user-attachments/assets/a0c6632c-8921-45e9-8b7c-eab7739f5df2)
![image](https://github.com/user-attachments/assets/c11a75bb-d510-4228-ae6b-39cc2e1ca4df)
![image](https://github.com/user-attachments/assets/fff239d4-dbf6-4cc9-beb5-f148fe8371d9)
![image](https://github.com/user-attachments/assets/f250e674-3c2b-4b56-b29e-2e96d64bc6f2)
![image](https://github.com/user-attachments/assets/2bc521cc-9db5-43d1-98cc-2470d969927f)
![image](https://github.com/user-attachments/assets/6223ef5b-25ec-409a-b5ca-f2b9fdbb7b7b)
![image](https://github.com/user-attachments/assets/085c0064-8731-4c68-b58c-0b7062dc5348)
![image](https://github.com/user-attachments/assets/aaad3e13-7751-483e-a01a-aae4dd0be707)
![image](https://github.com/user-attachments/assets/c6a7baa8-ff9c-4d7f-8681-a69531ca0959)
![image](https://github.com/user-attachments/assets/b819a592-4345-44a2-84b2-08e45d507228)
![image](https://github.com/user-attachments/assets/69dc653b-3dfc-45e7-ac90-d8e6d0c9d098)
![image](https://github.com/user-attachments/assets/fec39291-b8a5-4386-bdf7-574c58d76ad1)
![image](https://github.com/user-attachments/assets/751b4ae2-98fe-46b7-a845-2981a0bf25a6)















## Future Enhancements

- Integration with direct bank transaction APIs
- Multilingual support
- AI-powered support chatbot

## FYP ONLY

## Contributors
AUTHOR: MUHAMMAD SYAZWAN BIN RAZALI
SUPERVISOR: NURRUL QURRAISYA NADIYYA BT MD KHAIR
EXAMINER: NOR AZURA BT SALLEH @ OMAR
