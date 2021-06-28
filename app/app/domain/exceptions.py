class NotFoundException(Exception):
    pass

class ForbiddenException(Exception):
    def __init__(self):
        super().__init__('Access forbidden')
