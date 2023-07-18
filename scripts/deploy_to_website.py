import os
from ftplib import FTP
from config import FTP_USERNAME, FTP_PASSWORD

def upload_folder_to_ftp(source_folder, destination_folder, ftp_host):
	# Connect to the FTP server
	ftp = FTP(ftp_host)
	ftp.login(FTP_USERNAME, FTP_PASSWORD)

	# Change to the destination folder on the FTP server
	ftp.cwd(destination_folder)

	# Recursively upload each file and subfolder from the source folder
	for item in os.listdir(source_folder):
		item_path = os.path.join(source_folder, item)
		if os.path.isfile(item_path):
			print("FILE:", item_path)
			with open(item_path, 'rb') as file:
				ftp.storbinary(f'STOR {item}', file, None)
		elif os.path.isdir(item_path):
			print("DIR:", item_path)
			if item not in ftp.nlst():
				ftp.mkd(item)
			ftp.cwd(item)
			upload_folder_to_ftp(item_path, '.', ftp_host)
			ftp.cwd('..')

	# Disconnect from the FTP server
	ftp.quit()
	

# Usage example
source_folder = 'build'
destination_folder = '/domains/blackdragonsoftware.be/public_html'
ftp_host = 'ftp.blackdragonsoftware.be'

upload_folder_to_ftp(source_folder, destination_folder, ftp_host)