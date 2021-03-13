import random
from django.conf import settings
import string

# from shortner.models import ssurlURL

shorturl_min = getattr(settings, "shorturl_min", 5)

def code_generator(size=shorturl_min,chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return "".join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=shorturl_min):
    new_code = code_generator(size=size)
    klass = instance.__class__
    qs_exists = klass.objects.filter(shorturl=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code