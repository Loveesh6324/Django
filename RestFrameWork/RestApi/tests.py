from audioop import reverse
import requests
from django.urls import reverse
from rest_framework.test import APITestCase

from RestApi.models import Student


class TestList(APITestCase):

    # Get Test Case:--------------------------------------------------------------------------------
    def test_getlsit(self):
        response = self.client.get(reverse('Details'))
        if response.status_code == 200:
            print('Data Fetched successfully')
        else:
            print('Data not Fetched')

    # Post Test Cases:------------------------------------------------------------------------------
    def test_post_data_correctly(self):
        data = {
            "name": "ajsbd",
            "email": "asdhsa@gmail.com",
            "age": 22
        }
        response = self.client.post(
            reverse('Details'), data=data)
        if response.status_code == 201:
            print('Data posted successfully')
        else:
            print('Data not posted')

    def test_post_blank_data(self):
        data = {
            "name": "",
            "email": "",
            "age": 66
        }
        response = self.client.post(
            reverse('Details'), data=data)
        if response.status_code == 204:
            print('Blanked data is not posted')
        else:
            print('Data posted successfully')

    def test_post_wrong_type_of_data(self):
        data = {
            "name": "loveesh",
            "email": "loveesh@gmail.com",
            "age": "23"
        }
        response = self.client.post(
            reverse('Details'), data=data)
        if response.status_code == 500:
            print('Data not posted due to type error')
        else:
            print('Data posted successfully')

    # Put Test Cases:-------------------------------------------------------------------------------
    def test_put_data_correctly(self):
        new_student = Student.objects.create(
            name='Loveesh', email='loveesh@gmail.com', age=21)
        data = {
            "name": "Shiva",
            "email": "Shiva@gmail.com",
            "age": 22
        }

        response = self.client.put(reverse(
            'Alter', kwargs={'pk': new_student.pk}), data=data)
        print(response.status_code)
        if response.status_code == 200:
            print('Data Updated successfully')
        else:
            print('Data not Updated')

    def test_put_blank_data(self):
        new_student = Student.objects.create(
            name='Loveesh', email='loveesh@gmail.com', age=21)
        data = {
            "name": "",
            "email": "",
            "age": 66
        }
        response = self.client.put(reverse(
            'Alter', kwargs={'pk': new_student.pk}), data=data)

        if response.status_code == 204:
            print('Blank Data can not be updated ')
        else:
            print('Data Updated Successfully')

    def test_put_wrong_type_of_data(self):
        new_student = Student.objects.create(
            name='Loveesh', email='loveesh@gmail.com', age=21)
        data = {
            "name": "loveesh",
            "email": "loveesh@gmail.com",
            "age": "22"
        }
        response = self.client.put(reverse(
            'Alter', kwargs={'pk': new_student.pk}), data=data)

        if response.status_code == 500:
            print('Data not posted due to type error')
        else:
            print('Data Updated successfully')

    def test_put_duplicate_of_data(self):
        new_student = Student.objects.create(
            name='Loveesh', email='loveesh@gmail.com', age=21)
        data = {
            "name": "Loveesh",
            "email": "loveesh@gmail.com",
            "age": 21
        }
        response = self.client.put(reverse(
            'Alter', kwargs={'pk': new_student.pk}), data=data)

        if response.status_code == 226:
            print('Data not Updated due to duplicate of data')
        else:
            print('Data Updated successfully')

    # Delete Test Case:-----------------------------------------------------------------------------
    def test_delete(self):
        new_student = Student.objects.create(
            name='Loveesh', email='loveesh@gmail.com', age=21)
        response = self.client.delete(reverse(
            'Alter', kwargs={'pk': new_student.pk}))
        if response.status_code == 200:
            print('Data deleted successfully')
        else:
            print('Data not deleted successfully')
