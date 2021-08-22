import unittest
import requests
import json

from src import settings


class QueryTestCase(unittest.TestCase):

    def setUp(self):
        self.queries = settings.DATA_QUERIES

    def test_table_status_code(self):
        for i in self.queries:
            response = requests.get(self.queries[i]['URL'])
            self.assertEqual(200, response.status_code)

    def test_query_status_code(self):
        for i in self.queries:
            with open(self.queries[i]['JSON_QUERY']) as file:
                json_query = json.load(file)
            response = requests.post(self.queries[i]['URL'], json=json_query)
            self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
