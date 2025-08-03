#!/bin/bash

base_dir=$(dirname "$full_path")
cd "$base_dir"

# docker ps | grep nextcloud-1
sudo docker exec -it $(sudo docker ps --filter "name=docker-vscode-continue-ollama" --format "{{.ID}}") bash
# docker exec -it $(docker ps --filter "name=docker-nextcloud-demo-2025-nextcloud-1" --format "{{.ID}}") bash

