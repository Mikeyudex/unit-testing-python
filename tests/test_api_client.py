import unittest
import unittest.mock
import requests
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

    @patch('src.api_client.requests.get') #el decorador patch inserta una variable dentro del metodo, en este caso mock_get
    def test_get_location_returns_side_effect(self, mock_get):

        #side_effect sirve para agregar comportamiento a nuestros llamados a un api, en este caso hay dos efectos, el primero es una excepción y el segundo una respuesta exitosa.
        #La primera vez que se llame al metodo get_location fallará, en el segundo llamado será exitoso.
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code = 200,
                json=lambda: {
                    "countryName" : "United States of America",
                    "regionName": "California",
                    "cityName": "Mountain View"
                }
            )
        ]

        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"),"United States of America")
        self.assertEqual(result.get("region"),"California")
        self.assertEqual(result.get("city"),"Mountain View")

        
