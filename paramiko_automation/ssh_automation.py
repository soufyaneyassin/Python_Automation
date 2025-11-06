import paramiko




class SSHManager:
       def __init__(self, username, password):
            self.username = username
            self.password = password
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            pass
       
       def connect(self, hostname):
            pass
       
       def execute_command(self, command):
            pass
       
       def copy_file_to_remote(self, localfile, remotefile):
            pass
       
       def copy_file_from_remote(self, remotefile, localfile):
            pass

def main():
    pass

if __name__ == "__main__":
    main()