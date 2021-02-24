import os
import yaml
pathConfFile = os.path.abspath(__file__).replace('\\', '/').replace(os.path.basename(__file__), "")


def getConfigFile():
    with open(pathConfFile+"conf.yaml") as file:
        return yaml.safe_load(file)

