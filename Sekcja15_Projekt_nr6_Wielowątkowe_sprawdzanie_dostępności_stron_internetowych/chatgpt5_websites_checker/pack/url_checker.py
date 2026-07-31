import requests
import validators
import sys

class UrlChecker:
    @staticmethod
    def check(data: dict) -> dict:
        try:
            valid = validators.url(data["website"])
            if valid:
                data["validUrlFlag"] = True
                response = requests.get(data["website"], allow_redirects=True)
                data["statusCode"] = response.status_code
            else:
                data["validUrlFlag"] = False
        except Exception:
            data["exception"] = str(sys.exc_info()[0])
        return data
