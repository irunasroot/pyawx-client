class ApiUrl:
    def __init__(self, url):
        if "/api/v2" in url:
            url = url.replace("/api/v2", "")
        self._url = url

    def endpoint(self, endpoint):
        endpoint = endpoint.strip()

        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"

        if not endpoint.endswith("/"):
            endpoint = f"{endpoint}/"

        return f"{self._url}{endpoint}"

