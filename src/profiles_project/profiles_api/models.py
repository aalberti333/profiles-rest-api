from django.db import models
from django.contrib.auth.models import AbstractBaseUser #lets you build on Django's standard user model
from django.contrib.auth.models import PermissionsMixin #adds permissions to abstractbaseuser
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Helps DJango work with our custom user model"""

    def create_user(self, email, name, password=None):
        """creates a new user profile object."""

        #if not email is provided, raise a value error
        if not email:
            raise ValueError('Users must have an email address.')

        #corrects for uppercase
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        #automatically encrypted!
        user.set_password(password)
        #use same db we used with the user profile manager
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """creates and saves a new superuser with given details"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin): #inherits from what's in paranthesis
    """Represents a "user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True) #each user must have a unique email address
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #object manager is how we can manage the user profiles
    #this is required when substituting the custom user profile in Django

    objects = UserProfileManager()

    #username for people to log into
    USERNAME_FIELD = 'email'

    #email is already required by default because of what we wrote above
    REQUIRED_FIELDS = ['name']

    #THESE ARE REQUIRED WHEN USING ABSTRACTBASEUSER AND PERMISSIONS
    def get_full_name(self):
        """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        """used to get a users short name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email
