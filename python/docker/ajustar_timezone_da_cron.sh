#!/bin/bash
echo "America/Recife" > /etc/timezone
export TZ='America/Recife'
service cron restart

