import os, sys, SSHManager
from dotenv import load_dotenv



def main():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    hostname = sys.argv[1] # I intentionally chose to get the hostname from the arguments; you’re free to use environment variables instead.
    sshmanager = SSHManager(username, password)
    cmds = ["whoami"]
    try:
        sshmanager.connect(hostname)
        output, exit_code = sshmanager.execute_command(cmds)
        if(exit_code):
             print("command didnt run successfully")
        else:
             print("command run successfully")
        print(output)              
    except Exception as e:
         print(f"something went wrong: {e}")
    finally:
         sshmanager.close()

if __name__ == "__main__":
    main()