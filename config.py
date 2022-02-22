import yaml


PrintAllPossibilitiesRule = False
PrintSourcePossibilitiesRule = False


def init_config() -> dict:
    global CONFIG
    with open("config.yaml", "r") as fp:
        CONFIG = yaml.safe_load(fp)
