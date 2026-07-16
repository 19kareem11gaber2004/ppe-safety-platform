import logging
import sys
import json
from datetime import datetime, UTC


class JsonFormatter(logging.Formatter):

    def format(self, record):

        log_record = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
        }

        if hasattr(record, "request_id"):
            log_record["request_id"] = record.request_id

        return json.dumps(log_record)


def setup_logging():

    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(
        JsonFormatter()
    )

    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    logger.handlers.clear()

    logger.addHandler(handler)


logger = logging.getLogger(__name__)
