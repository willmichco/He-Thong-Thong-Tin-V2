class NoIndexMiddleware:
    """Mọi trang khu quản trị trả về X-Robots-Tag: noindex (Phụ lục C.1)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-Robots-Tag"] = "noindex, nofollow"
        return response
