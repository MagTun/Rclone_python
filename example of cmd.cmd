rclone sync --dry-run  "C:\Users\user\rclone folder" "remote name":"rclone folder appdata" --log-file "C:\Users\user\Desktop\zzLogRsync\rclone folder.log"  --log-level INFO --delete-after --copy-links --exclude "desktop.ini"  --drive-skip-gdocs
start "" "REPLACE\HERE\PATH TO format_log_rclone.py"
REM This will make the remote drive (google drive) identical to the local folder
