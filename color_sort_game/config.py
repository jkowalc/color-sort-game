import yaml


def config():
    with open("data/config.yaml", "r") as fp:
        return yaml.safe_load(fp)
