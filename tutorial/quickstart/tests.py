from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import django

django.setup()
from tutorial.quickstart.models import Usuario


class UsuarioTests(APITestCase):

    def test_create_user(self):
        """
            Ensure we can create a new account object.
        """
        # DADO
        url = reverse('usuario-list')
        data = {'nome': 'Marcus', 'data_aniversario': '2021-10-14',
                'email': 'marcus@email.com', 'telefone': '81835151'}

        # QUANDO
        response = self.client.post('/usuarios/', data, format='json')

        # ENTÃO
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 1)
        self.assertEqual(Usuario.objects.get(pk=1).nome, 'Marcus')

    def test_update_user(self):
        # DADO
        usuario = Usuario(nome='Luiz', data_aniversario='2021-10-14', email='Luiz@email.com',
                          telefone='81835151')
        usuario.save()
        data = {'nome': 'Luizinho grapixo', 'data_aniversario': '2021-10-14',
                'email': 'grapixinho@email.com', 'telefone': '81835151'}

        # QUANDO
        response = self.client.patch('/usuarios/1/', data, format='json')

        # ENTÃO
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Usuario.objects.get(pk=1).nome, 'Luizinho grapixo')
        self.assertEqual(Usuario.objects.get(pk=1).email, 'grapixinho@email.com')



