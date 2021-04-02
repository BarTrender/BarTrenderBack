from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from authentication.models import Client, Owner
from authentication.views import login
from django.conf import settings
import datetime, json

class AuthenticationViewTest(TestCase):

    def setUp(self):
        # Users
        self.client_user = User.objects.create_user(username='client@gmail.com', password="password")
        self.client = Client.objects.create(birthday=datetime.datetime.now(),user=self.client_user)

        self.factory = RequestFactory()

    def test_login_ok(self):
        request = self.factory.post("/authentication/login")
        request.headers = {'apiKey': settings.API_KEY, 'Content-Type': 'application/json'}
        request.data = json.loads('{"email":"client@gmail.com", "password":"password"}')
        resp = login.post(self, request)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.data["token"])
        self.assertEqual(resp.data['rol'], "client")

    def test_login_bad_password(self):
        request = self.factory.post("/authentication/login")
        request.headers = {'apiKey': settings.API_KEY, 'Content-Type': 'application/json'}
        request.data = json.loads('{"email":"client@gmail.com", "password":"bad"}')
        resp = login.post(self, request)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.data['error'], "Email or password incorrect")

    def test_login_bad_user(self):
        request = self.factory.post("/authentication/login")
        request.headers = {'apiKey': settings.API_KEY, 'Content-Type': 'application/json'}
        request.data = json.loads('{"email":"fake@gmail.com", "password":"password"}')
        resp = login.post(self, request)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.data['error'], "Email or password incorrect")

    def test_login_bad_request_data(self):
        request = self.factory.post("/authentication/login")
        request.headers = {'apiKey': settings.API_KEY, 'Content-Type': 'application/json'}
        request.data = json.loads('{"email":"client@gmail.com"}')
        resp = login.post(self, request)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.data['error'], "Incorrect Payload")
    
    def test_bad_apiKey(self):
        request = self.factory.post("/authentication/login")
        request.headers = {'apiKey': "badApiKey", 'Content-Type': 'application/json'}
        request.data = json.loads('{"email":"client@gmail.com", "password":"password"}')
        resp = login.post(self, request)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.data['error'], "A400")

    def test_no_apiKey(self):
        request = self.factory.post("/authentication/login")
        request.headers = {'Content-Type': 'application/json'}
        request.data = json.loads('{"email":"client@gmail.com", "password":"password"}')
        resp = login.post(self, request)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.data['error'], "No API KEY Provided")

    def test_no_apiKey(self):
        request = self.factory.post("/authentication/login")
        request.headers = {'Content-Type': 'application/json'}
        request.data = json.loads('{"email":"client@gmail.com", "password":"password"}')
        resp = login.post(self, request)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(resp.data['error'], "No API KEY Provided")