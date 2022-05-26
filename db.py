from configparser import ConfigParser
import json

config = ConfigParser()

file = 'conf.ini'
config.read(file)


# getting section data
def get_user_data(section: str = "default"):
  try:
    data = config[section]
  except KeyError:
    raise KeyError(f"""Invalid section '{section}' specified. Must be one of [{', '.join(config.sections())}]""")
  return data["username"], data["password"]


# def strigify_section(section: str = "default"):
#   print(config[section])
#   data = config[section]
#   result = json.dumps(data)
#   return result["username"], result["password"]



# Adding new section then updating the ini file 
config.add_section('account')
config.set('account', 'status', 'inactive')
config.set('account', 'username', 'maangchi')
config.set('account', 'password', 'man234')

with open(file, 'w') as configfile:
  config.write(configfile)


print(config.sections())
print(config['default'])
print(get_user_data('account'))
strigify_section('account')

