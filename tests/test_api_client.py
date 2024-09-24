import unittest
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTest(unittest.TestCase):

    @patch('src.api_client.requests.get') #el decorador patch inserta una variable dentro del metodo, en este caso mock_get
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"countryName" : "United States of America", "regionName": "California", "cityName": "Mountain View"}
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"),"United States of America")
        self.assertEqual(result.get("region"),"California")
        self.assertEqual(result.get("city"),"Mountain View")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8") #Valida que el codigo este haciendo el llamado al endpoint correcto