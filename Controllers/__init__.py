from Controllers.HomeController import home_controller
from flask import Flask
import logging


app = Flask(__name__)
app.register_blueprint(home_controller, url_prefix='/')

main_logger = logging.getLogger('base_logger')
main_logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('BaseLogs.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

main_logger.addHandler(fh)
main_logger.addHandler(ch)

main_logger.info("Server started.")
