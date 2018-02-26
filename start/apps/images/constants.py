from djchoices import ChoiceItem, DjangoChoices


class Gender(DjangoChoices):
    MALE = ChoiceItem(0, 'male')
    FEMALE = ChoiceItem(1, 'female')
