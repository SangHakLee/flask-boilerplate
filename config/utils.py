import yaml


def getConfig(config_path, env):
    """
    :config_path: 설정 파일 경로
    :env: 환경 [local, dev, prod]
    """
    try:
        with open(config_path, encoding='UTF8') as file:
            CONSTANT = yaml.load(file, Loader=yaml.FullLoader)[env]
            return CONSTANT
    except FileNotFoundError:
        print("build first. $ python manage.py build")