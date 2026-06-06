#!/bin/bash

# sync_gdrive_prompts.sh
# A script to synchronize AI prompt engineering documents from Google Drive to the local repository.
#
# Prerequisite: You must have a tool like 'gdrive' or 'rclone' installed and configured,
# OR use the Google Drive API via curl.
#
# This script provides templates for both 'gdrive' (CLI) and 'rclone'.

LOCAL_FOLDER="./docs/prompt-engineering/google-drive"
mkdir -p "$LOCAL_FOLDER"

# --- OPTION 1: Using 'gdrive' CLI ---
# Install: https://github.com/glotlabs/gdrive
# CONFIG: Run 'gdrive account add' first.
GDRIVE_FOLDER_ID="YOUR_GOOGLE_DRIVE_FOLDER_ID_HERE"

sync_with_gdrive() {
    echo "Syncing using gdrive CLI..."
    # Note: gdrive sync is often a paid/complex feature, using download as alternative
    # gdrive files download --recursive "$GDRIVE_FOLDER_ID" --path "$LOCAL_FOLDER"
    echo "Please configure GDRIVE_FOLDER_ID and uncomment the download command in the script."
}

# --- OPTION 2: Using 'rclone' (Recommended) ---
# Install: https://rclone.org/
# CONFIG: Run 'rclone config' and name your remote 'gdrive'.
RCLONE_REMOTE="gdrive:AI-Prompts"

sync_with_rclone() {
    echo "Syncing using rclone..."
    if command -v rclone &> /dev/null; then
        rclone sync "$RCLONE_REMOTE" "$LOCAL_FOLDER" --progress
    else
        echo "Error: rclone is not installed."
    fi
}

# --- OPTION 3: Using Google Drive API via curl ---
# Requires a valid OAuth2 Access Token.
ACCESS_TOKEN="YOUR_ACCESS_TOKEN_HERE"

sync_with_curl() {
    echo "Syncing using curl and Google Drive API..."
    # Example: List files in a specific folder
    # curl -H "Authorization: Bearer $ACCESS_TOKEN" \
    #      "https://www.googleapis.com/drive/v3/files?q='${GDRIVE_FOLDER_ID}'+in+parents"
    echo "Manual sync required via API. See script for example curl command."
}

# MAIN EXECUTION
echo "Google Drive Prompt Sync"
echo "========================="

# Uncomment the method you want to use:
# sync_with_rclone
# sync_with_gdrive
# sync_with_curl

echo "Synchronization complete (simulated). Update scripts/sync_gdrive_prompts.sh with your credentials."
