from worker import Worker
import schedule
from currency import USD, Crypto


def main():
    """
    Main Function
    """
    worker = Worker(USD, Crypto)
    worker.send_message()


if __name__ == "__main__":
    schedule.every().days.at("10:00").do(main)
    while True:
        schedule.run_pending()
