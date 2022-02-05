from django.core.cache import caches


def filling_cart(request):
    if not request.session.session_key:
        request.session.save()
    redis_cache=caches['default']
    cart=redis_cache.client.get_client()
    carts=cart.hgetall(request.session.session_key)
    for elm in carts:
        cart.hset(request.user.email,elm.decode("utf-8"),carts[elm])