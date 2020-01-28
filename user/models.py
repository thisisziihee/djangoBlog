from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

GENDER_CHOICES = (
    (0, 'Female'),
    (1, 'Male'),
    (2, 'Not to disclose')
)



class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, gender = 1, **extra_fields):
        if not email :
            raise ValueError('The given email mist be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email = email, username = username, gender=gender, **extra_fields)
        user.set_password(password)
        user.save (using = self._db)
        return user

    def create_user(self, email, username = '', password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(email, 'like_section.html', password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name = "email", max_length = 255, unique = True)
    username = models.CharField(max_length=30)
    gender = models.SmallIntegerField(choices = GENDER_CHOICES)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "<%d %s>" %(self.pk, self.email)
