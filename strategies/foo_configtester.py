from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('../setup/user.ini')
print (parser.get('OS', 'user_OS'))
candidate='OS'
print(parser.has_section(candidate))
