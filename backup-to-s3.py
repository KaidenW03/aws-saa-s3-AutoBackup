# Make sure to run "chmod +x backup-to-s3.py" before running this script

#!/usr/bin/env python3

import boto3
import tarfile
import os
import datetime
import subprocess

# Configuration
backup_src = "/var/log"
bucket_name = "Kaiden_Test_Bucket"
s3_prefix = "backups"
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
archive_name = f"/tmp/log_backup_{timestamp}.tar.gz"

# Create archive
with tarfile.open(archive_name, "w:gz") as tar:
    tar.add(backup_src, arcname=os.path.basename(backup_src))

# Upload to S3
s3 = boto3.client("s3")
s3.upload_file(archive_name, bucket_name, f"{s3_prefix}/log_backup_{timestamp}.tar.gz")

print(f"Backup uploaded to s3://{bucket_name}/{s3_prefix}/log_backup_{timestamp}.tar.gz")

# Remove temp file
os.remove(archive_name)
