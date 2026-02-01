# capstone_sem2_major documentation!

## Description

Major assignment for seminar week 2 of capstone class. Cookiecutter template and S3 connection.

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://capstone-sessions-storage/data/`.
* `make sync_data_down` will use `aws s3 sync` to recursively sync files from `s3://capstone-sessions-storage/data/` to `data/`.


