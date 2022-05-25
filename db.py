import configparser
import pathlib


def get_user_pass(section: str = "DEFAULT"):
  conf_file_path = pathlib.Path(__file__).parent.absolute().joinpath('conf.ini')
  config = configparser.ConfigParser()
  config.read(conf_file_path)
  try:
    data = config[section]
  except KeyError:
    raise KeyError(f"""Invalid section '{section}' specified. Must be one of ['Default', '{', '.join(config.sections())}']""")
  return data["username"], data["password"]

print(get_user_pass('grrom'))