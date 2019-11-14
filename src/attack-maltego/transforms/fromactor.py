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

@EnableDebugWindow
class ActorToMalware(Transform):
    
    input_type = Actor

    def do_transform(self, request, response, config):

        actor_name = request.entity.value

        for actor in attack.actors:
            if actor_name in actor.name:
                for malware in actor.malwares:
                    response += Malware(malware.name)
        return response

class ActorToTools(Transform):
    
    input_type = Actor

    def do_transform(self, request, response, config):

        actor_name = request.entity.value

        for actor in attack.actors:
            if actor_name in actor.name:
                for tool in actor.tools:
                    response += Tools(tool.name)
        return response

class ActorToTechnique(Transform):
    
    input_type = Actor

    def do_transform(self, request, response, config):

        actor_name = request.entity.value

        for actor in attack.actors:
            if actor_name in actor.name:
                for technique in actor.techniques:
                    response += Technique(technique.name)
        return response