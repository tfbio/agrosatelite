from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

from farm_base.models import Owner


class TestAPIClass(APITestCase, TestCase):
    client = APIClient()
 
    @classmethod
    def setUpTestData(cls):
        Owner.objects.create(name='Test Owner',document='111.111.111-11',document_type='CPF')
        cls.client.post('/api/v1/farms', {
          "name": "Test Farm",
          "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ],
                    [
                      -48.51244926452636,
                      -27.599661959066744
                    ],
                    [
                      -48.50918769836426,
                      -27.599205575928863
                    ],
                    [
                      -48.50832939147949,
                      -27.592968149256045
                    ],
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ]
                  ]
                ]
              },
          "municipality": "string",
          "state": "string",
          "centroid": "null",
          "area": 10,
          "owner": 1
        }, format='json')
        pass

    def test_get_farm_list(self):
        response = self.client.get('/api/v1/farms')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,text='"id":1,"name":"Test Farm"')
        self.assertContains(response,text='"municipality":"string","state":"string"')
        self.assertContains(response,text='"owner_id":1')

    def test_get_farm_detail(self):
        response = self.client.get('/api/v1/farms/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,text='"name":"Test Owner"')
        self.assertContains(response,text='"document":"111.111.111-11"')
        self.assertContains(response,text='"municipality":"string","state":"string"')
        self.assertContains(response,text='geometry')
        self.assertContains(response,text='"is_active":true')

    def test_post_farm_with_mandatory_fields(self):
        response = self.client.post('/api/v1/farms', {
          "name": "string",
          "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ],
                    [
                      -48.51244926452636,
                      -27.599661959066744
                    ],
                    [
                      -48.50918769836426,
                      -27.599205575928863
                    ],
                    [
                      -48.50832939147949,
                      -27.592968149256045
                    ],
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ]
                  ]
                ]
              },
          "municipality": "string",
          "state": "string",
          "centroid": "null",
          "area": 10,
          "owner": 1
        }, format='json')
        self.assertEqual(response.status_code, 201)   

        no_name_response = self.client.post('/api/v1/farms', {
          "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ],
                    [
                      -48.51244926452636,
                      -27.599661959066744
                    ],
                    [
                      -48.50918769836426,
                      -27.599205575928863
                    ],
                    [
                      -48.50832939147949,
                      -27.592968149256045
                    ],
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ]
                  ]
                ]
              },
          "municipality": "string",
          "state": "string",
          "owner": 1
        }, format='json')
        self.assertEqual(no_name_response.status_code, 400) 

        no_state_response = self.client.post('/api/v1/farms', {
          "name": "string",
          "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ],
                    [
                      -48.51244926452636,
                      -27.599661959066744
                    ],
                    [
                      -48.50918769836426,
                      -27.599205575928863
                    ],
                    [
                      -48.50832939147949,
                      -27.592968149256045
                    ],
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ]
                  ]
                ]
              },
          "municipality": "string",
          "owner": 1
        }, format='json')
        self.assertEqual(no_state_response.status_code, 400) 

        no_municipality_response = self.client.post('/api/v1/farms', {
          "name": "string",
          "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ],
                    [
                      -48.51244926452636,
                      -27.599661959066744
                    ],
                    [
                      -48.50918769836426,
                      -27.599205575928863
                    ],
                    [
                      -48.50832939147949,
                      -27.592968149256045
                    ],
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ]
                  ]
                ]
              },
          "state": "string",
          "owner": 1
        }, format='json')
        self.assertEqual(no_municipality_response.status_code, 400)       

        no_owner_response = self.client.post('/api/v1/farms', {
          "name": "string",
          "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ],
                    [
                      -48.51244926452636,
                      -27.599661959066744
                    ],
                    [
                      -48.50918769836426,
                      -27.599205575928863
                    ],
                    [
                      -48.50832939147949,
                      -27.592968149256045
                    ],
                    [
                      -48.510990142822266,
                      -27.592892080886568
                    ]
                  ]
                ]
              },
          "municipality": "string",
          "state": "string",
        }, format='json')
        self.assertEqual(no_owner_response.status_code, 400)  