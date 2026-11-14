import unittest

from siliarch.profile import max_memory_bytes, validate_memory_bytes


class MemoryBytesTests(unittest.TestCase):

    def test_valid_values(self):
        for value in (1, 65536, max_memory_bytes):
            with self.subTest(value=value):
                self.assertEqual(validate_memory_bytes(value), value)

    def test_invalid_values(self):
        invalid_values = (
            0,
            -1,
            max_memory_bytes + 1,
            True,
            1.5,
            "65536",
            None,
        )

        for value in invalid_values:
            with self.subTest(value=repr(value)):
                with self.assertRaises(ValueError):
                    validate_memory_bytes(value)