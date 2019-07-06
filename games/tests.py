from django.test import TestCase

# Create your tests here.
class ViewTestCase(TestCase):

    fixtures = ['game', 'publisher', 'platform']

    def test_retrieve_game_data_successful(self):
        response = self.client.get('/games/1/')
        expected = {
            'name': 'Call of Duty',
            'description': 'For the first time ever in Uncharted history, drive vehicles during gameplay',
            'age_rating': '16',
            'likes': 100,
            'by': 'Sony',
            'platform': ['PS4']
        }
        actual = response.data
        self.assertDictEqual(expected, actual)

    def test_retrieve_game_data_404(self):
        response = self.client.get('/games/23/')
        self.assertEqual(response.status_code, 404)