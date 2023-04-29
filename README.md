# Super Spreader Attack and Mitigation

```
                   +--+
                   |h4|
                   ++-+
                    |
                    |
+--+      +--+     ++-+     +--+
|h1+------+s1+-----+s3+-----+h3|
+--+      +-++     +--+     +--+
            |
            |
          +-++
          |s2|
          +-++
            |
            |
          +-++
          |h2|
          +--+
```

## Introduction


The objective of this project is to provide an efficient and scalable solution for detecting and mitigating super spreader attacks in real-time using programmable switches. The project aims to implement a novel super spreader monitor that uses a Geometric-Min Filter, an adaptive sampling technique, to accurately measure flow spread without incurring high memory overhead or requiring duplicate removal. The project will also evaluate the performance of the system using real-world traffic traces and provide a codebase that can be easily integrated into existing network infrastructure. The end goal is to improve network security and reduce the risk of damage caused by super spreader attacks. 

The Github repository will contain the source code, documentation, and examples necessary to implement and deploy the system in a production environment.


## How to run

Provide required Permissions to the Working Directory:

```
chmod 777 /path/to/directory
```


Intiation of Topology in P4 Environment:

```
sudo p4run
```

Open two different Terminals of the Working Directory and execute the below commands:

```
sudo python sniff.py
```


```
sudo python digest.py
```
### Intiate the Attack
##### Assume that h1 is the attacker host and h2,h3 & h4 are the hosts which are attacked.
In the mininet prompt execute the below commands:

```
mininet> xterm h1
mininet> xterm h2
mininet> xterm h3
mininet> xterm h4
```

From node "h1":
``` 
python send.py python  3 10.0.2.2,10.0.3.3,10.0.3.4 32 100
```
From node "h2", "h3" & "h4":
``` 
python receive.py
```
### Now you can see that the attack can be demonstrated
