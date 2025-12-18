from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import CanalMensaje, CanalUsuario, Canal, Blog, Avatar

User = get_user_model()


class BlogModelTest(TestCase):
    def test_blog_creation(self):
        blog = Blog.objects.create(
            Tema="Test",
            Material="PLA",
            Escala="1:100"
        )
        self.assertEqual(blog.Tema, "Test")
        self.assertEqual(blog.Material, "PLA")


class CanalModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_canal_creation(self):
        canal = Canal.objects.create()
        self.assertIsNotNone(canal.id)
    
    def test_canal_mensaje_creation(self):
        canal = Canal.objects.create()
        mensaje = CanalMensaje.objects.create(
            canal=canal,
            usuario=self.user,
            texto="Test"
        )
        self.assertEqual(mensaje.texto, "Test")


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
    
    def test_leer_blogs_view(self):
        response = self.client.get(reverse('leerBlogs'))
        self.assertEqual(response.status_code, 200)
