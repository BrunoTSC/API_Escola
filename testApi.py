import unittest
from profs import meuApp

class TestGetUser(unittest.TestCase):
    def setUp(self):
        app = meuApp.test_client()
        self.response = app.get('/profs/1')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_existing_user(self):
        app = meuApp.test_client()
        r = app.get('/profs/1')
        data = r.json
        self.assertEqual(dict, type(data))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['nome'], 'Kleber')
        self.assertEqual(data['idade'], 26)
        self.assertEqual(data['matéria'], 'DevOps')
        self.assertEqual(data['observações'], None)

if __name__ == '__main__':
    unittest.main()

   
   
   
