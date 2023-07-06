class Asserts:

    @staticmethod
    def assertEqual(actual, expected, what):
        assert expected == actual, f'Wrong {what} - {actual}'
