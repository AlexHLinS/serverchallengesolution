#!/bin/bash
sudo supervisorctl stop server
git pull
sudo supervisorctl start server
