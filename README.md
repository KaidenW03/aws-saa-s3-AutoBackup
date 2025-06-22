# S3-Based Backup System

This project sets up an automated backup system using an EC2 instance and S3. A scheduled Bash script compresses system logs and uploads them to an S3 bucket. IAM roles ensure secure access, and S3 lifecycle rules control long-term storage costs.

## Technologies Used
- AWS EC2
- AWS S3
- AWS IAM
- Bash
- Cron

## What It Does
- Compresses log/config files (e.g., `/var/log`) into a timestamped archive
- Uploads archive to a designated S3 bucket
- Schedules daily backups via `cron`
- Uses IAM roles for secure S3 access
- Applies S3 lifecycle rules to archive/delete old backups

## Setup Instructions

1. Launch an EC2 instance (Amazon Linux 2 or Ubuntu).
2. Attach an IAM role with the permissions in `iam-role-policy.json`.
3. Create an S3 bucket and enable versioning (optional).
4. Copy `backup-to-s3.sh` to your instance and make it executable:
   ```bash
   chmod +x backup-to-s3.sh

## Further Automation

For an alternative to the Bash script, this project includes `backup-to-s3.py` a Python-based backup script using `boto3`. It compresses the `/var/log` directory and uploads the archive to the configured S3 bucket. 

To run:
pip install boto3
chmod +x backup-to-s3.py
./backup-to-s3.py

This project also includes `cloudformation-template.yaml` file that automates:

Creating the S3 bucket with lifecycle rules

Launching an EC2 instance with the correct IAM role

Installing Python and setting up scheduled backups via cron