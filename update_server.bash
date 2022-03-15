#!/bin/bash
sudo supervisorctl stop server_app
git pull
sudo supervisorctl start server_app
