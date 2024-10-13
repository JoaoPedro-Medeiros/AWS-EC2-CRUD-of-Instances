from resources.adm_instances.keys.key import *
import boto3

class EC2_Read_Instance:
    def __init__(self):
        super().__init__()
    
    def read_all_instances(self):
        try:
            response = self.__ec2.describe_instances()
            instancias = []
            for reserva in response['Reservations']:
                for instancia in reserva['Instances']:
                    instancias.append({
                        'IdInstancia': instancia['InstanceId'],
                        'TipoInstancia': instancia['InstanceType'],
                        'Estado': instancia['State']['Name'],
                        'EnderecoIpPublico': instancia.get('PublicIpAddress', 'N/A'),
                        'EnderecoIpPrivado': instancia.get('PrivateIpAddress', 'N/A'),
                    })
            return instancias
        except Exception as e:
            print(f"Ocorreu um erro ao listar as instâncias: {str(e)}")
            return None