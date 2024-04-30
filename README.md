## CAPSTONE PROJECT:: Little lemon

`Following are the Little Lemon API URL`

### Steps to run the application
1. `pip install pipenv`
2. `pipenv shell`
3. `pipenv install`
4. `python manage.py runserver`

`Base URL:` http://127.0.0.1

### Booking Endpoint: Supports CRUD
http://127.0.0.1/api/v1/restaurant/booking/ <br/>
http://127.0.0.1/api/v1/restaurant/booking/1 <br/>

### Menu Endpoint
http://127.0.0.1/api/v1/restaurant/menu
http://127.0.0.1/api/v1/restaurant/menu/1

### DRF Token Endpoint:
http://127.0.0.1/api/v1/restaurant/api-token-auth/


### Djoser Endpoints:
http://127.0.0.1:8000/auth/users/<br/>
http://127.0.0.1:8000/auth/users/me/<br/>
http://127.0.0.1:8000/auth/users/confirm/<br/>
http://127.0.0.1:8000/auth/users/resend_activation/<br/>
http://127.0.0.1:8000/auth/users/set_password/<br/>
http://127.0.0.1:8000/auth/users/reset_password/<br/>
http://127.0.0.1:8000/auth/users/reset_password_confirm/<br/>
http://127.0.0.1:8000/auth/users/set_username/<br/>
http://127.0.0.1:8000/auth/users/reset_username/<br/>
http://127.0.0.1:8000/auth/users/reset_username_confirm/<br/>

### Djoser TOKEN:
http://127.0.0.1:8000/auth/token/login/<br/>

### Djoser JWT Authentication:
http://127.0.0.1:8000/auth/jwt/create/<br/>
http://127.0.0.1:8000/auth/jwt/verify/

## RUN TESTS
`python manage.py test tests/`
