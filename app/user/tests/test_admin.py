from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """setUp: Run before the test is run"""

        # Client() : 사용자
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@dev.com',
            password='admin1234'
        )
        # force_login: 강제로 로그인
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@naver.com',
            password='test1234',
            name='test'
        )

    def test_users_listed(self):
        """Test that users are listed on user page."""
        # reverse: find URL with name or viewname
        # resolve: find URL with match url
        url = reverse('admin:user_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works."""
        url = reverse('admin:user_user_change', args=[self.user.id])
        # /admin/user/user/1
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works."""
        url = reverse('admin:user_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)