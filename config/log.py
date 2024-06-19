import logging

logging.basicConfig(
        level=logging.DEBUG,
        filename="spellcheck.log",
        filemode="w",
        format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger("waiter_log_bot")
