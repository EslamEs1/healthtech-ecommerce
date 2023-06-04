from django.db import models

class HexColorField(models.CharField):

    description = "A string field for hexadecimal color values"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 6
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'INTEGER'

    def get_prep_value(self, value):
        if value is None:
            return None
        return int(value, 16)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        hex_value = format(value, 'X')
        return hex_value
