import fme
import fmeobjects
# Template Function interface:
# When using this function, make sure its name is set as the value of
# the 'Class or Function to Process Features' transformer parameter
def processFeature(feature):
    pass

# Template Class Interface:
# When using this class, make sure its name is set as the value of
# the 'Class or Function to Process Features' transformer parameter
class FeatureProcessor(object):
    def __init__(self):
        pass
    def input(self,feature):
        # formatar o campo turno
        if feature.getAttribute('TURNO') == 'D':
            feature.setAttribute('TURNO' , 'Diurno')
        else:
            feature.setAttribute('TURNO' , 'Noturno')
        
        # formatar o campo Lado_coletado
        if feature.getAttribute('LRS_REF_LADO') == 'A':
            feature.setAttribute('LADO COLETADO' , 'Ambos')
        elif feature.getAttribute('LRS_REF_LADO') == 'D':
            feature.setAttribute('LADO COLETADO' , 'Direito')
        elif feature.getAttribute('LRS_REF_LADO') == 'E':
            feature.setAttribute('LADO COLETADO' , 'Esquerdo')
        
        self.pyoutput(feature)
    def close(self):
        pass