from django.db import models
# from django import forms
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255,unique=True)
#     password = forms.CharField(widget=forms.PasswordInput)
#     last_login = forms.DateField()
#     USERNAME_FIELD = email
#     # isclient = models.BooleanField()
#     # isRestaurant = models.BooleanField()


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    isClient = models.BooleanField(default=1)
    isRestaurant = models.BooleanField(default=0)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
