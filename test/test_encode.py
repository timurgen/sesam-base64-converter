from unittest import TestCase
from os import walk, path

from service.base64transform_service import encode, decode


class TestEncode(TestCase):
    def test_encode(self):
        for (dirpath, dirnames, filenames) in walk("..\\test_data"):
            for name in filenames:
                test_file_name = path.join(dirpath, name)
                file = open(test_file_name, 'rb');
                file_data = file.read();
                file.close()
                encoded_data = encode(file_data)
                decoded_data = decode(encoded_data)
                self.assertEqual(file_data, decoded_data)



