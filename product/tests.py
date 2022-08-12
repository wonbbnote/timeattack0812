from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

from user.models import User


# Create your tests here.
def test_get_board_list(self) -> None:
    """
    get 함수를 검증하는 함수
    """
    client = APIClient()

    url = "/product"
    response = client.get(url)
    result = response.json()

    self.assertEqual(response.status_code, 200)
