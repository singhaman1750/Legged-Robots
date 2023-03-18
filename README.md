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

### Mechanical Design:
1. **MIT, Design Principles**: [Design principles for highly efficient quadrupeds and implementation on the MIT Cheetah robot](https://ieeexplore.ieee.org/document/6631038)
1. **KAIST, Actuator Design**: [DRPD, Dual Reduction Ratio Planetary Drive for Articulated Robot Actuators](https://ieeexplore.ieee.org/abstract/document/9981201)
2. **KAIST, HOUND design**: [Design of KAIST HOUND, a Quadruped Robot Platform for Fast and Efficient Locomotion with Mixed-Integer Nonlinear Optimization of a Gear Train](https://ieeexplore.ieee.org/abstract/document/9811755)
3. **UIUC, Panther**: [Design and experimental implementation of a quasi-direct-drive leg for optimized jumping](https://ieeexplore.ieee.org/document/8202172)
3. **UIUC, Tello Leg**: [Tello Leg: The Study of Design Principles and Metrics for Dynamic Humanoid Robots](https://ieeexplore.ieee.org/document/9813569)
4. **UIUC, Tello Leg**: [The dynamic effect of mechanical losses of transmissions on the equation of motion of legged robots](https://arxiv.org/abs/2106.01842)
5. **AMI, IIT, Italy, egroCub Humanoid**: [Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting](https://arxiv.org/abs/2211.13503)
6. **ETH Zurich, ANYmal**: [Vitruvio: An Open-Source Leg Design Optimization Toolbox for Walking Robots](https://ieeexplore.ieee.org/document/9157985)
7. **Co-design(CACTO)**: [Exploring the Limits of a Redundant Actuation System Through Co-Design](https://ieeexplore.ieee.org/document/9400808)

## Patents: 
1. **Boston Dynamics**: [List of Patents from Boston Dynamics](https://www.bostondynamics.com/patents)
2. **Boston Dynamics**: [Screw Actuator for Legged Robots](https://patents.google.com/patent/US10253855B2/en)

## Video Lectures: 
1. [Introduction to Trajectory Optimization: Matthew Kelly](https://www.youtube.com/watch?v=wlkRYMVUZTs)
2. [Reinforcement Learning: David Silver](https://www.youtube.com/playlist?list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-)

## Useful articles:

### Software installations:
1. [Installing Anaconda on Ubuntu 22.04](https://linuxhint.com/install-anaconda-ubuntu-22-04/)
2. [Installing Anaconda on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart)

### Algos:
1. [DDP](http://www.imgeorgiev.com/2023-02-01-ddp/): A good read for DDP

### Study:
1. [Paper Study Tips](https://github.com/IvLabs/ResearchPaperNotes/tree/master/literature_study_tips)
2. [List of Science & Math courses with video lectures](https://github.com/Developer-Y/math-science-video-lectures)

## Interesting Github Repositories

1. [loco-3d/crocoddyl:](https://github.com/loco-3d/crocoddyl)
Crocoddyl is an optimal control library for robot control under contact sequence. Its solver is based on various efficient Differential Dynamic Programming (DDP)-like algorithms

## Websites of Labs working in Legged robotics:

1. [**Biomimetics Robotics Lab**: Sangbae Kim, MIT, USA](https://biomimetics.mit.edu/)
2. [**DRDC Lab**: Hae-Won Park, KAIST, South Korea](https://www.dynamicrobot.kaist.ac.kr/)
3. [**Robo Design Lab**: Joao Ramos, UIUC, USA](https://publish.illinois.edu/robodesign/)
