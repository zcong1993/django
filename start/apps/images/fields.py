from rest_framework import (
    exceptions,
    fields
)

class ChoiceField(fields.Field):

    def __init__(self, choice, verbose=False, **kwargs):
        super(ChoiceField, self).__init__(**kwargs)
        self.choice = choice
        self.verbose = verbose

    def to_internal_value(self, data):
        if data in self.choice.attributes:
            return data

        if data.isdigit():
            return int(data)

        value = getattr(self.choice, data.upper(), None)
        if value is None:
            raise exceptions.ValidationError(
                'Invalid %s.' % self.choice.__name__)

        return value

    def to_representation(self, value):
        if not self.verbose:
            return value
        return self.choice.attributes.get(value, 'UNDEFINED')
