# hello-devops

_Please read these instructions carefully._

There are 2 applications in this project:

* **hello-python** is a web page that contains a form; when the form is submitted, hello-python enqueues the message on a RabbitMQ queue.

* **hello-node** is a worker that consumes the RabbitMQ queue and stores any message on a MySQL database.

There's also a `create_database.sql` script, to help you prepare the MySQL database.

Each application contains a short README file with more information.

## Problem

**Deploy this entire stack** in a way that _any message entered on the hello-python form is stored on a MySQL database by hello-node_.

* **There are a few bugs in the code**, and you'll need to fix them to solve this exercise; you should not require any specific knowledge of either Python or NodeJS to solve these issues.

* If you need to make any changes to help you debugging (such as adding logs or catching exceptions) we suggest you keep them so we can understand your thought proccess.

* If you have some knowledge of Python or NodeJS development, feel free to implement or suggest _simple_ improvements to the applications to make them production-ready.

## Solutions

We'll accept _any_ of the following types of solution:

* A script using a CLI, SDK, API or library that deploys the stack on a host running a modern Linux distribution _or_ on the AWS cloud.

* A Docker Compose file _or_ another similar container orchestration solution that deploys the stack on a host running a modern Linux distribution _or_ on the AWS cloud.

* A recipe using one or more configuration management tools (e.g. Terraform, Ansible, Chef, Puppet, CloudFormation, Vagrant, Packer, etc.) that deploys the stack on a host running a modern Linux distribution _or_ on the AWS cloud.

**Important:** please **edit this README file** with step-by-step instructions on _how_ to deploy using your solution. Feel free to also include a short paragraph and/or a diagram explaining your solution.

## Expectations

When assessing this exercise, we will take the following points into consideration:

* Whether the solution works or not
* How _easy_ it is to deploy the solution
* How _resilient_ it is (e.g. if the database takes a few more seconds to start than usual, does the system stop working and never recovers?)

Suppose that a _junior_ developer (who has access to most common Linux distributions and an AWS account) will try to run your solution. Would he be able to install all requirements and run it easily? Would he be able to verify that it works? Should any problems arise (e.g. a package is missing), would he be able to identify and fix it?

We don't expect a production-grade solution, but we expect you to show that you'd be able to deploy a production-grade distributed system given enough tools and time.

## Submissions

You should send us a [git patch](https://git-scm.com/docs/git-format-patch) file with your solution. To do so follow these steps:

1.  Clone (do NOT fork) this repository to your machine:

        $ git clone https://github.com/quintoandar/hello-devops.git

2.  Implement your solution and comit your changes locally:

        $ git commit -am "My solution"

3.  Create a patch file for this repository:

        $ git format-patch origin/master --stdout > result.patch

4.  Email us the `result.patch` file.

Please do **not** fork this repository and do **not** publish your solution online!

## Contact

Feel free to reach out if you have any questions! Also, we expect this problem to take some hours at most, but please do get in touch if you need more time to provide a good solution! It is far better than delivering something that does not work :)

## Installation Instructions:
### Pre-requisites:
- **Docker** and **docker-compose** should be available on the machine which you are going to install the application. <br> Docker and docker-compose installation can be verified by `docker -v` and  `docker-compose -v` command respectively. 

```
root@symus-linux:/home/symus/test# docker -v
Docker version 17.06.2-ee-19, build e56aa2d
```
```
root@symus-linux:/home/symus/test# docker-compose -v
docker-compose version 1.17.1, build 6d101fb
```

*Follow below official documentations to install docker and docker-compose if those are not already present:*
- **Docker:** https://docs.docker.com/install/linux/docker-ce/ubuntu/
- **Docker-Compose:** https://docs.docker.com/compose/install/

### Installation Steps:

*_All the docker, docker-compose commands should be run as root user_*

- Clone the git repo to the machine where the application is going to run (can be clonned in any folder. For Ex: /home/symus): <br>
  `git clone https://github.com/quintoandar/hello-devops`
 - Execute below commands from the directory (for ex: /home/symus) you executed the above command: <br>
    `cd hello-devops` - to change to the working directory <br>
    `docker-compose up` - to create builds and start containers
    
### Installation verification steps:
- Verify the installation by executing below `docker ps` command - it should return 4 containers running with the names:
    - `hello_python_producer`
    - `hello_node_consumer`
    - `rabbitmq`
    - `mysql-host`
    
    If one of the above containers are not running or not started - debug why it got failed and that can be done with the command `docker logs <container-id>`
    `container-id` can be copied with `docker ps -a | grep <container_name_as_mentioned_above>` command
    
    For Ex: 
     - `docker ps -a | grep hello_python_producer`
     - `docker logs 9faa3f52d2f5`

### Application access:
- Enter - `http://www.<hostname>:5001` to get started with the application
- login to `mysql-host` container with the command - <br> `docker exec -it mysql-host bash` --> to check if the database is updated with the message which is added from the above URL.
    - execute `mysql -u <username> -p<password>` inside the container. `username - root, password - root`
    - change the database with this command - `use hello`
    - select the messages table to see the messages - `select * from Messages;`
	
	For Example:
    ```
    root@symus-linux:/home/symus# docker exec -it mysql-host bash
    root@mysql_container:/# mysql -u root -proot
    mysql> use hello;
    Database changed
    mysql> select * from Messages;
    +----+---------+
    | ID | message |
    +----+---------+
    |  1 | first   |
    |  2 | second  |
    +----+---------+
    2 rows in set (0.00 sec)
    mysql>
    ```
    
- You can also check the messaging queue here - `http://www.<hostname>:15672/#/queues` - `username/password - guest/guest`

## Improvements:
 - more meaningfull logs can be added to producer and consumer apps, so that can be checked a the time of any failures or for any informations
 - Application can be more secured (https://)

*Any other queries?? contact - syedmustafa.net@gmail.com*
