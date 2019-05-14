from django.test import TestCase
from .models import Editor, Images, tags

class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'John', last_name ='Victor', email ='johnvictor0002@gmail.com')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.john,Editor))

class ImageTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.john= Editor(first_name = 'John', last_name ='Victor', email ='johnvictor0002@gmail.com')
        self.john.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image=Images(title = 'Test Image',post = 'This is a random test Post',editor = self.john)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Images.objects.all().delete()


def test_get_images_today(self):
        today_images = Image.todays_news()
        self.assertTrue(len(today_image) > 0)
