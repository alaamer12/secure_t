from fabric import Connection, task

@task
def list_files(c):
    result = c.run('ls', hide=True)
    print("Ran on {}: {}".format(c.host, result.stdout.strip()))

# Connect to the remote server using Paramiko directly
conn = Connection(host='your_server_ip', user='your_username', connect_kwargs={"password": "your_password"})

# Run the 'list_files' task on the remote server
list_files(conn)
