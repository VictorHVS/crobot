from pytrustnfe.certificado import Certificado
from pytrustnfe.nfe import consulta_distribuicao_nfe, xml_consulta_distribuicao_nfe

certificado = open("/path/certificado.pfx", "r").read()
certificado = Certificado(certificado, 'senha_pfx')