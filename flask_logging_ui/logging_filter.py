import logging
import re


class LogsUrlFilter(logging.Filter):
    def __init__(self, url_prefix, name='logs_url_filter'):
        self.regexp = re.compile(r"GET {url_prefix}".format(url_prefix = url_prefix))
        super().__init__(name)

    def filter(self, record):
        return not bool(self.regexp.findall(record.msg))
