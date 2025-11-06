import os, sys, paramiko
from dotenv import load_dotenv

class SSHManager:
       def __init__(self, username, password):
            self.username = username
            self.password = password
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            pass
       
       def connect(self, hostname):
            try:
                 self.ssh_client.connect(hostname, 22, self.username, self.password)
            except Exception as e:
                 return f"an error has occured while trying to connect to the host: {e}"
        
       
       def execute_command(self, commands):
            try:
                stdin, stdout, stderr = self.ssh_client.exec_command("; ".join(commands))
                output = stdout.read.decode('utf-8')+stderr.read.decode('utf-8')
                exit_code = stdout.channel.recv_exit_status()
                return output, exit_code
            except Exception as e:
                 return f"the command didnt run successfully, {e}"
       
       def copy_file_to_remote(self, localfile, remotefile):
            sftp = self.ssh_client.open_sftp()
            sftp.put(localfile, remotefile)
            sftp.close()
       
       def copy_file_from_remote(self, remotefile, localfile):
            sftp = self.ssh_client.open_sftp()
            sftp.get(remotefile, localfile)
            sftp.close()
       
       def close(self):
            self.ssh_client.close()

def main():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    hostname = sys.argv[1] # I intentionally chose to get the hostname from the arguments; you’re free to use environment variables instead.
    

if __name__ == "__main__":
    main()