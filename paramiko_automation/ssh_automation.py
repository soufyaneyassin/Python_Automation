import os, sys
from ssh_manager import SSHManager
from dotenv import load_dotenv
from pathlib import Path


def main():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    hostname = sys.argv[1] # I intentionally chose to get the hostname from the arguments; you’re free to use environment variables instead.
    sshmanager = SSHManager(username, password)
    local_ssh_file = Path("ssh_scripts/test.sh")
    remote_ssh_file = "test.sh"
    log_file = "test_paramiko.log"
    cmds = ["chmod +x test.sh", "./test.sh"]
    try:
        sshmanager.connect(hostname)
        sshmanager.copy_file_to_remote(local_ssh_file, remote_ssh_file)
        output, exit_code = sshmanager.execute_command(cmds)
        if(exit_code):
             print("command didnt run successfully")
        else:
             print("command run successfully")
        print(output)
        sshmanager.copy_file_from_remote(log_file, log_file)            
    except Exception as e:
         print(f"something went wrong: {e}")
    finally:
         sshmanager.close()

if __name__ == "__main__":
    main()