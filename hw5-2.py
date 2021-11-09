import json
import keyword


class GetAttributes:
    def __init__(self, json_dict: dict):
        for key, value in json_dict.items():
            if keyword.iskeyword(key):
                key = f'{key}_'
            if key == 'price':
                key = f'{key}__'
            if isinstance(value, dict):
                setattr(self, key, GetAttributes(value))
            else:
                setattr(self, key, value)
        return None


class BaseAdvert(GetAttributes):
    def __init__(self, json_dict: dict):
        super().__init__(json_dict)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class ColorizeMixin:
    def __repr__(self):
        text = super().__repr__()
        return f'\033[0;{self.repr_color_code}m{text}'


class Advert(ColorizeMixin, BaseAdvert):
    def __init__(self, json_dict: dict, color_code=33):
        self.repr_color_code = color_code
        super().__init__(json_dict)

    @property
    def price(self):
        if hasattr(self, 'price__'):
            if self.price__ < 0:
                raise ValueError('Attribute price must be >= 0')
            else:
                return self.price__
        else:
            return 0


if __name__ == "__main__":
    corgi_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""

    corgi_json = json.loads(corgi_str)
    corgi = Advert(corgi_json)
    print(corgi)
    print(corgi.class_)
    print(corgi.location.address)

    purple_corgi = Advert(corgi_json, color_code=35)
    print(purple_corgi)
