#!/usr/bin/env python
# ec2の情報を獲得
import boto3

if __name__ == '__main__':

   # EC2
   #ec2 = boto3.client('ec2', aws_access_key_id='', aws_secret_access_key='', region_name='ap-northeast-1')
   ec2 = boto3.client('ec2')
   ec2_list = ec2.describe_instances()
   #ec2_list = ec2.describe_instances(Filters=[{'Name':'network-interface.addresses.private-ip-address','Values':["172.31.17.104"]}])
   #print(ec2_list)

   for reservation in ec2_list['Reservations']:
      for instance in reservation['Instances']:
         tag_name = ""
         for tag in instance['Tags']:
            if tag['Key'] == 'Name':
               tag_name = tag['Value']

         print(tag_name, instance['InstanceType'], instance['State']['Name'])

   # VPC
   vpc_list = ec2.describe_vpcs()
   for vpc in vpc_list['Vpcs']:
      print(vpc['VpcId'], vpc['CidrBlock'])

   # RDS
   rds = boto3.client('rds')
   rds_list = rds.describe_db_instances()
   for db_instance in rds_list['DBInstances']:
      print(db_instance['DBInstanceIdentifier'], db_instance['Engine'])

   # S3
   s3 = boto3.client('s3')
   bucket_list = s3.list_buckets()
   for bucket in bucket_list['Buckets']:
      print(bucket['Name'], bucket['CreationDate'])

      bucket_data = s3.list_objects_v2(Bucket=bucket['Name'])
      for object in bucket_data['Contents']:
         print(object['Key'])



