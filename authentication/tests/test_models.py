from rest_framework.test import APITestCase

from authentication.models import User


class TestModel(APITestCase):

    def test_created_user(self):
        user = User.objects.create_user('dima', 'dima@gmail.com', 'password123!@')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'dima@gmail.com')
        self.assertEqual(user.username, 'dima')
        self.assertFalse(user.is_staff)

    def test_created_super_user(self):
        super_user = User.objects.create_superuser('kara', 'kata@gmail.com', 'password123@!')
        self.assertIsInstance(super_user, User)
        self.assertTrue(super_user.is_superuser)
        self.assertEqual(super_user.email, 'kata@gmail.com')

    def test_raise_create_user_without_username(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='dima@gmail.com',
                          password='password123!@')
        with self.assertRaisesMessage(ValueError, "The given username must be set"):
            User.objects.create_user(username='', email='dima@gmail.com',
                                     password='password123!@')

    def test_raise_create_user_without_email(self):
        self.assertRaises(ValueError, User.objects.create_user, username='dima', email='',
                          password='password123!@')
        with self.assertRaisesMessage(ValueError, "The given email  must be set"):
            User.objects.create_user(username='dima', email='',
                                     password='password123!@')

    def test_raise_create_super_user_is_staff_is_superuser_False(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True."):
            User.objects.create_superuser(username='dima', email='dima@gmail.com',
                                          password='password123!@', is_staff=False)
        with self.assertRaisesMessage(ValueError, "Superuser must have is_superuser=True."):
            User.objects.create_superuser(username='dima', email='dima@gmail.com',
                                          password='password123!@', is_superuser=False)
