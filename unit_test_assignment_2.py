import unittest
from second_assignment import YandexDisk

TOKEN = ''
url = 'https://cloud-api.yandex.net/v1/disk/resources'


class TestSecondAssignment(unittest.TestCase):
    def setUp(self) -> None:
        print('Test has started')

    def tearDown(self) -> None:
        print('Test has finished')

    def test_yandex_disk(self):
        ya = YandexDisk(TOKEN)
        self.assertEqual(ya.put_methode_create_folder(url), 201)


if __name__ == '__main__':
    unittest.main()
