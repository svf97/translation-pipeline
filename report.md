# Pipleline for user review translation and sentiment analysis

## Software Requirements Specifications

[SRS can be found here](https://github.com/svf97/translation-pipline/blob/main/srs.md)

## Solution Presented

The solution presented fulfils the requirement of deploying a Python-based program on AWS, provided that the architecture is cost-efficient, time-constrained and follows best practices. 


### AWS

**AWS Batch + Spot Instances**


Note: All images below are screenshots from these

- [Reference](https://www.youtube.com/watch?v=Wrg8XvU6qqI)
- [Reference](https://aws.amazon.com/blogs/compute/creating-a-simple-fetch-and-run-aws-batch-job/#:~:text=AWS%20Batch%20executes%20jobs%20as,script%20and%20run%20your%20job.)

**What is AWS Batch?**

![img](https://user-images.githubusercontent.com/60857664/140624011-5d2a1acb-46f2-4ac8-b457-08a675ac2315.png)



**2. AWS Batch Job Architecture**

![img](https://user-images.githubusercontent.com/60857664/140624009-733706c2-1520-4951-ab2f-f40b34d45c7a.png)


**3. Why Spot Instances?**

- uses spare EC2 capacity that is available for less than the On-Demand price
- batch allocation stategy includes spot capacity optimized, which allows AWS to find available capacity pools, and launch instances accordingly
-  suitable for a hybrid compute environment such that if on-demand resource's threshold is met, scaling would shift towards using spot instances, which in turn will scale as per requirements without much worry on the cost. 

![img](https://user-images.githubusercontent.com/60857664/140624022-004137cf-f985-49f6-804c-4d2cac69ec9a.png)

- **spot interruptions:** 
    - though spot interuptions may seem riskier at first, statistics show less than 5% of spot instance were interrupted in a span of 3 months

    ![img](https://user-images.githubusercontent.com/60857664/140627554-0224d61a-d67b-40d0-94c7-cf300d83bd6b.png)  

    - ECS agent in spot instances trigger a 2 minute notice prior to interruptions if the resources are required, however this is handled by:
        -  monitoring spot instances for notices, which should drain instance containers and stop scheduling any jobs to that instance
        - allowing flexibility in terms of subnets and instance types leads to an increased combination of spot instance across resources




**Best Practice Methodology**

- Key steps:

    - [ ] Build a Docker image with the fetch & run script
    - [ ] Create an Amazon ECR repository for the image
    - [ ] Push the built image to ECR
    - [ ] Create a simple job script and upload it to S3
    - [ ] Create an IAM role to be used by jobs to access S3
    - [ ] Create a job definition that uses the built image
    - [ ] Submit and run a job that execute the job script from S3

The figure below shows the idea architecture for the solution, which is mainly to have a script that fetches jobs to run from S3, batch processess the data, and have the ready data written to a DB.


![img](https://user-images.githubusercontent.com/60857664/140627570-7b90b61a-77fb-4ead-b55b-7150c968189b.png)

----

- create EC2 template and enable spot interruption handling

![img](https://user-images.githubusercontent.com/60857664/140624043-01af41ad-2728-4610-9640-6cc568f867da.png)

- job retries enabled

- **Handling Spot Interruption:** 

    Advanced Settings > User Data >
    `echo "ECS_ENABLE_SPOT_INSTANCE _DRAINING=true" >> /etc/ecs/ecs.config` 


- AWS Batch > create 
    - compute environment
        - ![img](https://user-images.githubusercontent.com/60857664/140624045-46d54d14-5fa4-479a-af35-9f1f6172c59c.png)
        - ![img](https://user-images.githubusercontent.com/60857664/140624046-843fdf25-4298-403c-92ae-36a85bcb35a4.png)
    - job queue
    - job definition
    - jobs


### Python

[Source code and documentation can be found here](README.md)
