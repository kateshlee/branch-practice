def get_response() -> int:
    return requests.get("http://www.google.com/').status_code
