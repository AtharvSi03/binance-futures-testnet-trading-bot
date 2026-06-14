from bot.cli import get_args
from bot.client import get_client
from bot.orders import (
    place_market_order,
    place_limit_order
)
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger

logger = setup_logger()


def print_response(order):
    print("\n========== RESPONSE ==========")

    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))

    if "avgPrice" in order:
        print("Average Price:", order["avgPrice"])

    print("\nSUCCESS")


def main():
    try:
        args = get_args()

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        logger.info(
            f"Order Request: {symbol} {side} {order_type}"
        )

        client = get_client()

        print("\n========== ORDER SUMMARY ==========")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)

        if order_type == "MARKET":

            order = place_market_order(
                client,
                symbol,
                side,
                quantity
            )

        else:

            if not args.price:
                raise ValueError(
                    "Price is required for LIMIT orders"
                )

            price = validate_price(args.price)

            print("Price:", price)

            order = place_limit_order(
                client,
                symbol,
                side,
                quantity,
                price
            )

        logger.info(
            f"Order Success: {order.get('orderId')}"
        )

        print_response(order)

    except Exception as e:
        logger.error(str(e))
        print(f"\nERROR: {e}")


if __name__ == "__main__":
    main()