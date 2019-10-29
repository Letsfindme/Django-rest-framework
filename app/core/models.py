from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.conf import settings
import uuid
import os


def post_image_file_path(instance, filename):
    """Generate file path for new post image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/post/', filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    #password: Sequelize.STRING,
    firstConnection = models.DateField()
    lastConnection = models.DateField()
    avatar = models.BooleanField(default=False)
    creationDate= models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    birthday = models.DateField()
    age = models.IntegerField()
    status = models.CharField(max_length=255)
    avatar = models.ImageField(null=True, upload_to=post_image_file_path)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Tag(models.Model):
    """Tag to be used for a post"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient to be used in a Post"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    """Post object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    #ingredients = models.ManyToManyField('Ingredient')
    tags = models.ManyToManyField('Tag')
    imageUrl= models.ImageField(null=True, upload_to=post_image_file_path)
    #image = models.ImageField(null=True, upload_to=post_image_file_path)
    starCount = models.IntegerField()
    category = models.CharField(max_length=255, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True, blank=True)
    content = models.CharField(max_length=255)


    def __str__(self):
        return self.title


class Image(models.Model):
    """ Image of post """
    post = models.ForeignKey(
        'Post',
        #related_name='images',
        on_delete=models.CASCADE
    )
    imageRef = models.ImageField(null=True, upload_to=post_image_file_path)


class Address(models.Model):
    """ Address object """
    street= models.CharField(max_length=255, blank=True)
    city= models.CharField(max_length=255, blank=True)
    country= models.CharField(max_length=255, blank=True)
    postcode = models.IntegerField(blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class PostComment(models.Model):
    """ PostComment object """
    title= models.CharField(max_length=255, blank=True)
    text= models.CharField(max_length=255, blank=True)
    imageRef= models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        'Post',
        #related_name='images',
        on_delete=models.CASCADE
    )

class PostRate(models.Model):
    """ PostRate object """
    rate = models.IntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        'Post',
        #related_name='images',
        on_delete=models.CASCADE
    )