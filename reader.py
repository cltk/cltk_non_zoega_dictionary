import os
import yaml

PACKDIR = os.path.abspath(os.path.dirname(__file__))


def read_yaml():
    """
    >>> read_yaml()["sonr"]
    '(gen. sonar, dat. syni and søni; pl. synir, sønir; ace. sonu and syni), m. son.'

    """
    with open(os.path.join(PACKDIR, "dictionary.yaml"), "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.CLoader)
