# Rclone_python
GUI to select .cmd that start rclone command and then parse the log

Before starting you should:
- save the choose_which_rclone_remote_to_sync.py and format_log.py in a folder
- create a folder "dry run cmd" and a folder "real run cmd"
- for each rclone remote you have, you should create a dry run cmd and a "real" run cmd. update the path to format_log.py (cf the example)
- move all the dry run cmd of all your remotes in a folder and all the real run cmd in another folder 
- create a folder to store the rclone log
- update the path in the in choose_which_rclone_remote_to_sync.py and format_log.py
