from django.test import TestCase

# Create your tests here.
class ViewTestCase(TestCase):

    fixtures = ['game', 'publisher', 'platform', 'user', 'comment']

    def test_retrieve_game_data_successful(self):
        response = self.client.get('/games/1/')
        expected = {
            'name': 'Call of Duty',
            'description': 'For the first time ever in Uncharted history, drive vehicles during gameplay',
            'age_rating': '16',
            'likes': 100,
            'by': 'Sony',
            'platform': ['PS4'],
            'comments': [{
                'user': 'bob',
                'message': 'Cracking game far too much cinematic',
                'dateCreated': '2011-01-03',
                'like': 6
            }, {
                'user': 'testingPriest',
                'message': 'Not enough shooting for me,far too easy ',
                'dateCreated': '2011-04-02',
                'like': 5
            }],
        }
        actual = response.data
        self.maxDiff = None
        self.assertDictEqual(expected, actual)

    def test_retrieve_game_data_404(self):
        response = self.client.get('/games/23/')
        self.assertEqual(response.status_code, 404)