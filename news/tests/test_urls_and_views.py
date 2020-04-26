from django.test import TestCase
from django.urls import reverse, resolve
from news.views import (
    publication_view, publications_list, create_publication,
    update_publication, delete_publication
)
from news.models import Publication

class TestUrls(TestCase):
    
    def setUp(self):
        self.publication = Publication.objects.create(
            author = "aaa",
            title = "Title",
            text = "loremipsumdolorsitamet",
        )

    def test_publications_list_url_is_resolved(self):
        url = reverse('publications_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, publications_list)

    def test_create_publication_url_is_resolved(self):
        url = reverse('create_publication')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, create_publication)

    def test_detail_view_url_is_resolved(self):
        resp = self.client.get(reverse('detail_view', kwargs={'pk':self.publication.pk}))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'news/show_publication.html')


    def test_update_publication_url_is_resolved(self):
        resp = self.client.get(reverse('update_publication', kwargs={'pk':self.publication.pk}))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'news/create_publication.html')

    def test_delete_publication_url_is_resolved(self):
        resp = self.client.get(reverse('delete_publication', kwargs={'pk':self.publication.pk}))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'news/publication_confirm_delete.html')