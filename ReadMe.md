**Django Project Example for Class based views, user model expansion and authentication**

# Notes:

1. for extending user model by inheriting of "AbstractUser" or "AbstractBaseUser" you have to specify this in the "setting.py" by adding `AUTH_USER_MODEL = 'app.CostumeUserModel'`  to it

2. more information on extending the default User model https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html