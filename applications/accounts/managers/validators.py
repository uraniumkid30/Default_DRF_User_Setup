import re


class FieldValidators:
    @staticmethod
    def is_phone_no_valid(value):
        pattern = r"\+?[0-9]{9,18}"
        if len(value) < 10 or not re.match(pattern, value):
            return False
        return value

    @staticmethod
    def is_email_valid(value):
        pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if len(value) < 6 or not re.match(pattern, value):
            return False
        return value

    @staticmethod
    def is_password_valid(value):
        pattern = r"(?=\w{5,25})(?=[^a-z]*[a-z])(?=(?:[^A-Z]*[A-Z]))"
        pattern += r"(?=[^@_!#$%^&*()<>?/\.|}{~:]*[@_!#$%^&*()<>?/\.|}{~:])"
        pattern += r"\D*\d.*"
        if not re.match(pattern, value):
            return False
        return value

    @staticmethod
    def is_username_valid(value):
        if len(value) < 5:
            return False
        return value
