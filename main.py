from setting import AllSettings
from binance.um_futures import UMFutures


TF = 15
TP = 0.03
SL = 0.01
DEPOSIT = 10

client = UMFutures(key=AllSettings.BINANCE_API_KEY, secret=AllSettings.BINANCE_SECRET_KEY)


def main():
    pass


if __name__ == "__main__":
    main()
