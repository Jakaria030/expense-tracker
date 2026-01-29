import logging
import os

# -----------------------------
# Build log file path
# -----------------------------
filename = "logs/tracker.log"
folder = os.path.dirname(filename)

# Create logs folder if not exists
if folder:
    os.makedirs(folder, exist_ok=True)

# Logger factory
def get_logger(name="tracker"):
    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # File handler writes to logs/tracker.log
    file_handler = logging.FileHandler(filename)
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    file_handler.setFormatter(formatter)


    logger.addHandler(file_handler)
    logger.propagate = False

    return logger
