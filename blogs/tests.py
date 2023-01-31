from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.Post1 = Post.objects.create(
            title='title5',
            text='this is a description about title5',
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user,
        )
        cls.Post2 = Post.objects.create(
            title='title6',
            text='this is a description about title6',
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user,
        )
    def test_post_model_str(self):
        post = self.Post1
        self.assertEqual(str(post) ,post.title)



    def test_post_detail_view(self):
        self.assertEqual(self.Post1.title ,'title5')
        self.assertEqual(self.Post1.text, 'this is a description about title5')
        self.assertEqual(self.Post1.status, Post.STATUS_CHOICES[0][0])
        self.assertEqual(self.Post1.author, self.user)

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_with_name_of_url(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.Post1.title)

    def test_detail_list_url(self):
        response = self.client.get(f'/blog/{self.Post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_detail_list_with_name_of_url(self):
        response = self.client.get(reverse('post_detail',args=[self.Post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_detail_list_page(self):
        response = self.client.get(reverse('post_detail', args=[self.Post1.id]))
        self.assertContains(response, self.Post1.title)
        self.assertContains(response, self.Post1.text)

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.Post1.title)
        self.assertNotContains(response, self.Post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'),{
            'title' : 'some title',
            'text' :'this is a description some title',
            'status' : 'pub',
            'author' : self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title ,'some title')
        self.assertEqual(Post.objects.last().text, 'this is a description some title')
        self.assertEqual(Post.objects.last().status ,'pub')
        #self.assertEqual(Post.objects.last().author,  self.user.id)

    def test_post_update_view(self):
        response =self.client.post(reverse('post_update',args=[self.Post2.id]),{
            'title' : 'title5 updated',
            'text' : 'this is a description about title5 updated',
            'status': 'pub',
            'author': self.Post2.author.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title,'title5 updated')
        self.assertEqual(Post.objects.last().text,'this is a description about title5 updated')
    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.Post1.id]))
        self.assertEqual(response.status_code, 302)







