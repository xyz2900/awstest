#!/usr/bin/env python
# cloudwatchのデータを獲得
import boto3

if __name__ == '__main__':
   logs = boto3.client('logs')
   log_list = logs.describe_log_groups()
   print(log_list)