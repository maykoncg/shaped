from django.test import TestCase
from rest_framework import status
class HealthCheck(TestCase):  
   

    def test_operation_type(self):
     
        response = self.client.get(f"/api/pacientes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(f"/api/exames/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)