# Testes unitários
class TestIsBase64(unittest.TestCase):

    def test_valid_base64(self):
        self.assertTrue(is_base64("U29tZSBkYXRh"))  # "Some data" em base64
        self.assertTrue(is_base64("SGVsbG8gd29ybGQh"))  # "Hello world!" em base64

    def test_invalid_base64(self):
        self.assertFalse(is_base64("invalid_base64"))  # caracteres inválidos
        self.assertFalse(is_base64("U29tZSBkYXRh$"))  # caractere inválido ($)
        self.assertFalse(is_base64(""))  # string vazia

    def test_partial_padding(self):
        self.assertFalse(is_base64("U29tZSBkYXRh="))  # padding incompleto
        self.assertTrue(is_base64("U29tZSBkYXRh=="))  # padding correto


class TestDecimalEncoder(unittest.TestCase):
    def test_decimal_integer(self):
        data = {"value": Decimal("10.0")}
        encoded = json.dumps(data, cls=DecimalEncoder)
        self.assertEqual(encoded, '{"value": 10}')
    
    def test_decimal_float(self):
        data = {"value": Decimal("10.5")}
        encoded = json.dumps(data, cls=DecimalEncoder)
        self.assertEqual(encoded, '{"value": 10.5}')
    
    def test_string(self):
        data = {"text": "hello"}
        encoded = json.dumps(data, cls=DecimalEncoder)
        self.assertEqual(encoded, '{"text": "hello"}')
    
    def test_set(self):
        data = {"numbers": {1, 2, 3}}
        encoded = json.dumps(data, cls=DecimalEncoder)
        self.assertEqual(json.loads(encoded), {"numbers": [1, 2, 3]})
    
    def test_unsupported_type(self):
        class CustomType:
            pass
        with self.assertRaises(TypeError):
            json.dumps({"custom": CustomType()}, cls=DecimalEncoder)

if __name__ == "__main__":
    unittest.main()
