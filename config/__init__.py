import os
import yaml

from config.config import appConfig
from config.utils import getConfig

FLASK_ENV = os.environ.get("FLASK_ENV", default="dev")
CONFIG_SAMPLE_PATH = "config/config.sample.yml"
CONFIG_PATH = "config/config.yml"

CONSTANT = None # prevent null

"""
returns
    appConfig
    CONSTANT
"""

CONSTANT = getConfig(CONFIG_PATH, FLASK_ENV)

# try:
#     with open(CONFIG_PATH, encoding='UTF8') as file:
#         CONSTANT = yaml.load(file, Loader=yaml.FullLoader)[FLASK_ENV]

# except FileNotFoundError:
#     print("build first. $ python manage.py build")






