from binance.exceptions import BinanceAPIException


def place_market_order(
    client,
    symbol,
    side,
    quantity
):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        return order

    except BinanceAPIException as e:
        raise Exception(f"Binance Error: {e.message}")


def place_limit_order(
    client,
    symbol,
    side,
    quantity,
    price
):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        return order

    except BinanceAPIException as e:
        raise Exception(f"Binance Error: {e.message}")