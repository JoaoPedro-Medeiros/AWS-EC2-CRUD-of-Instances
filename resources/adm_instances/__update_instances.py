import boto3
from __create_instances import EC2_Instance

class EC2_Update_Instance(EC2_Instance):
    def __init__(self, id):
        super().__init__(id)

    def atualizar_tipo_instancia(self, novo_tipo):
        try:
            # Parar a instância antes de modificar
            print(f"Parando a instância {self.__id}...")
            self.__ec2.stop_instances(InstanceIds=[self.__id])
            waiter = self.__ec2.get_waiter('instance_stopped')
            waiter.wait(InstanceIds=[self.__id])
            print(f"Instância {self.__id} parada.")

            # Modificar o tipo da instância
            print(f"Modificando o tipo da instância {self.__id} para {novo_tipo}...")
            self.__ec2.modify_instance_attribute(
                InstanceId=self.__id,
                InstanceType={'Value': novo_tipo}
            )
            print(f"Tipo da instância {self.__id} modificado para {novo_tipo}.")

            # Iniciar a instância novamente
            print(f"Iniciando a instância {self.__id}...")
            self.__ec2.start_instances(InstanceIds=[self.__id])
            print(f"Instância {self.__id} iniciada com sucesso.")
            
            return True
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar a instância {self.__id}: {str(e)}")
            return False
