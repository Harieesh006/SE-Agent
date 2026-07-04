import json


class ValidationService:
    def validate_json(self, text: str):
        try:
            return True, json.loads(text)
        except json.JSONDecodeError as e:
            return False, str(e)

    def validate_code(self, code: str) -> bool:
        return len(code.strip()) > 0


validation_service = ValidationService()
