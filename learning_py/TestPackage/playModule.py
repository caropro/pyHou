# coding=utf-8
# Author:jonathon woo
# email:live.wujianxuan@gmail.com
# version:1.0.0
import logging
logging.basicConfig(level=logging.INFO)


def run():
    print("Running!")

if __name__ == "__main__":
    logging.log(20, "Running Current playModule As File")
else:
    # {50: 'CRITICAL', 40: 'ERROR', 30: 'WARNING', 20: 'INFO', 10: 'DEBUG', 0: 'NOTSET'}
    logging.log(20, "Import playModule.")