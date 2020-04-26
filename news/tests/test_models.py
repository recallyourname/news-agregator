"""
Testing the models module
"""
from django.test import TestCase
from news.models import Publication

class TestModels(TestCase):
    """
    TestModels is a child of unittest.TestCase python class
    that declares exactly the test case
    This exact test is creating a temporary database,
    creating an instance of object Publication (declared in models),
    and testing the features that is declared in Publication class
    """
    def setUp(self):
        self.publication = Publication.objects.create( # pylint: disable=no-member
            author="Author",
            title="title",
            text="loremipsumdolorsitamet"
        )

    def test_str_return(self):
        """
        This function is testing __str__() function to check if
        this function returns the expected value
        """
        self.assertEqual(
            self.publication.__str__(),
            'title'
        )

    def test_get_absolute_url(self):
        """
        This function is testing get_absolute_url() function to check if the
        route returning by this function is equals to the one expected
        """
        self.assertEqual(
            self.publication.get_absolute_url(),
            '/detail/1/'
        )
