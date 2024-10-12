from .__create_instances import EC2_Instance
from resources.adm_instances.keys.key import *
import boto3

class EC2_Delete_Instance(EC2_Instance):

    def __init__(self, id):
        self.__ec2 = boto3.client('ec2')
        self.__id = id

    def delete(self):
        if DELETE_KEY == 'DELETE_NOW':
            self.__ec2.stop_instances(InstanceIds=[self.__id,])