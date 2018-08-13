import logging


class BusinesLogic:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def do(self, l):
        iterator = iter(l)
        i = 1
        while True:
            try:
                i /= next(iterator)
            except StopIteration:
                self.logger.exception('Stop iterator')
                break
            except ZeroDivisionError:
                self.logger.critical('Zero division bitch!!!', exc_info=True)
        return i
