import unittest
from validators import validate_payload

class TestValidators(unittest.TestCase):
    def test_valid_payload(self):
        payload = {"project": {"name": "Test"}, "status": "success"}
        self.assertTrue(validate_payload(payload))

    def test_invalid_payload(self):
        payload = {"project": {}, "status": "success"}
        self.assertFalse(validate_payload(payload))

if __name__ == "__main__":
    unittest.main()