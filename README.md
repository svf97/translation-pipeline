# Pipeline for user review translation and sentiment analysis

Assuming user review and its metadata are stored in [AWS S3](), the script translates user review based on detected `{language: [fra, deu]}`, applies sentiment analysis to translated text and calculates score. 

Data is then stored in AWS database, ?

## Setting Environment

**Pre-requisites**

- Python 3+
- pip3 
- [awscli](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-prereq)
- [download aws batch helpers](https://github.com/awslabs/aws-batch-helpers/archive/master.zip)


- create virtual environment & install requirements

```
$ git clone repo
$ cd repo
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt 
```

- Install [docker](https://docs.docker.com/engine/install/ubuntu/)
- Install `seqtolang` from source

```
$ git clone https://github.com/hiredscorelabs/seqtolang
$ cd seqtolang
$ python setup.py install
```

- Verify installation in terminal

```
$ sudo docker build . -t seqtolang
$ sudo docker run -e SEQTOLANG_TEXT="Good boy in chinese is 好孩子" seqtolang
```

- install [huggingface](https://github.com/huggingface/transformers#installation) transformer and its prerequisites

### todo:

- dockerize python solution 
