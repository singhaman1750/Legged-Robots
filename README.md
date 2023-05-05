# Legged-Robots
This repository contains papers, videos and other references in the field of legged robots. 

## Papers
### Control: 
#### Optimization Based control for legged robots

1. **Survey Paper**: [Optimization-Based Control for Dynamic Legged Robots](https://arxiv.org/abs/2211.11644)
2. **Convex MPC**: [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](https://ieeexplore.ieee.org/document/8594448)
3. **Feedback MPC**: [Feedback MPC for Torque-Controlled Legged Robots](https://arxiv.org/abs/1905.06144)
4. **RF-MPC**: [Representation-Free Model Predictive Control for Dynamic Motions in Quadrupeds](https://arxiv.org/abs/2012.10002)\
      a. Github Code link: [YanranDing/RF-MPC](https://github.com/YanranDing/RF-MPC)
5. **Motion Imitation**: [Learning Agile Robotic Locomotion Skills by Imitating Animals](https://arxiv.org/abs/2004.00784)\
      a. Github Code link: [erwincoumans/motion_imitation](https://github.com/erwincoumans/motion_imitation)
6. **Non-Linear RF-MPC**:[Real-Time Constrained Nonlinear Model Predictive Control on SO(3) or Dynamic Legged Locomotion](http://ras.papercept.net/images/temp/IROS/files/2325.pdf)
7. **WBC+MPC**: [Highly Dynamic Quadruped Locomotion via Whole-Body Impulse Control and Model Predictive Control](https://arxiv.org/abs/1909.06586)

#### Optimization problem solving:
1. **Contact-implicit DDP**: [Contact-Implicit Differential Dynamic Programming for Model Predictive Control with Relaxed Complementarity Constraints](https://ieeexplore.ieee.org/document/9981476)
2. **RPC on MIT Cheetah-3**: [Implementing Regularized Predictive Control for Simultaneous Real-Time Footstep and Ground Reaction Force Optimization](https://ieeexplore.ieee.org/document/8968031)
3. **CACTO**: [CACTO: Continuous Actor-Critic with Trajectory Optimization -- Towards global optimality](https://arxiv.org/abs/2211.06625#:~:text=CACTO%3A%20Continuous%20Actor%2DCritic%20with%20Trajectory%20Optimization%20%2D%2D%20Towards%20global%20optimality,-Gianluigi%20Grandesso%2C%20Gastone&text=Abstract%3A%20This%20paper%20presents%20a,RL)

#### Barrier Functions:
1. **AMBER Lab, CalTech**: [Risk-Averse Control via CVaR Barrier Functions: Application to Bipedal Robot Locomotion](https://ieeexplore.ieee.org/document/9447796)
2. **MIT Humanoid**: [Humanoid Self-Collision Avoidance Using Whole-Body Control with Control Barrier Functions](https://arxiv.org/abs/2207.00692)

--------

### Mechanical Design:
1. **MIT, Design Principles**: [Design principles for highly efficient quadrupeds and implementation on the MIT Cheetah robot](https://ieeexplore.ieee.org/document/6631038)
2. **UIUC, Panther**: [Design and experimental implementation of a quasi-direct-drive leg for optimized jumping](https://ieeexplore.ieee.org/document/8202172)
3. **UIUC, Tello Leg**: [Tello Leg: The Study of Design Principles and Metrics for Dynamic Humanoid Robots](https://ieeexplore.ieee.org/document/9813569)
4. **UIUC, Tello Leg**: [The dynamic effect of mechanical losses of transmissions on the equation of motion of legged robots](https://arxiv.org/abs/2106.01842)
5. **AMI, IIT, Italy, egroCub Humanoid**: [Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting](https://arxiv.org/abs/2211.13503)
6. **ETH Zurich, ANYmal**: [Vitruvio: An Open-Source Leg Design Optimization Toolbox for Walking Robots](https://ieeexplore.ieee.org/document/9157985)
7. **Co-design(CACTO)**: [Exploring the Limits of a Redundant Actuation System Through Co-Design](https://ieeexplore.ieee.org/document/9400808)
8. **Tachyon, Sony**: [Tachyon: Design and Control of High Payload, Robust, and Dynamic Quadruped Robot with Series-Parallel Elastic Actuators](https://ieeexplore.ieee.org/document/9636196)

#### Actuator Designs:
1. **KAIST, Actuator Design**: [DRPD, Dual Reduction Ratio Planetary Drive for Articulated Robot Actuators](https://ieeexplore.ieee.org/abstract/document/9981201)
2. **KAIST, HOUND design**: [Design of KAIST HOUND, a Quadruped Robot Platform for Fast and Efficient Locomotion with Mixed-Integer Nonlinear Optimization of a Gear Train](https://ieeexplore.ieee.org/abstract/document/9811755)
3. **Dual Motor Design (2021)**: [Explosive Electric Actuator and Control for Legged Robots](https://reader.elsevier.com/reader/sd/pii/S2095809921005282?token=528592F31700C12282D3918FF7D6AC7D58F2B05BE168CEA0767BE07971464D4F37986B7E089D0A53D6F9E87E12E5AB73&originRegion=eu-west-1&originCreation=20230413064751)
4. **John Harry Bell, Master's Thesis, MIT (2018)**: [A Two-Motor Actuator for Legged Robotics Applications](https://dspace.mit.edu/bitstream/handle/1721.1/127152/1191839946-MIT.pdf?sequence=1&isAllowed=y)
8. **Robotics and Multibody Mechanics Research Group (R&MM), Belgium (2017)**: [Modeling and design of an energy-efficient dual-motor actuation unit with a
planetary differential and holding brakes](https://reader.elsevier.com/reader/sd/pii/S0957415817301812?token=FAB5BDB0EADAEA7F8CA91AD6F2AB31755882038340745DCBB9D1AB5AA3D244E6B66C7BE60CC0D6E7334D1A3368EB0343&originRegion=eu-west-1&originCreation=20230413064458)
7. **Alexandre Girard's paper, Hamburg, Germany IROS(2015)**: [A Two-Speed Actuator for Robotics with Fast Seamless Gear Shifting](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7354047)
6. **Hoyul Lee's Paper, ASME/IEEE Transactions on mechatronics(2012)**: [A New Actuator System Using Dual-Motors and a Planetary Gear](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6022796)
5. **Jung Jun Park' paper, ASME/IEEE Transactions on mechatronics(2010)**: [A Serial-Type Dual Actuator Unit With Planetary Gear Train: Basic Design and Applications](https://dspace.mit.edu/bitstream/handle/1721.1/127152/1191839946-MIT.pdf?sequence=1&isAllowed=y)

## Patents: 
1. **Boston Dynamics**: [List of Patents from Boston Dynamics](https://www.bostondynamics.com/patents)
2. **Boston Dynamics**: [Screw Actuator for Legged Robots](https://patents.google.com/patent/US10253855B2/en)
3. **Boston Dynamics**: [WO2018112097 - TRANSMISSION WITH INTEGRATED OVERLOAD PROTECTION FOR A LEGGED ROBOT](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2018112097)

-------

## Video Lectures: 
1. [Introduction to Trajectory Optimization: Matthew Kelly](https://www.youtube.com/watch?v=wlkRYMVUZTs)
2. [Reinforcement Learning: David Silver](https://www.youtube.com/playlist?list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-)
3. [ROS Wiki Tutorials: Muhammad Luqman](https://www.youtube.com/playlist?list=PLBbhfIdh4NdgBBkX7q0Y3UukO2_ZoICee)

-------

## Useful articles:

### Software installations:
1. [Installing Anaconda on Ubuntu 22.04](https://linuxhint.com/install-anaconda-ubuntu-22-04/)
2. [Installing Anaconda on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart)

### Technical topics:
1. [DDP](http://www.imgeorgiev.com/2023-02-01-ddp/): A good read for DDP
2. [Policy Gradient Algorithms](https://lilianweng.github.io/posts/2018-04-08-policy-gradient/#what-is-policy-gradient): A good read for Policy Gradient Algos

### Study:
1. [Paper Study Tips](https://github.com/IvLabs/ResearchPaperNotes/tree/master/literature_study_tips)
2. [List of Science & Math courses with video lectures](https://github.com/Developer-Y/math-science-video-lectures)
3. [How to read a paper: Linkedin Post](https://www.linkedin.com/feed/update/urn:li:activity:7044621048364900352?utm_source=share&utm_medium=member_desktop)

### Know your scientist:
1. [Steven LaValle](http://lavalle.pl/bio.html): A motivating story of the man who gave the RRT algorithm for motion planning, in his own words

## Interesting Github Repositories

1. [loco-3d/crocoddyl:](https://github.com/loco-3d/crocoddyl)
Crocoddyl is an optimal control library for robot control under contact sequence. Its solver is based on various efficient Differential Dynamic Programming (DDP)-like algorithms

## Websites of Labs working in Legged robotics:

1. [**Biomimetics Robotics Lab**: Sangbae Kim, MIT, USA](https://biomimetics.mit.edu/)
2. [**DRDC Lab**: Hae-Won Park, KAIST, South Korea](https://www.dynamicrobot.kaist.ac.kr/)
3. [**Robo Design Lab**: Joao Ramos, UIUC, USA](https://publish.illinois.edu/robodesign/)
4. [**Stochastic Robotics Lab**: Shishir N Y, IISc Bengaluru, India](https://www.stochlab.com/)
5. [**Robotic Systems Lab**: Marco Hutter, ETH Zurich, Switzerland](https://rsl.ethz.ch/)
6. [**Sony Quadruped Research**:](https://www.sony.com/en/SonyInfo/research/technologies/new_mobility/)
