from pathlib import Path


class Vault(object):
    # Default paths
    dir_ = Path.home() / '.vault'
    config_path_default = dir_ / '.config'
    vault_path_default = dir_ / '.secure.db'

    def __init__(self, config_path: Path = None, vault_path: Path = None):
        self.config_path = config_path if config_path is not None else Vault.config_path_default
        self.vault_path = vault_path if vault_path is not None else Vault.vault_path_default
