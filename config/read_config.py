from omegaconf import OmegaConf


class Config:
    _config = None

    @classmethod
    def load_config(cls, file_path):
        if not cls._config:
            cls._config = OmegaConf.load(file_path)
        return cls._config

CONFIG = Config.load_config("config/config.yaml")
