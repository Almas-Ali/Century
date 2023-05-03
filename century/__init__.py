import os
import json
from importlib.util import spec_from_file_location
from icecream import install, ic

# Debugger configuration
install()
ic.configureOutput(prefix='[century] ', includeContext=True)
ic.enable()

__VERSION__ = "0.0.1"
__AUTHOR__ = "Md. Almas Ali"


class century_conf_loader:
    '''
    This class is responsible for loading and saving the century configuration.
    '''
    def __init__(self):
        self._conf = self._load_conf() # load the configuration
        
    def _get_century_json_path(self):
        '''Get the century.json path'''
        return os.path.join(os.getcwd(), "century.json")

    def _load_conf(self):
        '''Load the century.json file and return the configuration or an empty dict'''
        try:
            with open(self._get_century_json_path(), "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        
    def _save_conf(self):
        '''Save the configuration to century.json'''
        with open(self._get_century_json_path(), "w") as f:
            json.dump(self._conf, f, indent=4)

    def get(self, key):
        '''Get a value from the configuration'''
        return self._conf.get(key)
    
    def set(self, key, value):
        '''Set a value to the configuration'''
        self._conf[key] = value
        self._save_conf()

    def update(self, key, value):
        '''Update a value to the configuration'''
        self._conf[key] = value
        self._save_conf()

    def delete(self, key):
        '''Delete a value from the configuration'''
        del self._conf[key]
        self._save_conf()

    def get_all(self):
        '''Get all the configuration'''
        return self._conf
    

class SettingsResolver:
    def __init__(self):...
    
    def _get_settings_path(self):
        self._conf = century_conf_loader()
        # get the settings path from century.json
        self.settings_path = self._conf.get("APP").get('SETTINGS')
        # get the settings module name from the settings path
        
        self.settings = spec_from_file_location(
            "settings", self.settings_path
        ).loader.load_module()

        return self.settings

settings = SettingsResolver()._get_settings_path()


class ControllerResolver:
    def __init__(self):...
    
    def _get_controller_path(self):
        self._conf = century_conf_loader()

        # get the app path from century.json
        self.controller_path = os.path.join(
            self._conf.get("APP").get('PATH'),
            self._conf.get("APP").get('NAME')
        )
        
        # get the controller module name from the APP PATH
        self.controller = spec_from_file_location(
            "controller", os.path.join(
                self.controller_path, "controller.py"
            )
        ).loader.load_module()

        return self.controller
    
# controller = ControllerResolver()._get_controller_path()
