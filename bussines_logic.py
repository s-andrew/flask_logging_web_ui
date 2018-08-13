import logging

class BusinesLogic:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def do(self, l):
        self.logger.debug('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maxime, modi praesentium. Culpa distinctio dolore dolorum enim, exercitationem fugit incidunt inventore iure rem soluta. Consectetur consequuntur esse eveniet impedit iure praesentium quis reiciendis tempore, veritatis! Adipisci architecto atque consectetur culpa dolores inventore iste iusto, nesciunt officiis, optio quis rem temporibus veniam.')
        iterator = iter(l)
        while True:
            try:
                i = 1/next(iterator)
            except StopIteration:
                self.logger.exception('Stop iterator')
                break
            except ZeroDivisionError:
                self.logger.critical('Zero division bitch!!!', exc_info=True)