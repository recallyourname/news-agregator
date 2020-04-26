"""
This module used to test the url patterns and
templates that the views by this urls returns
"""
from django.test import TestCase
from django.urls import reverse, resolve
from news.models import Publication
from news.views import (
    PublicationsList, CreatePublication
)

class TestUrls(TestCase):
    """
    This module used to test the url patterns and
    templates that the views by this urls returns
    """
    def setUp(self):
        """
        Creating an instance of Publication that we are going to use
        in our test scenarios
        """
        self.publication = Publication.objects.create( # pylint: disable=no-member
            author="aaa",
            title="Title",
            text="loremipsumdolorsitamet",
        )

    def test_publications_list_url_is_resolved(self):
        """
        We are getting the url adress by context-name publications_list
        to make sure if the url given by url_patterns is exact the same
        as in view class
        """
        url = reverse('publications_list')
        self.assertEqual(
            resolve(url).func.view_class,
            PublicationsList
        )

    def test_create_publication_url_is_resolved(self):
        """
        Test if create_publication form is opening by the url given
        """
        url = reverse('create_publication')
        self.assertEqual(
            resolve(url).func.view_class,
            CreatePublication
        )

    def test_detail_view_url_is_resolved(self):
        """
        Test if the detail_view is opening by the given url adress with
        the primary key of created in setUp instance
        """
        resp = self.client.get(reverse('detail_view', kwargs={'pk':self.publication.pk}))
        self.assertEqual(
            resp.status_code,
            200
        )
        self.assertTemplateUsed(
            resp,
            'news/show_publication.html'
        )


    def test_update_publication_url_is_resolved(self):
        """
        Test if update view is opening by given url with the
        primary key of created instance
        """
        resp = self.client.get(reverse('update_publication', kwargs={'pk':self.publication.pk}))
        self.assertEqual(
            resp.status_code,
            200
        )
        self.assertTemplateUsed(
            resp,
            'news/create_publication.html'
        )

    def test_delete_publication_url_is_resolved(self):
        """
        Test if delete view is opening by given url with the
        primary key of created instance
        """
        resp = self.client.get(reverse('delete_publication', kwargs={'pk':self.publication.pk}))
        self.assertEqual(
            resp.status_code,
            200
        )
        self.assertTemplateUsed(
            resp,
            'news/publication_confirm_delete.html'
        )
