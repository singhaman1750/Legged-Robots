# Legged-Robots
A curated collection of papers, videos, tools, and references for legged robotics (actuators, control, design).

---

## Table of Contents
- [Start Here](#start-here)
- [1) Full Conference Paper Lists](#1-full-conference-paper-lists)
- [2) Curated Papers by Topic](#2-curated-papers-by-topic)
  - [2.1 Actuators & Transmissions](#21-actuators--transmissions)
  - [2.2 Legged Robot Control](#22-legged-robot-control)
  - [2.3 Legged Robot Mechanical Design & Co-Design](#23-legged-robot-mechanical-design--co-design)
- [3) Hands-on Resources](#3-hands-on-resources)
- [4) Ecosystem](#4-ecosystem)
- [5) Buying Hardware & Parts](#5-buying-hardware--parts)
- [Star History](#star-history)

---

## Start Here
Use this repo as a quick index depending on what you are currently working on:

| If you are… | Go to | What you’ll find |
|---|---|---|
| **New to legged robotics** | **2.3 Mechanical Design & Co-Design** + **3) Hands-on Resources → YouTube Projects / Videos** | *Design Principles* + key *Quadruped/Humanoid design papers* + beginner-friendly quadruped build videos|
| **Working on actuators** | **2.1 Actuators & Transmissions** | *Planetary / Cycloidal* + *Non-conventional actuators* + *Motor theory & dyno/testing* |
| **Working on control or RL** | **2.2 Legged Robot Control** | *Model-based control* + *Learning-based locomotion* |
| **Looking for implementations / code / builds** | **3) Hands-on Resources** | YouTube builds + GitHub repos + workshops + lectures |
| **Looking for people / labs / companies** | **4) Ecosystem** | Professors & labs + conferences/journals + companies |
| **Buying parts for a build** | **5) Buying Hardware & Parts** | Motors + drivers + stators + magnets + manufacturing tools |

---

> **Note:** Click the small triangle next to each section (▶) to expand the detailed list.

---

## 1) Full Conference Paper Lists

<details><summary><b>ICRA</b></summary>
  
  1. **ICRA 2025:** [[Github](https://github.com/DoongLi/ICRA2025-Paper-List)]
  2. **ICRA 2024:** [[Github](https://github.com/ryanbgriffiths/ICRA2024PaperList)] / [[Google Sheet](https://docs.google.com/spreadsheets/d/1z1IK0fxNZBEF7IiWZhM7TdK5dvNUvwnj3KwO5u0B91o/edit?gid=1438356197#gid=1438356197)] / [[Offcial IEEE List](https://ieeexplore.ieee.org/xpl/conhome/10609961/proceeding)]
  3. **ICRA 2023:** [[Google sheet](https://docs.google.com/spreadsheets/d/1LcYjqrh8EyZ4HIeSl80ECF-rb7tND6DTdUj2p5XA2gM/edit?usp=sharing)]
</details>

<details><summary><b>IROS</b></summary>

1. **IROS 2025:** [[Official IEEE List](https://ieeexplore.ieee.org/xpl/conhome/11245651/proceeding)]
2. **IROS 2024:** [[Offcial IEEE List](https://ieeexplore.ieee.org/xpl/conhome/10801246/proceeding)]
3. **IROS 2023:** [[Google sheet](https://docs.google.com/spreadsheets/d/1cdca2J4g2gmHym1J0nXxJabhsxK7xIfXxicB8Le6AwU/edit#gid=214014586)] / [[Github Repo](https://github.com/ryanbgriffiths/IROS2023PaperList)] / [[Offcial IEEE List](https://ieeexplore.ieee.org/xpl/conhome/10341341/proceeding)]
</details>

<details><summary><b>Humanoids</b></summary>

1. **Humanoids 2025**: [[Official IEEE List](https://ieeexplore.ieee.org/xpl/conhome/11202977/proceeding)]
</details>

**[Paper Copilot](https://papercopilot.com/)**: A centralized tool for accessing conference paper lists and related statistics, all in one place.

---

## 2) Curated Papers by Topic

### 2.1 Actuators & Transmissions

<details>
  <summary><b>Planetary Gearboxes</b></summary>

  1. **MIT Mini Cheetah Actuator**: *Mini Cheetah: A Platform for Pushing the Limits of Dynamic Quadruped Control* [[Paper](https://ieeexplore.ieee.org/document/8793865)] [[Blog](https://build-its.blogspot.com/2019/12/the-mini-cheetah-robot.html)]
  2. **MIT Humanoid Actuator (Alex Hattori, Thesis)**: *Design of a High Torque Density Modular Actuator for Dynamic Robots* [[Thesis-Webpage](https://dspace.mit.edu/handle/1721.1/127165?show=full)]
  3. **MIT Humanoid Actuator (Paper)**: *Design and Development of the MIT Humanoid: A Dynamic and Robust Research Platform* [[Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10375199)]
  4. **Berkeley Humanoid**: *Berkeley Humanoid: A Research Platform for Learning-based Control* [[Paper](https://arxiv.org/abs/2407.21781)]
  5. **Quasi-Direct Drive Actuator (ICRA 2024)**: *Design and Experimental Characterisation of a Novel Quasi-Direct Drive Actuator for Highly Dynamic Robotic Applications* [[Paper](https://ieeexplore.ieee.org/document/10611567)]
  6. **3D-Printed Open-Source Actuators (EmBiR Lab, Univ. of Michigan)**: *Design and Characterization of 3D Printed, Open-Source Actuators for Legged Locomotion* [[Paper](https://ieeexplore.ieee.org/document/9981940)] [[Open-Source Designs](https://www.embirlab.com/3dpactuator)]

</details>

<details>
  <summary><b>Cycloidal Gearboxes</b></summary>

1. **Berkely Humanoid Lite**: *Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot* [[Paper](https://arxiv.org/abs/2504.17249)] [[Documentation](https://berkeley-humanoid-lite.gitbook.io/docs)] [[Github](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)]
2. **Wesley Roozing's Paper**: *Experimental comparison of pinwheel and non-pinwheel designs of 3D-printed cycloidal gearing for robotics* [[Paper](https://ieeexplore.ieee.org/abstract/document/10610250/)]
3. **RaM (Uni of Twente)**: *Anti-Backlash Mechanisms for Cycloidal Drive Robotic Actuators: Design and Evaluation* [[Paper](https://ieeexplore.ieee.org/abstract/document/11197911/)]

</details>

<details>
  <summary><b>Series Elastic Actuators (SEA)</b></summary>
  
1. **High-Performance Series Elastic Actuation**: Paine, Nicholas Arden: Thesis [[Thesis-PDf](https://sites.utexas.edu/hcrl/files/2016/01/nick-paine-thesis-dissertation-2014.pdf)] [[Thesis-webpage-link](https://repositories.lib.utexas.edu/items/383f9e7f-2213-4bca-bd46-3aabdee6fda5)]

</details>

<details><summary><b> Non-Conventional Actuators</b></summary>

1. **KAIST, Actuator Design**: DRPD, Dual Reduction Ratio Planetary Drive for Articulated Robot Actuators [[Paper](https://ieeexplore.ieee.org/abstract/document/9981201)]
2. **Dual Motor Design (2021)**: Explosive Electric Actuator and Control for Legged Robots [[Paper](https://reader.elsevier.com/reader/sd/pii/S2095809921005282?token=528592F31700C12282D3918FF7D6AC7D58F2B05BE168CEA0767BE07971464D4F37986B7E089D0A53D6F9E87E12E5AB73&originRegion=eu-west-1&originCreation=20230413064751)]
3. **John Harry Bell, Master's Thesis, MIT (2018)**: A Two-Motor Actuator for Legged Robotics Applications [[Thesis](https://dspace.mit.edu/bitstream/handle/1721.1/127152/1191839946-MIT.pdf?sequence=1&isAllowed=y)]
4. **Robotics and Multibody Mechanics Research Group (R&MM), Belgium (2017)**: Modeling and design of an energy-efficient dual-motor actuation unit with a
planetary differential and holding brakes [[Paper](https://reader.elsevier.com/reader/sd/pii/S0957415817301812?token=FAB5BDB0EADAEA7F8CA91AD6F2AB31755882038340745DCBB9D1AB5AA3D244E6B66C7BE60CC0D6E7334D1A3368EB0343&originRegion=eu-west-1&originCreation=20230413064458)]
5. **Alexandre Girard's paper, Hamburg, Germany IROS(2015)**: A Two-Speed Actuator for Robotics with Fast Seamless Gear Shifting [[Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7354047)]
6. **Hoyul Lee's Paper, ASME/IEEE Transactions on mechatronics(2012)**: A New Actuator System Using Dual-Motors and a Planetary Gear [[Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6022796)]
7. **Jung Jun Park' paper, ASME/IEEE Transactions on mechatronics(2010)**: A Serial-Type Dual Actuator Unit With Planetary Gear Train: Basic Design and Applications [[Paper](https://dspace.mit.edu/bitstream/handle/1721.1/127152/1191839946-MIT.pdf?sequence=1&isAllowed=y)]
8. **Brubotics VUB paper, IEEE Robotics and Automation Letters(2022)**: A Methodology for Designing a Lightweight and Energy-Efficient Kinematically Redundant Actuator [[Paper](https://ieeexplore.ieee.org/document/9834077)]

</details>

<details>
  <summary><b>Modelling actuator dynamics</b></summary>

</details>

<details><summary><b>Motor Theory & Dyno / Testing</b></summary>
  
#### Motor Theory and Design
1. Master's Thesis: James Mevey [[Thesis-Link](https://krex.k-state.edu/server/api/core/bitstreams/e3f7aa0b-4833-44e4-9ef0-af09f411baa1/content)]
2. Book, Brushless Permanent Magnet Motor Design, Dr. Duane Hanselman
3. Instructables Post: [[Link](https://www.instructables.com/Make-Your-Own-Miniature-Electric-Hub-Motor/)]
4. Source: Reddit Post: [[Need some guidance with BLDC motor design: Answer by alternativemax](https://www.reddit.com/r/Motors/comments/pmopwr/need_some_guidance_with_bldc_motor_design/)] 

#### Dynamometer: Actuator testing setup

1. Benjamin Katz, blog: [[Link1](https://build-its-inprogress.blogspot.com/2016/08/small-motor-dynamometer-beginnings.html)] [[Link2](https://build-its.blogspot.com/2019/12/motor-dynamometer.html)] [[Link3](https://build-its-inprogress.blogspot.com/2016/04/torque-ripple-characterization-and.html)] [[Link4](https://build-its-inprogress.blogspot.com/2016/10/motor-dyno-updates-first-tests.html)]
2. MJbots blog: [[Link](https://blog.mjbots.com/2020/08/19/initial-dynamometer-assembly/)]
3. The brushless zone: [[Link](https://brushless.zone/quantifying-a-motor-the-ipm-dyno/)]
4. Understanding a motor dynamometer setup, Adi Mehrotra: [[Link: PDF](https://evt.mit.edu/textbooks/Dynos_for_Dummies.pdf)]
5. Berkeley humanoid motor testing setup: \
      i. Paper Title: Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot 

#### Actuator Design: Blogs, Videos, twitter threads, posts, papers etc

1. 3D Printed QDD Robotic Actuator (MIT Mini Cheetah Clone) : By nachumtwersky [[Blog-Link](https://www.instructables.com/3D-Printed-QDD-Robotic-Actuator-MIT-Mini-Cheetah-C/)]

</details>

---

### 2.2 Legged Robot Control

<details><summary><b>Model based Control: Quadrupeds </b></summary>
  
1. **Survey Paper**: Optimization-Based Control for Dynamic Legged Robots [[Paper](https://arxiv.org/abs/2211.11644)]
2. **Convex MPC for Quadruped walking**: Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control [[Paper](https://ieeexplore.ieee.org/document/8594448)]
3. **Feedback MPC**: Feedback MPC for Torque-Controlled Legged Robots [[Paper](https://arxiv.org/abs/1905.06144)]
4. **RF-MPC**: Representation-Free Model Predictive Control for Dynamic Motions in Quadrupeds [[Paper](https://arxiv.org/abs/2012.10002)] [[Github](https://github.com/YanranDing/RF-MPC)]
5. **Motion Imitation**: Learning Agile Robotic Locomotion Skills by Imitating Animals [[Paper](https://arxiv.org/abs/2004.00784)] [[Github](https://github.com/erwincoumans/motion_imitation)]
6. **Non-Linear RF-MPC**: Real-Time Constrained Nonlinear Model Predictive Control on SO(3) or Dynamic Legged Locomotion [[Paper](http://ras.papercept.net/images/temp/IROS/files/2325.pdf)]
7. **WBC+MPC**: Highly Dynamic Quadruped Locomotion via Whole-Body Impulse Control and Model Predictive Control [[Paper](https://arxiv.org/abs/1909.06586)]

</details>

<details><summary><b>Learning Based Control: Quadrupeds</b></summary>

1. **RMA**: RMA: Rapid Motor Adaptation for Legged Robots [[Paper](https://www.roboticsproceedings.org/rss17/p011.pdf)]
2. **Walk These Ways**: Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior [[Paper](https://arxiv.org/abs/2212.03238)][[Github](https://github.com/Improbable-AI/walk-these-ways)]
3. **DreamWaQ**: DreamWaQ: Learning Robust Quadrupedal Locomotion with Implicit Terrain Imagination Via Deep Reinforcement Learning [[Paper](https://arxiv.org/pdf/2301.10602.pdf)][[Video](https://www.youtube.com/watch?v=J5wl0be5KQM)][[Website](https://sites.google.com/view/dreamwaq)]
4. **HIMloco**: Hybrid Internal Model: Learning Agile Legged Locomotion with Simulated Robot Response [[Paper](https://arxiv.org/abs/2312.11460)][[Github](https://github.com/OpenRobotLab/HIMLoco)]
5. **Tencent Robotics**: Lifelike Agility and Play on Quadrupedal Robots using Reinforcement Learning and Deep Pre-trained Models [[Paper](https://tencent-roboticsx.github.io/lifelike-agility-and-play/)][[Website](https://tencent-roboticsx.github.io/lifelike-agility-and-play/)][[Video](https://www.youtube.com/watch?v=ucucrLqT5dM)]
6. **Linear Policy**: Force Control for Robust Quadruped Locomotion: A Linear Policy Approach [[Paper](https://ieeexplore.ieee.org/document/10161080)][[Video](https://www.youtube.com/watch?v=k89QdImcqdo&t=2s)][[Website](https://www.stochlab.com/projects/LinPolForceControlQuad.html)]
7. **PIP-Loco**: Pip-Loco: A propioceptive Infinite Horizon Planning Framework for Quadrupedal Robot Locomotion [[Paper](https://arxiv.org/pdf/2409.09441)]

</details>

<details><summary><b>Learning based controls: Interesting behaivour in Quadrupeds</b></summary>

1.  **DribbleBot**: DribbleBot: Dynamic Legged Manipulation in the wild [[Paper](https://arxiv.org/pdf/2304.01159.pdf)][[Video](https://www.youtube.com/watch?v=1cek5Ypa3TE)][[Code](https://github.com/Improbable-AI/dribblebot)][[Notes](https://github.com/singhaman1750/Research-Paper-Notes/blob/main/README.md#dribblebot-dynamic-legged-manipulation-in-the-wild)]
2. Legs As Manipulator: Pushing Quadrupedal Agility Beyond Locomotion [[Paper](https://robot-skills.github.io/resources/legmanip.pdf)][[Video](https://www.youtube.com/watch?v=d3YCmkEC7V0)][[Website](https://robot-skills.github.io/)]

</details>

<details><summary><b>Learning based controls: Humanoids</b></summary>
  
1. Bi-Level Motion Imitation for Humanoid Robots [[Paper](https://openreview.net/forum?id=wH7Wv0nAm8)]

</details>

---

### 2.3 Legged Robot Mechanical Design & Co-Design
<details><summary><b>Design Principles for legged robots:</b></summary>
  
1. **MIT, Design Principles**: Design principles for highly efficient quadrupeds and implementation on the MIT Cheetah robot [[Paper](https://ieeexplore.ieee.org/document/6631038)]

</details>

<details><summary><b>Quadruped Robot Design Papers</b></summary>

1. **MIT Cheetah-3**: MIT Cheetah 3: Design and Control of a Robust, Dynamic Quadruped Robot [[Paper](https://ieeexplore.ieee.org/document/8593885)]
2. **MIT Mini Cheetah**: Mini Cheetah: A Platform for Pushing the Limits of Dynamic Quadruped Control [[Paper](https://ieeexplore.ieee.org/document/8793865)] [[Blog](https://build-its.blogspot.com/2019/12/the-mini-cheetah-robot.html)] [[Gear-width-Calc](https://drivetrainhub.com/notebooks/gears/strength/Chapter%202%20-%20Root%20Stress.html)]
3. **MIT Super Mini-Cheetah**: The MIT Super Mini Cheetah: A small, low-cost quadrupedal robot for dynamic locomotion [[Paper](https://ieeexplore.ieee.org/document/7443018)]
4. **ANYmal Robot**: ANYmal - A Highly Mobile and Dynamic Quadrupedal Robot [[Paper](https://ieeexplore.ieee.org/document/7758092)]
5. **KAIST, HOUND design**: Design of KAIST HOUND, a Quadruped Robot Platform for Fast and Efficient Locomotion with Mixed-Integer Nonlinear Optimization of a Gear Train [[Paper](https://ieeexplore.ieee.org/abstract/document/9811755)]
6. **Barry Robot**: Barry: A High-Payload and Agile Quadruped Robot [[Paper](https://ieeexplore.ieee.org/document/10246325)]
7. **UIUC, Panther**: Design and experimental implementation of a quasi-direct-drive leg for optimized jumping [[Paper](https://ieeexplore.ieee.org/document/8202172)]
8. **Stanford Doggo**: Stanford Doggo, an open source quasi-direct drive quadruped [[Paper](https://github.com/Nate711/StanfordDoggoProject)] [[Github](https://github.com/Nate711/StanfordDoggoProject)]
9. **Solo Robot**: An Open Torque-Controlled Modular Robot Architecture for Legged Locomotion Research [[Paper](https://ieeexplore.ieee.org/document/9015985)]
10. **MiniTaur**: Design Principles for a Family of Direct-Drive Legged Robots [[Paper](https://ieeexplore.ieee.org/document/7403902)]
11. **Stoch, IISc**: Design, Development and Experimental Realization of A Quadrupedal Research Platform: Stoch [[Paper](https://ieeexplore.ieee.org/document/8813480)]
12. **Tachyon, Sony**: Tachyon: Design and Control of High Payload, Robust, and Dynamic Quadruped Robot with Series-Parallel Elastic Actuators [[Paper](https://ieeexplore.ieee.org/document/9636196)]
13. **Raibo Robot, KAIST**: RaiBo: A versatile robo-dog that runs through a sandy beach at 3 meters per second [[News-Article](https://techxplore.com/news/2023-01-raibo-versatile-robo-dog-sandy-beach.html)] [[Video](https://www.youtube.com/watch?v=ATvFSwkneu4)]
14. **Stoch-3, IISc, Bengaluru**: A Chain-Driven, Sandwich-Legged Quadruped Robot: Design and Experimental Analysis [[Arxiv-Paper](https://arxiv.org/abs/2503.14255)][[Video](https://youtu.be/ygSMCPcFnP8?feature=shared)]
15. **PADWQ**: Design and Control of a Open-Source, Low Cost, 3D Printed Dynamic Quadruped Robot [[Paper](https://www.mdpi.com/2076-3417/11/9/3762)]

</details>

<details><summary><b>Humanoid Robot Design</b></summary>
  
1. **Berkely Humanoid**: Berkeley Humanoid: A Research Platform for Learning-based Control [[Paper](https://arxiv.org/abs/2407.21781)]
2. **MIT Humanoid**: Design and Development of the MIT Humanoid: A Dynamic and Robust Research Platform [[Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10375199)]
3. **UIUC, Tello Leg**: Tello Leg: The Study of Design Principles and Metrics for Dynamic Humanoid Robots [[Paper](https://ieeexplore.ieee.org/document/9813569)]
4. **UIUC, Tello Leg**: The dynamic effect of mechanical losses of transmissions on the equation of motion of legged robots [[Paper](https://arxiv.org/abs/2106.01842)]
5. **AMI, IIT, Italy, egroCub Humanoid**: Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting [[Paper](https://arxiv.org/abs/2211.13503)]
6. **Tiktok, Humanoid, Cornell University**: [[Website](http://ruina.tam.cornell.edu/research/topics/locomotion_and_robotics/Tik-Tok/)] 
  
</details>

<details><summary><b>Design Optimization and Co-design Optimization</b></summary>

1. Vitruvio: An Open-Source Leg Design Optimization Toolbox for Walking Robots [[Paper](https://ieeexplore.ieee.org/document/9157985)]
2. **Co-design(CACTO)**: Exploring the Limits of a Redundant Actuation System Through Co-Design [[Paper](https://ieeexplore.ieee.org/document/9400808)]
3. Meta Reinforcement Learning for Optimal Design of Legged Robots [[Paper](https://arxiv.org/pdf/2210.02750.pdf)]

</details>

<details><summary><b>Design Patents</b></summary>

1. **Boston Dynamics**: [List of Patents from Boston Dynamics](https://www.bostondynamics.com/patents)
2. **Boston Dynamics**: [Screw Actuator for Legged Robots](https://patents.google.com/patent/US10253855B2/en)
3. **Boston Dynamics**: [WO2018112097 - TRANSMISSION WITH INTEGRATED OVERLOAD PROTECTION FOR A LEGGED ROBOT](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2018112097)

</details>

-------------------------

## 3) Hands-on Resources
<details><summary><b>Youtube Project / Videos </b></summary>

#### Quadruped Robot projects

1. **Stanley** by AheadIO: [[Video-Link](https://youtu.be/tIJMQKBBDtc?si=kkgVG_2jDeyVNn2C)][[Video-link-2](https://youtu.be/UTWGk3VrvQk?si=cYK-9lprQ1rbC0Ra)]
2. **Open Robot Dog** by James Bruton: [[Video-Link](https://www.youtube.com/playlist?list=PLpwJoq86vov8uTgd8_WNgBHFpDYemO-OJ)]
3. **CARA** by Aaed Musa: [[Video-Link](https://youtu.be/8s9TjRz01fo?si=E9OzYa9STsJEYgQx)]
4. **Dingo** by Nathan Ferguson: [[Video-Link](https://youtu.be/8KntOIgzUjY?si=Kg7lPAJMX9Akev89)] 
5. **Quadruped** by Alex Hattori: \
   a. **Quadruped V1**: [[Video-Link](https://youtu.be/nnKyDTrJ9DU?si=2VWDTEgI9JMUquLo)] \
   b. **Quadruped v2, v3**: [[Video-Link](https://youtu.be/aI4PkDkCDtE?si=OZFdMZwN7z5gOt0S)]
6. **PuppyPi, MechDog** and **ROSpug** by Hiwonder: \
   a. **PuppyPi**: [[Video-Link](https://youtu.be/OKaEbnmZ0PU?si=oM8rGW1es4kvkIia)] \
   b. **ROSPug**: [[Video-Link](https://youtu.be/nuAXr-FJmu8?si=bSkaENYsn_IGidym)] \
   c. **MechDog**: [[Video-Link](https://youtu.be/c7XJqjFmjto?si=tONRx2X6TE-thURP)]
7. **Fully 3d-printed robot dog** by jorgefer88: [[Video-Link](https://youtu.be/nmkJ_TJag_k?si=OjbLeTcoi6nRsVwf)]
8. **NovaSM3** by Chris Locke: [[Video-Link](https://youtu.be/0YpnKmXtMKQ?si=SBpXyaCsK51mGO5T)]
9. **XGO-Mini**: [[Video-Link](https://youtu.be/ZYeSgKPc02M?si=sQOHm0S0N6sVicel)]

</details>

<details><summary><b>Useful GitHub Repositories</b></summary>

#### Control of quadruped robots

1. [motion_imitation:](https://github.com/erwincoumans/motion_imitation/tree/master)
   Useful for Quadruped robot simulation in Pybullet using SRB (single-rigid body) model (by Erwin Couman, creator of Pybullet)

2. [walk-these-ways:](https://github.com/Improbable-AI/walk-these-ways)
   Learning-based locomotion controller in Issac-gym simulator, with different gaits and height changes

3. [HIMLoco:](https://github.com/OpenRobotLab/HIMLoco)
   Learning-based locomotion controller for rough terrain navigation using hybrid internal models

#### Controls for Humanoids and Biped robots

1. [VI_discretized_TO:](https://github.com/DRCL-USC/VI_discretized_TO)
   Code for the Backflips of biped and quadruped robots using Traj_Opt using Variational Integration


#### Mechanical Design

1. [COMPAct:](https://github.com/singhaman1750/COMPAct-Actuator_design_framework.git)
A computational design optimization and automated CAD generation for 3D-printed actuators for legged robots

2. [Manim-Gearbox](https://github.com/GarryBGoode/manim-GearBox.git)
A gearbox visualizer tool build on Manim

#### Others

1. [loco-3d/crocoddyl:](https://github.com/loco-3d/crocoddyl)
   Crocoddyl is an optimal control library for robot control under contact sequence. Its solver is based on various efficient Differential Dynamic Programming (DDP)-like algorithms

2. [Pinocchio:](https://github.com/stack-of-tasks/pinocchio?tab=readme-ov-file#examples)
   Efficient and Versatile Rigid Body Dynamics Algorithms

</details>

<details><summary><b>Workshops</b></summary>

1. **ICRA 2024 Workshop on Co-design in Robotics: Theory, Practice, and Challenges**: [[Webpage](https://www.robotmechanisms.org/activities/icra-2024-codesign)]
2. **ICRA 2024 Advancements in Trajectory Optimisation and Model Predictive Control for Legged Systems**: [[Webpage](https://atompc-workshop.github.io/)]

</details>

<details><summary><b>Video Lectures</b></summary>

#### Robotics and Controls:
1. Robotics Fall 2023, by Pranav Bhounsule: [[Videos](https://youtube.com/playlist?list=PLc7bpbeTIk77plTksRXAe1JPJZVmBNk8_&feature=shared)][[Notes](https://pab47.github.io/robotics/robotics23.html)]

#### Topics in Mathematics 
1. [MIT 18.06 Linear Algebra, Spring 2005, MITOCW: Gilbert Strang](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8)

#### Optimization
1. **Course:** [Numerical Optimization, *(NPTEL)*: Shirish Sevade ](https://www.youtube.com/playlist?list=PLEAYkSg4uSQ3Hi2kc4n4bqJvxrtyaQa3P)

**Trajectory Optimization** 
1. **Video Lecture:** [Introduction to Trajectory Optimization: Matthew Kelly](https://www.youtube.com/watch?v=wlkRYMVUZTs)
3. **Video Lecture:** [Underactuated Robotics, Trajectory Optimization I: Lec 11, *Russ Tedrake*](https://www.youtube.com/watch?v=fY6gAo88Aa0)
4. **Video Lecture:** [Underactuated Robotics, Trajectory Optimization II: Lec 12, *Russ Tedrake*](https://www.youtube.com/watch?v=Mo9fTJmWAJY)
5. **Video Lecture:** [Optimization, Optimal Control, Trajectory Optimization, and Splines: Jesus Tordesillas](https://www.youtube.com/watch?v=j82Ia436DYY)
6. **Book:** Practical Methods for Optimal control and estimation using non-linear programming, John T. Betts
7. **Github Repos:** [Matthew Kelly's TrajOpt Repo](https://github.com/MatthewPeterKelly/OptimTraj)
8. **Github Repos:** [MindtPy Library Page: MINLP solver](https://pyomo.readthedocs.io/en/stable/contributed_packages/mindtpy.html)
9. **Tutorial Paper:** [An Introduction to Trajectory Optimization: How to do your own direct collocation, *Matthew Kelly*](https://www.matthewpeterkelly.com/research/MatthewKelly_IntroTrajectoryOptimization_SIAM_Review_2017.pdf)

#### Basics of Control systems
1. Linear Quadratic Regulator (LQR): [Basics/Overview](https://www.youtube.com/watch?v=1_UobILf3cc) [Derivation]()

#### Reinforcement Learning
1. [Deep RL Bootcamp](https://sites.google.com/view/deep-rl-bootcamp/lectures)
2. [Reinforcement Learning: David Silver](https://www.youtube.com/playlist?list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-)
3. [CS-285: Deep Reinforcement Learning, UC Berkeley](http://rail.eecs.berkeley.edu/deeprlcourse/)
4. [Spinning up*](https://spinningup.openai.com/en/latest/index.html): It's a blog but really useful

#### ROS
1. [ROS Wiki Tutorials: Muhammad Luqman](https://www.youtube.com/playlist?list=PLBbhfIdh4NdgBBkX7q0Y3UukO2_ZoICee)

#### Mechanical Design and Theory
1. [Kinematics of Mechanisms and Machines: NPTEL, IIT KGP](https://www.youtube.com/playlist?list=PLbRMhDVUMngdCkMipemSKP_dCgZLLfOe8)
      1. [Lec-37: Gear Kinematics](https://www.youtube.com/watch?v=BjkxYZ93Fbs&list=PLbRMhDVUMngdCkMipemSKP_dCgZLLfOe8&index=38) 
      2. [Lec-38: Gear Trains I](https://www.youtube.com/watch?v=lu_Qw4Y4XRQ&list=PLbRMhDVUMngdCkMipemSKP_dCgZLLfOe8&index=39)
      3. [Lec-39: Gear Trains II](https://www.youtube.com/watch?v=5f3wBlRY8dQ&list=PLbRMhDVUMngdCkMipemSKP_dCgZLLfOe8&index=40)
      4. [Lec-40: Gear Trains III](https://www.youtube.com/watch?v=-aHRWEXB3h4&list=PLbRMhDVUMngdCkMipemSKP_dCgZLLfOe8&index=41)
2. [Bond Graph Modeling: NPTEL](https://www.youtube.com/watch?v=M8Nam032vgE)
3. [Gear Strength Theory: NPTEL](https://archive.nptel.ac.in/courses/112/106/112106137/)
4. [Friction-Model-for-Spur-Gear-transmission-efficiency: Review by Tsuneji Yada](https://www.jstage.jst.go.jp/article/jsmec1993/40/1/40_1_1/_article)

#### Miscellaneous:
1. [List-of-Science-and-Math-courses](https://github.com/Developer-Y/math-science-video-lectures)

#### Informative videos
1. **Materials**: Neodymium magnets [[Video-1: Brief history and use](https://youtu.be/XZZDy_R2h7E?si=wOG1tuobcxuZ3By6)] [[Video-2: Manufacturing_process](https://youtu.be/Egmi22VONS0?si=1Y3Cl43SdpTtWEuQ)]

</details>

<details><summary><b>Books</b></summary>

#### Mechanical Engineering
1. [Statics and Dynamics: Andy Ruina](http://ruina.tam.cornell.edu/Book/RuinaPratap-July-12-2019.pdf)

</details>

<details><summary><b>Articles (Installs / Study / Technical)</b></summary>

#### Technical topics:
1. [DDP](http://www.imgeorgiev.com/2023-02-01-ddp/): A good read for DDP
2. [Policy Gradient Algorithms](https://lilianweng.github.io/posts/2018-04-08-policy-gradient/#what-is-policy-gradient): A good read for Policy Gradient Algos
3. [Reinforcement Learning Resources](https://stable-baselines.readthedocs.io/en/master/guide/rl.html): A list of resources for studying Reinforcement Learning
4. [What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)

#### Study:
1. **How to read Research Papers?**
      * How to read a research paper by *Andrew NG*: [Video](https://www.youtube.com/watch?v=733m6qBH-jI) / [Notes](https://github.com/IvLabs/ResearchPaperNotes/tree/master/literature_study_tips)
      * How to Read a Paper by *S. Keshav*: [PDF](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)
      * How to read a paper: [LinkedIn Post](https://www.linkedin.com/feed/update/urn:li:activity:7044621048364900352?utm_source=share&utm_medium=member_desktop)
      * Useful Resources by *Ness B Shroff*, on PhD and writing papers: [Webpage](https://newslab.ece.ohio-state.edu/for%20students/index.html)
2. **How to organize research papers?**
      * How to find, read and organize papers by *Maya Gosztyla*: [Article](https://www.nature.com/articles/d41586-022-01878-7)

3. **How to setup and run your research Lab?**
      * A guide to setting up and managing a lab at a research-intensive institution : [[Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8218371/#CR2)]

#### Stories of Science:
1. [Steven LaValle](http://lavalle.pl/bio.html): Motivating story of Steven LaValle, who gave the RRT algorithm.
2. [Shuji Nakamura: Invention of Blue LED](https://youtu.be/AF8d72mA41M?feature=shared): Documentary about the invention of blue LED, which eventually led to a Nobel Prize in physics, one of the few for engineering efforts.
3. [The Value of Science: Richard P. Feynman](https://calteches.library.caltech.edu/1575/1/Science.pdf): An article on why science and the scientific method are important, is it just a tool for the betterment of society or is it much more?

#### Resource Websites:
1. [List of useful resources: Aditya Mehrotra, MIT D-lab](https://www.adim.io/resources)
2. [StePhane Caron](https://scaron.info/category/robotics.html)
3. [Usefull Resources: Xiaobin Xiong](https://www.xiaobinxiong.info/resources)

#### Software installations:
1. [Installing Anaconda on Ubuntu 22.04](https://linuxhint.com/install-anaconda-ubuntu-22-04/)
2. [Installing Anaconda on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart)
</details>

<details><summary><b>Random Cool Stuff</b></summary>

#### Mathematics
1. **Lean**: Programming Language for Theorem prover [[Link](https://lean-lang.org/)] \
      i. **Tutorials**: Natural Number Game [[Link](https://adam.math.hhu.de/#/g/leanprover-community/nng4)]
2. **Manim**: Python Library for making cool mathematical videos [[Github-Link](https://github.com/ManimCommunity/manim.git)] [[Manim Community](https://www.manim.community/)]

#### Cool AI tools:
1. [InstantID](https://huggingface.co/spaces/InstantX/InstantID) : Merges your picture with text description and an optional pose photo
2. [Text to Image Playground](https://huggingface.co/spaces/MisterProton/text-to-image-models-playground): COnvert text to image with free credits addition.

</details>

---------------------

## 4) Ecosystem
<details><summary><b>Professors & Labs</b></summary>

#### India
* **Shishir N Y**, Stochastic Robotics Lab, RBCCPS, IISc Bengaluru [[Personal Website](https://www.shishirny.com/)][[Lab website](https://www.stochlab.com/)]
* **Mangal Kothari**, IIT Kanpur: [[Homepage](https://home.iitk.ac.in/~mangal/)]

#### USA
* **Sangbae Kim**, Biomimetics Robotics Lab, MIT [[Lab Website](https://biomimetics.mit.edu/)]
* **Pulkit Agarwal**, Improbable AI Lab, MIT [[Personal Website](https://people.csail.mit.edu/pulkitag/)]
* **Deepak Pathak**, CMU [[Personal Website](https://www.cs.cmu.edu/~dpathak/)]
* **Zac Manchester**, Robotic Exploration Group, CMU [[Personal Webpage](https://www.ri.cmu.edu/ri-faculty/zachary-manchester/)][[Lab Website](https://roboticexplorationlab.org/)]
* **Ye Zhao**, LIDAR lab, Georgia Tech [[Personal Website](https://sites.google.com/site/yezhaout)][[Lab Website](https://lab-idar.gatech.edu/)]
* **Sehoon Ha**, Georgia Tech [[Personal Website](https://faculty.cc.gatech.edu/~sha9/)]
* **Quan Nguyen**, Dynamic Robotics and Control Laboratory, University of South California (USC) [[Personal Webpage](https://viterbi.usc.edu/directory/faculty/Nguyen/Quan)][[Lab Website](https://sites.usc.edu/quann/)]
* **Pranav Bhounsule**, Robotics and Motion Laboratory, University of Illinois Chicago [[Personal Webpage](https://mie.uic.edu/profiles/bhounsule-pranav/)][[Lab Website](https://pab47.github.io/)]
* **Joao Ramos**, Robo Design Lab, University of Illinois Urbana-Champaign (UIUC) [[Lab Website](https://publish.illinois.edu/robodesign/)]
* **Ayonga Hereid**, Cyber-Physical and Robotics Lab, Ohio State University [[Personal Webpage](https://mae.osu.edu/people/hereid.1)][[Lab Webpage](https://mae.osu.edu/cyberbotics)]
* **Koushil Sreenath**, Hybrid Robotics, University of South California, Berkeley (USC, Berkeley) [[Personal Webpage](https://me.berkeley.edu/people/koushil-sreenath/)][[Lab Website](https://hybrid-robotics.berkeley.edu/)]
* **Jitendra Malik**, EECS, University of California at Berkeley [[Personal Webpage](https://homepages.laas.fr/ostasse/hugo/)]
* **Yanran Ding**, Robotics Department, University of Michigan [[Personal Website](https://sites.google.com/view/yanranding/home)]
* **Xiaobin Xiong**, UW WELL Lab, University of Wisconsin-Madison [[Personal Website](https://www.xiaobinxiong.info/about)][[Lab Website](https://well.robotics.wisc.edu/team/)]

#### Europe
* **Marco Hutter**, Robotic Systems Lab, ETH Zurich, Switzerland [[Lab Website](https://rsl.ethz.ch/)]
* **Serena Ivaldi**, Research Scientist, INRIA, France [[Personal Website](https://members.loria.fr/SIvaldi/)]
* **Oliver Strasse**, French National Centre for Scientific Research, France [[Personal Website](https://homepages.laas.fr/ostasse/hugo/)]
* **Carlos Mastalli**, Heriot-Watt University, Edinburgh, UK [[Personal Website](https://cmastalli.github.io/)]

#### South Korea
* **Hae-Won Park**, DRDC Lab, KAIST [[Lab Website](https://www.dynamicrobot.kaist.ac.kr/)]
* **Jemin Hwangbo**, RaiLab, KAIST [[Lab Website](https://www.railab.kaist.ac.kr/)]

#### Other Labs
* **Sony Quadruped Research** [Website](https://www.sony.com/en/SonyInfo/research/technologies/new_mobility/)

</details>

<details><summary><b> List of Robotics Conferences and Journals </b></summary>
  
1. **List of Top Robotics Conferences and Publications**: [[List on Google Scholar Webpage](https://scholar.google.com/citations?view_op=top_venues&hl=en&vq=eng_robotics)]
      1. *A few ASME Conferences and Journals*:
            1. Journal of Mechanisms and Robots,
            2. Journal of Dynamics Systems, Measurement and Control, and
            3. Transaction on Mechatronics (IEEE/ASME) etc
      2. *A few IEEE Conferences and Journals*:
            1. International Conference on Robotics and Automation (ICRA),
            2. International Conference on Intelligent Robots and Systems (IROS),
            3. Robotics and Automation Letters (RAL),
            4. Transaction on Robotics (T-RO) etc.
        
2. **IEEE publication recommender:** [[Link](https://publication-recommender.ieee.org/home)]

</details>

<details><summary><b>Legged Robotics Companies</b></summary>
  
#### India
* **Strider Robotics**, Quadruped Company, based in Bengaluru [[Website](https://www.strider-robotics.in/)]
* **General Autonomy**, Humanoid and Quadruped Company, based in Bengaluru [[LinkedIn](https://www.linkedin.com/company/factoryofthefuture/posts/?feedView=all)]
* **xTerra Robotics**, Quadruped robot company, based in Kanpur [[Website](https://xterrarobotics.com/)]
* **Addverb**, Industrial mobile robots company with a division for legged robots, based in Delhi NCR [[Website](https://addverb.com/)]
* **Ati Motors**, Industrial Mobile robots company with a division for upper body humanoid robots, based in Bengaluru [[Website](https://atimotors.com/)]
* **NeoManav Robotics**: In stealth mode, in Bengaluru

</details>

---


## 5) Buying Hardware & Parts
<details><summary><b>Motors</b></summary>
  
1. [**TQ-Motors**](https://www.tq-group.com/de/produkte/tq-robodrive/): Used in Raibo Quadruped
2. [**Halodi Motors**](https://futurerobotix.com/?product=revo1-30): Used in Hound quadruped
3. [**Cube Mars**](https://store.cubemars.com/?rs_ref=rbz3SHCJ): Different kind of actuators available
4. [**Robstride Dynamics**](https://robstride.com/): Actuators of different kinds, one of the most cost effective ones

</details>

<details><summary><b>Drivers</b></summary>

1. **Mjbots**: [Moteus-n1](https://mjbots.com/products/moteus-n1), [Moteus-r4.xx](https://mjbots.com/products/moteus-n1) \
                        It also provide several other accesories for legged robots. It is like a one stop shop.
2. **O-drives**: [Buying-Link](https://odriverobotics.com/?srsltid=AfmBOor5dbEx1yK3nqDN6iZG3vK3uxDh5Z1SSTte0VuJgffkIhFrC24q)

</details>

<details><summary><b>Stators</b></summary>

1. **8110 Stator**: you can order single stator here [[Ebay-Link](https://www.ebay.com/itm/314132711015)] \
2. **BLDC Stators**: You can order bulk stators here [[Made-in-china link](https://yuhuidg.en.made-in-china.com/)]


</details>

<details><summary><b>Permanent Magnets</b></summary>

1. **N52 Neodymium magnets**: [[Digikey India Link](https://www.digikey.in/en/products/detail/radial-magnets-inc/8110/5400478?gclsrc=aw.ds&gad_source=1&gad_campaignid=23291937036&gbraid=0AAAAADrbLlgJjB_1CELFK0V2KPXLLOrOW&gclid=Cj0KCQiA1czLBhDhARIsAIEc7uh_KnAzMXl7b3tJNi5YqIt6ON5xnd7i2C60bHppvT43sNw2f19od5EaAlQPEALw_wcB)]
 
</details>

<details><summary><b>Manufacturing Tools</b></summary>

1. **HONEST**(Shenzen Honest Intelligent Equipments): Chinese Company, sells Motor Winding Machines [[Website-Link](https://www.honest-hls.com/products)] \
                        Has a center in Kanchipuram, near Chennai, India as well
</details>

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=singhaman1750/Legged-Robots&type=date&legend=top-left)](https://www.star-history.com/#singhaman1750/Legged-Robots&type=date&legend=top-left)
