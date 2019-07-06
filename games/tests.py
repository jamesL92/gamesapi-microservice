from django.test import TestCase

# Create your tests here.
class ViewTestCase(TestCase):

    fixtures = ['game']

    def test_retrieve_game_data(self):
        response = self.client.get('/games/1/')
        expected = {
            'name': 'Call of Duty',
            'description': 'For the first time ever in Uncharted history, drive vehicles during gameplay',
            'age_rating': '16',
            'likes': 100,
        }
        actual = response.data
        self.assertDictEqual(expected, actual)