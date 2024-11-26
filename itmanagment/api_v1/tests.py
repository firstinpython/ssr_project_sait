from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import UsersModel, DevStackModel, ProfessionCategoryModel, RoleModel

class CreateUserAPITest(APITestCase):
    def setUp(self):
        # Создаем необходимые объекты для тестов
        self.role = RoleModel.objects.create(name_role="Test Role")
        self.profession_category = ProfessionCategoryModel.objects.create(name_prof_category="Test Profession")
        self.dev_stack = DevStackModel.objects.create(user_stack="Test Stack")

    def test_create_user(self):
        url = 'http://127.0.0.1:8000/api/v1/create_user/'
        data = {
            "username": "jopavuvvxa",
            "first_name": "Tagir",
            "last_name": "sodnonv",
            "email": "ntr.0707@mail.ru",
            "age": 17,
            "name_role": "Test Role",
            "name_prof_category": "Test Profession",
            "dev_stack": ["Test Stack"],
            "password": "lolololol"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'User is created')
        self.assertEqual(response.data['data']['username'], 'jopavuvvxa')
        self.assertEqual(response.data['data']['first_name'], 'Tagir')
        self.assertEqual(response.data['data']['last_name'], 'sodnonv')
        self.assertEqual(response.data['data']['email'], 'ntr.0707@mail.ru')
        self.assertEqual(response.data['data']['age'], 17)


    def test_create_user_invalid_data(self):
        url = 'http://127.0.0.1:8000/api/v1/create_user/'
        data = {
            "username": "",  # Невалидные данные
            "first_name": "Tagir",
            "last_name": "sodnonv",
            "email": "ntr.0707@mail.ru",
            "age": 17,
            "role": self.role.id,
            "profession_category": self.profession_category.id,
            "dev_stack": [self.dev_stack.id],
            "password": "lolololol"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_missing_required_field(self):
        url = 'http://127.0.0.1:8000/api/v1/create_user/'
        data = {
            "username": "jopauxa",
            "first_name": "Tagir",
            "last_name": "sodnonv",
            "email": "ntr.0707@mail.ru",
            "age": 17,
            "role": self.role.id,
            "profession_category": self.profession_category.id,
            "dev_stack": [self.dev_stack.id],
            # Пропущен пароль
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
