# Legged-Robots
This repository contains papers, videos and other references in the field of legged robots. 

-------------------

## Papers
### Legged Robots, ICRA 2023 
#### [[List of all ICRA 2023 papers](https://docs.google.com/spreadsheets/d/1LcYjqrh8EyZ4HIeSl80ECF-rb7tND6DTdUj2p5XA2gM/edit?usp=sharing)]
#### Learning for locomotion
1. DribbleBot: Dynamic Legged Manipulation in the wild: *Yandong Ji, Gabriel Margolis, Pulkit Agrawal* \
[[Paper](https://arxiv.org/pdf/2304.01159.pdf)][[Video](https://www.youtube.com/watch?v=1cek5Ypa3TE)][[Code](https://github.com/Improbable-AI/dribblebot)]
2. DreamWaQ: Learning Robust Quadrupedal Locomotion with Implicit Terrain Imagination Via Deep Reinforcement Learning \
[[Paper](https://arxiv.org/pdf/2301.10602.pdf)][[Video](https://www.youtube.com/watch?v=J5wl0be5KQM)][[Website](https://sites.google.com/view/dreamwaq)]
3. Learning Low-Frequency Motion Control for Robust and Dynamic Robot Locomotion \
[[Paper](https://arxiv.org/pdf/2209.14887.pdf)][[Video](https://www.youtube.com/watch?v=pSuX223zLvM)][[Website](https://ori-drs.github.io/lfmc/)]
4. OPT-Mimic: Imitation of Optimized Trajectories for Dynamic Quadruped Behaviors \
[[Paper](https://arxiv.org/pdf/2210.01247.pdf)][[Video](https://www.youtube.com/watch?v=tDzu_sy_FAI)][[Website](https://www.cs.ubc.ca/~van/papers/2022-opt-mimic/index.html)]
5. Learning to Walk by Steering: Perceptive Quadrupedal Locomotion in Dynamic Environments \
[[Paper](https://arxiv.org/pdf/2209.09233.pdf)][[Video](https://www.youtube.com/watch?v=_BvLqx3wAxI)][[Website](https://ut-austin-rpl.github.io/PRELUDE/)][[Code](https://github.com/UT-Austin-RPL/PRELUDE)]
6. Legs As Manipulator: Pushing Quadrupedal Agility Beyond Locomotion : *Deepak Pathak, CMU* \
[[Paper](https://robot-skills.github.io/resources/legmanip.pdf)][[Video](https://www.youtube.com/watch?v=d3YCmkEC7V0)][[Website](https://robot-skills.github.io/)]
7. Force Control for Robust Quadruped Locomotion: A Linear Policy Approach: *Stoch Lab, IISc* \
[[Paper: will be updated soon]()][[Video](https://www.youtube.com/watch?v=k89QdImcqdo&t=2s)][[Website](https://www.stochlab.com/projects/LinPolForceControlQuad.html)]
8. Advanced Skills through Multiple Adversarial Motion Priors in Reinforcement Learning: *Marco Hutter, ETH Zurich* \
[[Paper](https://arxiv.org/pdf/2203.14912.pdf)][[Video](https://www.youtube.com/watch?v=kEdr0ARq48A)]
9. Deep Reinforcement Learning Based Personalized Locomotion Planning for Lower-Limb Exoskeletons
10. Expanding Versatility of Agile Locomotion through Policy Transitions Using Latent State Representation
11. Sim-To-Real Transfer for Quadrupedal Locomotion Via Terrain Transformer
12. Agile and Versatile Robot Locomotion Via Kernel-Based Residual Learning

#### Design of Mechanisms
1. Meta Reinforcement Learning for Optimal Design of Legged Robots: *ETH Zurich, Marco Hutter* \
[[Paper](https://arxiv.org/pdf/2210.02750.pdf)]

#### Navigation and planning of Quadruped Robots
1. GPF-BG: A Hierarchical Vision-Based Planning Framework for Safe Quadrupedal Navigation: *LiDAR Lab, GaTech* [[Paper](https://lab-idar.gatech.edu/wp-content/uploads/2023/02/pubQuadNav-ICRA-2023.pdf)][[Video](https://www.youtube.com/watch?v=avUnefrbhY8)]

--------

### Control

#### Optimization Based control for legged robots:
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

### Mechanical Design
#### Design Principles and design of robots:
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

-------------------------

## Patents
1. **Boston Dynamics**: [List of Patents from Boston Dynamics](https://www.bostondynamics.com/patents)
2. **Boston Dynamics**: [Screw Actuator for Legged Robots](https://patents.google.com/patent/US10253855B2/en)
3. **Boston Dynamics**: [WO2018112097 - TRANSMISSION WITH INTEGRATED OVERLOAD PROTECTION FOR A LEGGED ROBOT](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2018112097)

------

## Good Robot designs:
1. [MIT Mini Cheetah, MIT](https://build-its.blogspot.com/2019/12/the-mini-cheetah-robot.html)
2. [Tiktok, Humanoid, Cornell University](http://ruina.tam.cornell.edu/research/topics/locomotion_and_robotics/Tik-Tok/) 
3. [Stanford Doggo, Stanford University (Click here then scroll down for designs)](https://github.com/Nate711/StanfordDoggoProject)

-------

## Video Lectures: 
### Optimization
1. [Introduction to Trajectory Optimization: Matthew Kelly](https://www.youtube.com/watch?v=wlkRYMVUZTs)
2. [Crash-Course on Non-Linear Programming (Optimization): MathPod YouTube channel](https://www.youtube.com/playlist?list=PLLtQL9wSL16hTHWFHPxMkMVPUGIZNhhHP)

### Reinforcement Learning
1. [Deep RL Bootcamp](https://sites.google.com/view/deep-rl-bootcamp/lectures)
2. [Reinforcement Learning: David Silver](https://www.youtube.com/playlist?list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-)
3. [CS-285: Deep Reinforcement Learning, UC Berkeley](http://rail.eecs.berkeley.edu/deeprlcourse/)

### ROS
1. [ROS Wiki Tutorials: Muhammad Luqman](https://www.youtube.com/playlist?list=PLBbhfIdh4NdgBBkX7q0Y3UukO2_ZoICee)

### Mechanical Design and Theory
1. [Kinematics of Mechanisms and Machines: NPTEL, IIT KGP](https://www.youtube.com/playlist?list=PLbRMhDVUMngdCkMipemSKP_dCgZLLfOe8)
      1. [Lec-37: Gear Kinematics](https://www.youtube.com/watch?v=BjkxYZ93Fbs&list=PLbRMhDVUMngdCkMipemSKP_dCgZLLfOe8&index=38) 
      2. [Lec-38: Gear Trains I](https://www.youtube.com/watch?v=lu_Qw4Y4XRQ&list=PLbRMhDVUMngdCkMipemSKP_dCgZLLfOe8&index=39)
      3. [Lec-39: Gear Trains II](https://www.youtube.com/watch?v=5f3wBlRY8dQ&list=PLbRMhDVUMngdCkMipemSKP_dCgZLLfOe8&index=40)
      4. [Lec-40: Gear Trains III](https://www.youtube.com/watch?v=-aHRWEXB3h4&list=PLbRMhDVUMngdCkMipemSKP_dCgZLLfOe8&index=41)
-------

## Useful articles:

### Software installations:
1. [Installing Anaconda on Ubuntu 22.04](https://linuxhint.com/install-anaconda-ubuntu-22-04/)
2. [Installing Anaconda on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart)

### Technical topics:
1. [DDP](http://www.imgeorgiev.com/2023-02-01-ddp/): A good read for DDP
2. [Policy Gradient Algorithms](https://lilianweng.github.io/posts/2018-04-08-policy-gradient/#what-is-policy-gradient): A good read for Policy Gradient Algos
3. [Reinforcement Learning Resources](https://stable-baselines.readthedocs.io/en/master/guide/rl.html): A list of resources for studying Reinforcement Learning

### Study:
1. [Paper Study Tips](https://github.com/IvLabs/ResearchPaperNotes/tree/master/literature_study_tips)
2. [List of Science & Math courses with video lectures](https://github.com/Developer-Y/math-science-video-lectures)
3. [How to read a paper: Linkedin Post](https://www.linkedin.com/feed/update/urn:li:activity:7044621048364900352?utm_source=share&utm_medium=member_desktop)

### Know your scientist:
1. [Steven LaValle](http://lavalle.pl/bio.html): A motivating story of the man who gave the RRT algorithm for motion planning, in his own words

--------------

## Interesting Github Repositories

1. [loco-3d/crocoddyl:](https://github.com/loco-3d/crocoddyl)
Crocoddyl is an optimal control library for robot control under contact sequence. Its solver is based on various efficient Differential Dynamic Programming (DDP)-like algorithms

---------------

## Websites of Labs working in Legged robotics:

1. [**Biomimetics Robotics Lab**: Sangbae Kim, MIT, USA](https://biomimetics.mit.edu/)
2. [**DRDC Lab**: Hae-Won Park, KAIST, South Korea](https://www.dynamicrobot.kaist.ac.kr/)
3. [**Robo Design Lab**: Joao Ramos, UIUC, USA](https://publish.illinois.edu/robodesign/)
4. [**Stochastic Robotics Lab**: Shishir N Y, IISc Bengaluru, India](https://www.stochlab.com/)
5. [**Robotic Systems Lab**: Marco Hutter, ETH Zurich, Switzerland](https://rsl.ethz.ch/)
6. [**Sony Quadruped Research**:](https://www.sony.com/en/SonyInfo/research/technologies/new_mobility/)
7. [**LIDAR, Laboratory of Intelligent Decision and Autonomous systems, GaTech:** Ye Zhao](https://lab-idar.gatech.edu/) 
