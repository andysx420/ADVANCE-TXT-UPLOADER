# Don't Remove Credit Tg - @AndySX25

import logging
from logging.handlers import RotatingFileHandler

# Set up root logger
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S"
)

# File handler
file_handler = RotatingFileHandler("logs.txt", maxBytes=50_000_000, backupCount=10)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Optional: Silence noisy libraries like pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
