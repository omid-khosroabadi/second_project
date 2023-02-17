from .cart import Cart


def test_(request):
    return {'cart': Cart(request)}

