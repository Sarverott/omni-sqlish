import docker

client = docker.from_env()




print(client.containers.list())


print(client.containers.run("omnisqlish", "echo hello world"))