import os
import yaml
import shutil

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app, db
from config import CONSTANT, CONFIG_SAMPLE_PATH, CONFIG_PATH

app = create_app(os.getenv("FLASK_ENV") or "dev")

app.app_context().push()

manager = Manager(app)
# migrate = Migrate(app, db)



"""
$ python manage.py db init
"""
manager.add_command("db", MigrateCommand)

@manager.command
def build():
    """
    Build app.
    1. copy `config/config.sample.yml` to `config/config.yml`
    2. remove default keys

    $ python manage.py build
    """
    shutil.copy2(CONFIG_SAMPLE_PATH, CONFIG_PATH)

    with open(CONFIG_SAMPLE_PATH, encoding="UTF8") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

        config_file = open(CONFIG_PATH, "w")

        config = {
            k: v for k, v in config.items() if not k.startswith("default_")
        }  # remove "_" keys

        config_file.write(yaml.dump(config))


@manager.command
def run():
    """
    $ python manage.py run
    """
    if not os.path.isfile(CONFIG_PATH):
        raise Exception(f"config: {CONFIG_PATH}. use $ python manage.py build")
    app.run(
        host=CONSTANT["app"]["host"],
        port=CONSTANT["app"]["port"]
    )


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
