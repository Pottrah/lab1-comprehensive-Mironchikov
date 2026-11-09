TIER_1_DISCOUNT = 0.97
TIER_2_DISCOUNT = 0.93

MAX_TOTAL_DISCOUNT_PERCENT = 0.70
LARGE_CART_THRESHOLD = 15000
LARGE_CART_DISCOUNT = 0.85


def calculate_cart_total(cart_sum: float, tier: int, promos: list) -> float:
    """Рассчитывает итоговую стоимость корзины с учетом скидок."""
    if cart_sum <= 0:
        return 0.0

    price = float(cart_sum)

    if price > LARGE_CART_THRESHOLD:
        price *= LARGE_CART_DISCOUNT

    promo_actions = {
        "SUMMER": lambda p: p - 500.0,
        "VIP": lambda p: p * 0.90
    }

    for promo in promos:
        if promo in promo_actions:
            price = promo_actions[promo](price)

    tier_discounts = {
        1: TIER_1_DISCOUNT,
        2: TIER_2_DISCOUNT
    }
    price *= tier_discounts.get(tier, 1.0)

    min_allowed_price = cart_sum * MAX_TOTAL_DISCOUNT_PERCENT
    if price < min_allowed_price:
        price = min_allowed_price

    return round(price, 2)
