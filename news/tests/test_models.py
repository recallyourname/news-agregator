from django.test import TestCase
from news.models import Publication
from django.urls import reverse

class TestModels(TestCase):

    def setUp(self):
        self.publication = Publication.objects.create(
            author = "Author",
            title= "title",
            text = "loremipsumdolorsitamet"
        )

    def test_str_return(self):
        self.assertEquals(self.publication.__str__(), 'title')

    def test_get_absolute_url(self):
        self.assertEquals(self.publication.get_absolute_url(), '/detail/1/')