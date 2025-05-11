import logging
import os

def setup_logger(name="network_scanner"):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Format des logs
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Log dans un fichier
    file_handler = logging.FileHandler(f"logs/{name}.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Log dans la console (optionnel)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
