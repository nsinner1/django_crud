from django.test import SimpleTestCase, TestCase
from django.urls import reverse 
from .models import Books
from django.contrib.auth import get_user_model

# Create your tests here.
class BooksTest(SimpleTestCase):

    def test_homepage_status(self):
        self.help_status_code('home')

    def help_status_code(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        self.check_template_used('home', 'home.html')

    def check_template_used(self, url_name, template):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, template)


class BooksTest2(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test',
            password = 'pass',
        )

        self.books = Books.objects.create(
            title='Test Title',
            author=self.user,
            body='Test Description',
        )

        self.books.save()
        self.book_record = Books.objects.get(pk=1)

    def test_model_content(self): 
        self.assertEqual(self.book_record, self.books)

    def test_model_name(self): 
        self.assertEqual(self.book_record.title, self.books.title)

    def test_create_redirect_home(self): 
        response = self.client.post(reverse('home'),{
            'title' : 'Test Title', 
            'author' : self.user, 
            'body' : 'Test Description',
        } 
        , follow=True)

        self.assertEqual(response.status_code, 405)

        self.assertTemplateUsed('home.html')