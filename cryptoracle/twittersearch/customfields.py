from django.db import models

class BatchedValuesField(models.TextField):

    def __init__(self, *args, **kwargs):
        # Default split token
        self.token = kwargs.pop('token', ',')
        super(BatchedValuesField, self).__init__(*args, **kwargs)

    # value to return when getting from db
    def from_db_value(self, value, expression, connection, context=None):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    # value transformation before saving to db
    def get_db_prep_value(self, value, connection, prepared=False):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([s for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)