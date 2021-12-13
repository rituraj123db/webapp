from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from .models import User, MessageData


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser@nadajd.com',
            'password': 'secret'}

    def test_login(self):
        # send login data
        response = self.client.post('/login_user/', self.credentials)
        user = User.objects.get(username='testuser@nadajd.com')
        assert user.username == self.credentials['username']
        assert response.status_code == 302

        # should be logged in now


class CreateMessageTest(TestCase):
    def setUp(self):
        self.data = {
            'message': 'text'
        }

    def test_msg_creation(self):
        response = self.client.post('/message_create/', self.data)
        message_obj = MessageData.objects.get(message='text')
        assert message_obj.message == self.data['message']
        assert response.status_code == 200


class GetMessageTest(TestCase):
    def setUp(self):
        self.data = {
            'message': 'user create '
        }

    def test_msg_creation(self):
        response = self.client.get('/message_list/')
        message_obj = MessageData.objects.all()
        # assert message_obj[0].message == self.data['message']
        assert response.status_code == 200
