import sys
from omegaconf import OmegaConf


def read_config(key: str):
    config = OmegaConf.load("config/config.yaml")
    keys = key.split(".")
    value = config
    for k in keys:
        value = value.get(k)  # type: ignore
        if not value:
            break
    return value


if __name__ == "__main__":
    key = sys.argv[1]
    value = read_config(key)
    if value:
        print(value)
