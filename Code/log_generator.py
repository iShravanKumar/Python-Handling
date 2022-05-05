import logging
from datetime import date

logging.basicConfig(filename=f'Log-{date.today().strftime("%b-%d-%Y")}.log', level=logging.INFO)
