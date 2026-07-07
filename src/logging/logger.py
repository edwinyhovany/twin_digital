# src/logging/logger.py
"""Centralised logger configuration.

Usage:
    from src.logging import get_logger
    logger = get_logger(__name__)
    logger.info("Message")
"""

import logging
import pathlib
import sys

# Define a logs directory at the project root
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]
LOGS_DIR = PROJECT_ROOT / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

def get_logger(name: str) -> logging.Logger:
    """Return a logger with console and file handlers.

    The logger is configured only once per process.
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # Already configured

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    logger.addHandler(console)

    # File handler (rotating daily)
    file_path = LOGS_DIR / "twin_digital.log"
    file_handler = logging.FileHandler(file_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger
