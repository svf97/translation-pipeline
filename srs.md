# SRS

time-constrained and cost optimized solution

# steps to reproduce 

- OS: Ubuntu 20.0+
- create venv

## Language Detection

### TODO:
- [ ] trigger when user writes `review` for `movie`
- [ ] input = review + review_metadata 
- [x] deploy `seqtolang` docker image
- [ ] read `input` from S3 bucket
- [ ] batch trigger

## Language Translation

### TODO:
- [x] test `de` to `en`
- [x] test `fr` to `en`

## Sentiment Analysis

### TODO:
- [x] sentiment analysis for translated text

----

# AWS
### TODO:
 - [ ] AWS database
    - [ ] orig_review
    - [ ] {review_md: input json file}
    - [ ] lang_detected
    - [ ] sa_class
    - [ ] sa_score
 - [ ] constraints
    - [ ] batch mode
    - [ ] scalibility 
    - [ ] time limit [max time limit for 1000 predictions is 1.5 hours]


# to submit

- [ ] PDF Report 
   - [ ] cost estimation
- [ ] documentation 
   - [ ] readme
   - [ ] docstrings
- [ ] code


## criterea

- [ ] justified factors 
- [ ] how implemented system optimizes cost-driven time constraints
- [ ] code best practice