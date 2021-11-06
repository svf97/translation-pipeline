# Pipleline for user review translation and sentiment analysis

## Software Requirements Specifications

[SRS can be found here](srs.md)

## Solution Presented

The solution presented fulfils the requirement of deploying a Python-based program on AWS, provided that the architecture is cost-efficient, time-constrained and follows best practices. 


### AWS

**AWS Batch + Spot Instances**

Reference: https://www.youtube.com/watch?v=Wrg8XvU6qqI

Note: All images below are screenshots from the reference mentioned above. 

**What is AWS Batch?**

![img](https://user-images.githubusercontent.com/60857664/140624011-5d2a1acb-46f2-4ac8-b457-08a675ac2315.png)



**2. AWS Batch Job Architecture**

![img](https://user-images.githubusercontent.com/60857664/140624009-733706c2-1520-4951-ab2f-f40b34d45c7a.png)


**3. Why Spot Instances?**

- uses spare EC2 capacity that is available for less than the On-Demand price
- batch allocation stategy includes spot capacity optimized, which allows AWS to find available capacity pools, and launch instances accordingly
-  suitable for a hybrid compute environment such that if on-demand resource's threshold is met, scaling would shift towards using spot instances, which in turn will scale as per requirements without much worry on the cost. 

![img](https://user-images.githubusercontent.com/60857664/140624022-004137cf-f985-49f6-804c-4d2cac69ec9a.png)

- **spot interruptions:** ECS agent in spot instances trigger a 2 minute notice prior to interruptions if the resources are required, however this is handled by:
    -  monitoring spot instances for notices, which should drain instance containers and stop scheduling any jobs to that instance
    - allowing flexibility in terms of subnets and instance types leads to an increased combination of spot instance across resources



**Best Practice Methodology**

- create EC2 template with the following options:

![img](https://user-images.githubusercontent.com/60857664/140624043-01af41ad-2728-4610-9640-6cc568f867da.png)

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