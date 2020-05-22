#!/usr/bin/env python
from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.ml import Personalize
from diagrams.aws.analytics import KinesisDataStreams, KinesisDataFirehose, Athena, Quicksight, Glue
from diagrams.onprem.client import Client
from diagrams.aws.storage import S3

with Diagram('イベントストリーミング'):
    # インスタンス化によってノードを作成
    # ノードにラベルを付与でき、\nを入れることでラベルの改行も可能
    stream = KinesisDataStreams('Kinesis\nData Streams')
    s3 = S3('S3')
    athena = Athena('Athena')

    # 定義したノードを始点とした流れを作成
    # 変数に代入せずとも、ノードは作成可能
    Client() >> stream >> Lambda('Lambda') >> Personalize('Personalize\nEventTracker')
    stream >> KinesisDataFirehose('Kinesis\nData Firehose') >> s3
    s3 - athena >> Quicksight('QuickSight') << Client()
    s3 >> Glue('Glue') >> athena