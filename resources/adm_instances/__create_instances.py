import boto3
from boto3.session import Session

class EC2_Instance():

    def __init__(self, id:str=None):
        self.__ec2 = boto3.client('ec2')
        self.__id = id
        while True:
            if(id != None):
                self.start_instance(self.__id)
            else:
                try:
                    response = self.__ec2.run_instances(
                        ImageId = 'ami-0866a3c8686eaeeba',
                        InstanceType = 't2.micro',
                        MaxCount = 1,
                        MinCount = 1,
                    )

                    self.__id = response['InstanceId']
                    return self
                except:None

    def get_client(self):
        return self.__ec2
    
    def get_instance_id(self):
        return self.__id

    def start_instance(self, id):
        try:
            self.__ec2.start_instances(InstanceIds = [self.__id,])
        except:None

    def delete_instance(self):
        raise EOFError()

    def read_all_instances(self):
        raise EOFError()

    def update_instance(self):
        raise EOFError()