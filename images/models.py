from django.db import models
import datetime as dt

# Create your models here.


class Category(models.Model):
    img_category = models.CharField(max_length=60)

    def __str__(self):
        return self.img_category


class Location(models.Model):
    img_location = models.CharField(max_length=60)

    def __str__(self):
        return self.img_location

class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name

        class Meta:
            ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Images(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to='image/')


    @classmethod
    def todays_images(cls):
            today = dt.date.today()
            images = cls.objects.filter(pub_date__date=today)
            return images


    def test_get_images_by_date(self):
            test_date = '2017-03-17'
            date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
            images_by_date = Images.days_images(date)
            self.assertTrue(len(images_by_date) == 0)


    @classmethod
    def days_images(cls, date):
            images = cls.objects.filter(pub_date__date=date)
            return images

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(
            category__img_category__icontains=search_term)
        return images

