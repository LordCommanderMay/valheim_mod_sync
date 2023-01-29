import os
import platform

import yaml


class Settings:
    server_ip : str
    mod_sync_port: int
    valheim_path: str
    mod_path: str
    mod_config_path: str


def init_settings():
    if 'settings.yaml' in os.listdir():
        load_settings()
    else:
        create_settings()
        init_settings()


def create_settings():
    valhiem_path = ''
    match platform.system():
        case 'windows':
            valhiem_path = 'C:/Program Files (x86)/Steam/steamapps/common/Valheim'
        case 'Linux':
            valhiem_path = 



def load_settings() -> None:
    file = open("settings.yaml")
    settings_yaml = yaml.safe_load(file)
    Settings.server_ip = settings_yaml["server_ip"]
    Settings.mod_sync_port = settings_yaml["mod_sync_port"]
    Settings.valheim_path = settings_yaml["valheim_path"]
    Settings.mod_path = settings_yaml["mod_path"]
    Settings.mod_config_path = settings_yaml["config_path"]


