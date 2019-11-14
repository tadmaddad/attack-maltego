from pyattck import Attck
from canari.maltego.message import Entity, StringEntityField
from canari.maltego.entities import Phrase
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow

__author__ = 'Tatsuya Daitoku'
__copyright__ = 'Copyright 2019, ATT&CK_maltego Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.1'
__maintainer__ = 'tad'
__email__ = 'tadmaddad@gmail.com'
__status__ = 'Development'

attack = Attck()

class Actor(Entity):
    name = StringEntityField('Actor.name', display_name='Actor name',
                             is_value=True, description='Actor or Group')

class Malware(Entity):
    name = StringEntityField('Malware.name', display_name='Malware name',
                             is_value=True, description='Malware')

class Tools(Entity):
    name = StringEntityField('Tools.name', display_name='Tools name',
                             is_value=True, description='Tools')

class Technique(Entity):
    name = StringEntityField('Technique.name', display_name='Technique name',
                             is_value=True, description='Technique')

class Tactic(Entity):
    name = StringEntityField('Tactic.name', display_name='Tactic name',
                             is_value=True, description='Tactic')

@EnableDebugWindow
class TacticToTechnique(Transform):
    
    input_type = Tactic

    def do_transform(self, request, response, config):

        tactic_name = request.entity.value

        for tactic in attack.tactics:
            if tactic_name in tactic.name:
                for technique in tactic.techniques:
                    response += Technique(technique.name)
        return response

