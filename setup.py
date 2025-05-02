import vars
import yaml

def setup():
    # read yaml file
    config_file = open("config.yaml", 'r')
    config = yaml.load(config_file)

    # setup global varables
    vars.config = config
    vars.timeout = config.timeout
    vars.bitfile = config.bitfile
    vars.serial = config.serial
    vars.output = config.output
    vars.vivado = config.vivado
    vars.upload_cmd = config.upload_cmd
    
    _setup_serial()
    _setup_logger()

def _setup_serial():
    pass
# start serial

def _setup_logger():
    pass
# start logger
