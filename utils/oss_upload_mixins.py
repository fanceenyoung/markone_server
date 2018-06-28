# -*- coding: utf-8 -*-
from django.conf import settings
import oss2

"""
oss更多操作参考https://help.aliyun.com/document_detail/32029.html?spm=a2c4g.11186623.6.699.4ykQj1
"""


class AliOssClient:
    def __init__(self, key_id, key_secret, endpoint, bucket_name, oss_dir=None):
        self.auth = oss2.Auth(key_id, key_secret)
        self.bucket = oss2.Bucket(self.auth, endpoint, bucket_name, enable_crc=False)

        self.bucket_name = bucket_name
        self.endpoint = endpoint
        self.oss_dir = oss_dir

    def upload_object_to_oss(self, file_name, file_path):
        remote_name = self.oss_dir + '/' + file_name
        result = oss2.resumable_upload(self.bucket, remote_name, file_path)
        if result.status == 200:
            return 'https://{}.{}/{}/{}'.format(self.bucket_name, self.endpoint, self.oss_dir, file_name)
        return ''


class AliOssClientFactory(object):
    @staticmethod
    def create_client():
        key_id = settings.OSS_KEY
        key_secret = settings.OSS_SECRET
        endpoint = settings.END_POINT
        bucket_name = settings.BUCKET_NAME
        oss_dir = settings.OSS_DIR

        client = AliOssClient(key_id, key_secret, endpoint, bucket_name, oss_dir)
        return client


def upload_file_to_oss(file_name, file_path):
    if not file_path or not file_name:
        return ''

    oss_cli = AliOssClientFactory().create_client()
    outside_url = oss_cli.upload_object_to_oss(file_path, file_name)

    return outside_url
