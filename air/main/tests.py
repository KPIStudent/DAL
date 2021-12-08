from rest_framework.test import APITestCase
from rest_framework import status


class TestView(APITestCase):
    def test_get_station(self):
        url = '/stations/station/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_station(self):
        url = '/stations/station/'
        data = {
            "id": 4,
            "region": "Dnipro",
            "pollution_percentage": "14.60",
            "allowable_rate": "18.00",
            "chronology": 1
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
