#Gui
import easygui

# rename file
import os

# start cmd
import subprocess

## var to customize
path_to_rlcone_cmd_dry_run = r"path to\rclone\cmd for dry_run\\"
path_to_rlcone_cmd_REAL_run = r"path to\rclone\cmd for REAL_run\\"

## ask if dry-run or real-run  + choose the cmd
continue_asking= True # need to  to go back to question if wrong cmd chosen in popup
while continue_asking:
	# dry_run vs real run
	dry_run_TvsF = easygui.ynbox('What do you want to do?', 'Dry_run vs real run', ('Dry Run', 'REAL RUN'))
	rootdirectory= path_to_rlcone_cmd_dry_run if dry_run_TvsF == True else path_to_rlcone_cmd_REAL_run
		
	#file choose to select rclone cmd 
	cmd_path = easygui.fileopenbox(msg=None, title=None, default=rootdirectory, filetypes=None, multiple=False)
	
	if cmd_path== None: # if choose file = cancel
		continue
	else:
		#confirm choice (with the choosen cmd name and the kind of run)
		cmd_name= os.path.basename(cmd_path)
		print(cmd_path)
		choice = 'Dry Run' if 'Dry' in cmd_name else 'REAL RUN'
		proceed_to_rclone = easygui.ynbox(f'Do a  **{choice}** on **{cmd_name}**?', 'Last check before run', ('Yes', 'No'))
		
		#if check = yes, then stop loop, otherwise start the while lopp again
		if proceed_to_rclone == True:
			continue_asking= False

## call cmd rclone
subprocess.call([cmd_path])   # subprocess.Popen(doesnt work)

