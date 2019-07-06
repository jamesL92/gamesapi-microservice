from django.test import TestCase

# Create your tests here.
class ViewTestCase(TestCase):

    fixtures = ['game']

    def test_retrieve_game_data(self):
        response = self.client.get('/games/1/')
        expected = {
            'name': 'Call of Duty'
        }
        actual = response.data
        self.assertEqual(expected, actual)