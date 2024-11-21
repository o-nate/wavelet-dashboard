"""Helper functions for logging"""

import logging


def define_other_module_log_level(level: str) -> None:
    """Disable logger ouputs for other modules up to defined `level`"""
    for log_name in logging.Logger.manager.loggerDict:
        if log_name != "__name__":
            log_level = getattr(logging, level.upper())
            logging.getLogger(log_name).setLevel(log_level)
