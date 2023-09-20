### Problem: 

In developing countries we have a problem and that is over population. Whosoever reading and writing this are also part of this/ responsible for this blunder. Okay, lets come to the point now. 

In over populated cities we have a lot of car. As long as it stays in the garage, all good. As soon as it hit the road, we have traffic jam. Also, we have another problem related to car is parking. Sometimes, this is the reason for the traffic jam too. So, in here we will discuss problem specific to the urban parking.

Sometime, people park the car besides the road and go for their work and since we as a common people does not have access to public data of contact information, we suffer a lot. We just need to simply wait and suffer.

Here we are going to build/discuss a solution which will give the facility to inform the car owner without revealing any parties identity(more specifically, contact information). 

### Solution:

Here we are going to build the backend which will give the facility to connect to car owner by any person, who is facing the problem. 

Now lets jump on to the product that we are going to build. As of now we only have idea of v1 and v2.

![User Diagram](https://i.imgur.com/PlRrUuG.png)

##

#### v1
***owner***

1. Register their vehicle using the mobile number(Assuming the same mobile number is the driver of that vehicle).
2. Considering one owner could be having more than 1 car. For each car there will be one QR code.

***scanner***

1. If a scanner(person who scan it) scan the QR code, then he/she will get connected to the car owner.

#### v2:

Location and DND, these will be implemented here.


##
**We are going to publish few API's which will get consumed by UI**

    1. To register the User
    2. To register the car in the app
    3. To generate QR code
    4. To connect to the car owner


We need to make the codebase of this product more readable, reliable and maintainable so that, whoever touches the codebase and read about a function, it should not take more than 3 minutes.

We are using TDD - First we will write the tests for a functionality or feature and then we will write the code.



