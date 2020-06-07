#!/bin/bash
suffix=$(date +%Y-%m-%d_%H-%M-%S)
oldName=wow.db
newName=wow_${suffix}.db
cp ${oldName} ${newName}
gdrive upload --parent "your_google_drive_folder_key" ${newName}
rm ${newName}