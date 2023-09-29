#!/bin/bash

#curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash


docker build -t streamlit .
docker run -p 8501:8501 streamlit

