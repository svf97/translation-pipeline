# assement-requirement

migrate ML pipelines from development into production

# steps to reproduce

- OS: Ubuntu 20.0+
- create venv

## Language Detection

### TODO:
- [ ] trigger when user writes `review` for `movie`
- [ ] input = review + review_metadata 
- [x] deploy `seqtolang` docker image
- [ ] read `input` from S3 bucket

------

- Install [docker](https://docs.docker.com/engine/install/ubuntu/)
- Install `seqtolang` from source

```
$ git clone https://github.com/hiredscorelabs/seqtolang
$ cd seqtolang
$ python setup.py install
```

- Verify installation in terminal

```
$ docker build . -t seqtolang
$ docker run -e SEQTOLANG_TEXT="Good boy in chinese is 好孩子" seqtolang
```

## Language Translation

### TODO:

----

- [Install from pip](https://github.com/huggingface/transformers#installation)