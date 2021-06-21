class NotFoundException(Exception):
  def __init__(self, message):
    super().__init__(message)

class ForbiddenException(Exception):
  def __init__(self):
    super().__init__('Access forbidden')
