from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="lerton",
            email="josinelerton@gmail.com",
            password="josineoffsec"
        )
        self.assertEqual(user.username, "lerton")
        self.assertEqual(user.email, "josinelerton@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username="margarida",
            email="margarida@gmail.com",
            password="margarida123"
        )
        self.assertEqual(superuser.username, 'margarida')
        self.assertEqual(superuser.email, 'margarida@gmail.com')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)
