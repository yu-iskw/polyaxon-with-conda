# Anaconda with Polyaxon
This repository is to reproduce something wrong to upgrade a conda environment on polyaxon.

## How to run
```
# Create and initialize the project.
polyaxon project create --name "test-conda"
polyaxon init "test-conda"

# Run the testing experiment.
polyaxon run -u -f polyaxonfile.yml
```

## Log to build the docker image on polyaxon

```
ERROR 2019-02-01 20:53:58,973 build 1 139940430952256 Failed to create build job None

NoneType: None

Downloading file from http://polyaxon-polyaxon-api:80/api/v1/yu/test-conda/repo/download?commit=285558971ff4cd8c28fe21e8942c7906ebd392e6 using Internaltoken

Building: Step 1/8 : FROM continuumio/miniconda:4.5.11

Pushing ...

Building: ---> db6fb3419fc6

Building: Step 2/8 : ENV LC_ALL en_US.UTF-8

Building: ---> Using cache

Building: ---> 55740e08a00b

Building: Step 3/8 : ENV LANG en_US.UTF-8

Building: ---> Using cache

Building: ---> 5e40f199c393

Building: Step 4/8 : ENV LANGUAGE en_US.UTF-8

Building: ---> Using cache

Building: ---> b175677b9988

Building: Step 5/8 : ENV SHELL /bin/bash

Building: ---> Using cache

Building: ---> c4077ddb5f96

Building: Step 6/8 : WORKDIR /code

Building: ---> Using cache

Building: ---> a64f9071580b

Building: Step 7/8 : RUN conda env update -n base -f environment.yml

Building: ---> Running in 3b2eb4cf513c

Building: [91m

SpecNotFound: Invalid name, try the format: user/package

2019-02-01T20:53:58.973759556Z

[0m

Building: Removing intermediate container 3b2eb4cf513c

ERROR: The command '/bin/sh -c conda env update -n base -f environment.yml' returned a non-zero code: 1]]
```
