from canari.maltego.message import *

__author__ = 'Tatsuya Daitoku'
__copyright__ = 'Copyright 2019, attack-maltego Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.1'
__maintainer__ = 'Tatsuya Daitoku'
__email__ = 'tadmaddad@gmail.com'
__status__ = 'Development'


class Technique(Entity):
    _category_ = 'attack-maltego'
    _namespace_ = 'attack-maltego'

    properties_technique = StringEntityField('properties.technique', display_name='Technique', is_value=True)


class Tools(Entity):
    _category_ = 'attack-maltego'
    _namespace_ = 'attack-maltego'

    properties_tools = StringEntityField('properties.tools', display_name='Tools', is_value=True)


class Malware(Entity):
    _category_ = 'attack-maltego'
    _namespace_ = 'attack-maltego'

    properties_malware = StringEntityField('properties.malware', display_name='Malware', is_value=True)


class Tactic(Entity):
    _category_ = 'attack-maltego'
    _namespace_ = 'attack-maltego'

    properties_tactic = StringEntityField('properties.tactic', display_name='Tactic', is_value=True)


class Actor(Entity):
    _category_ = 'attack-maltego'
    _namespace_ = 'attack-maltego'

    properties_actor = StringEntityField('properties.actor', display_name='Actor', is_value=True)

