#!/bin/bash

certificate_name="certificate.pem"
openssl req -x509 -newkey rsa:4096 -nodes -out ${certificate_name} -keyout privatekey.pem -days 60
sudo cp ./${certificate_name} /usr/local/share/ca-certificates
sudo update-ca-certificates
