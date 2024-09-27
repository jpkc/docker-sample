# Docker Sample

This is a docker sample developed by João Pedro Kerr Catunda to demostrate docker functionality.

This sample uses a text sentiment analysys model provided by DataScientest and was developed with Docker Compose V2 version v2.24.0.

You can bring it up with the following docker command line:

```
docker compose up
```

# Requirements

To run this you will need:

1. docker 
	debian linux: apt-get install docker (double check)
	gentoo linux: emerge --ask app-containers/docker
	osx:
	windows:
	
2. docker compose
	debian linux: apt-get install docker-compose (double check)
	gentoo linux: emerge --ask app-containers/docker-compose
	osx:
	windows:

# Architecture

This sample uses an image provided by DataScientest with the current configuration:
- Two phrase mood evaluation models named V1 and V2

- Three users credentials with different model permissions:
	user		password		Available Models
	alice		wonderland		V1, V2
	bob		builder			V1
	clementine	mandarine

- The following API
	Authenticate
	Athorize
	Evaluate

# Files

Files:
```
    .
    ├── AUTHENTICATION_IMAGE
    │   ├── AUTHENTICATION_TEST.py
    │   ├── Dockerfile
    │   └── setup.sh
    ├── AUTHORIZATION_IMAGE
    │   ├── AUTHORIZATION_TEST.py
    │   ├── Dockerfile
    │   └── setup.sh
    ├── BASE_ENV_IMAGE
    │   ├── Dockerfile
    │   └── setup.sh
    ├── CONTENT_IMAGE
    │   ├── CONTENT_TEST.py
    │   ├── Dockerfile
    │   └── setup.sh
    ├── docker-compose.yml
    ├── README.txt
    ├── setup_environment.sh
    ├── start_compose.sh
    └── start_containers.sh

4 directories, 16 files
```

# Usage

How to use this example:

1. Run setup_environment.sh to create the required images and prepare the environment.
2. Run ``start_compose.sh`` according to ``docker-compose.yml`` architecture. **Alternatively** you can run ``start_containers.sh`` to get things started manually.


After running ``setup.sh`` a ``SHARED_STORAGE`` folder will be created.
This folder will be used as a storage device shared between containers so that they can all log activity in the same ``api_test.log`` file.

The ``api_test.log`` file will be populated **if** the LOG env variable is set to "1".
You can set this with the ``-e LOG="1"`` parameter like
```
docker run ... -e LOG="1" ...
```
as seen on the ``start_containers.sh`` script.
You can also specify it like
```
environment:
    LOG: 1
```
As seen in the ``docker-compose.yml`` file.

# Goal: Create a toy CI/CD pipeline to test an API

API entry points:
	/docs				# Detailed description of the entry points.
	/status 			# returns 1 if the API is running
	/permissions 		# returns a user's permissions: See which version of the template the user have access to. Identified by a username and a password.
	/v1/sentiment		# returns the sentiment analysis using an old model
	/v2/sentiment		# returns the sentiment analysis using a new template

# Tests:

-Authentication:
	In this first test, we are going to check that the identification logic works well.
	To do this, we will need to make GET requests on the /permissions entry point.
	We know that two users exist alice and bob and their passwords are wonderland and builder.
	We'll try a 3rd test with a password that doesn't work: clementine and mandarine.

-Authorization:
	In this second test, we will verify that our user authorization logic is working properly.
	We know that bob only has access to v1 while alice has access to both versions.
	For each of the users, we will make a query on the /v1/sentiment and /v2/sentiment entry
	points: we must then provide the arguments username, password and sentence which contains
	the sentence to be analyzed.

-Content:
	In this last test, we check that the API works as it should. We will test the following
	sentences with the alice account:
		-Life is beautiful
		-That sucks
	For each version of the model, we should get a positive score for the first sentence and
	a negative score for the second sentence. The test will consist in checking the positivity
	or negativity of the score.

