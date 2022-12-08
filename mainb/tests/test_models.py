from django.test import TestCase
from mainb.models import Author


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='John', last_name='Doe', user_name='mrBoss')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    def test_user_name_label(self):
        author = Author.objects.get(id=1)
        expected_user_name = '%s' % author.user_name
        self.assertEquals(expected_user_name, str(author.user_name))

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_user_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('user_name').max_length
        self.assertEquals(max_length, 80)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/mainb/authors/1')
