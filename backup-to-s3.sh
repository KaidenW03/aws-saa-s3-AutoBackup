# Make sure to run "chmod +x backup-to-s3.sh" before running this script

#!/bin/bash

# CONFIGURATION
BACKUP_SRC="/var/log"
BUCKET_NAME="Kaiden_Test_Bucket"
S3_PREFIX="backups"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
ARCHIVE_NAME="/tmp/log_backup_$TIMESTAMP.tar.gz"

# Create a compressed archive of the logs
tar -czf $ARCHIVE_NAME $BACKUP_SRC

# Upload to S3
aws s3 cp $ARCHIVE_NAME s3://$BUCKET_NAME/$S3_PREFIX/

# Optional: Output success message
echo "Backup $ARCHIVE_NAME uploaded to s3://$BUCKET_NAME/$S3_PREFIX/"

# Clean up temporary file
rm -f $ARCHIVE_NAME
