# F1Tenth Vehicle States & Dynamics

F1Tenth is used as our "*robot*" throughout this BootCamp, so it's fitting to introduce its states, kinematics, and dynamics here. 

<img src="fig/f1tenth.jpg" width="200"/>

(As shown above, F1Tenth vehicles are open-source, 1∕10-scale autonomous racecars that replicate the sensing, computing, and control stack of full-size self-driving cars.)
<br>
<br>

> Note that the majority of the content in this section is from Dr. Johannes Betz's lecture on [F1Tenth L06 - Vehicle States, Vehicle Dynamics, and Map Representations](https://www.youtube.com/watch?v=8zr5NUS05cM&list=PL7rtKJAz_mPdFDJtufKmqfWRNu55s_LMc&index=8) on YouTube.

## 1. F1Tenth Vehicle States

Vehicle states, including position, velocity, and orientation, are fundamental components in dynamic modeling. Accurate measurement and representation of these states enable better predictions and refined control, ensuring that the model closely mirrors real-world driving scenarios.

Here, we introduce the essential states used when modeling the F1Tenth vehicle dynamics.

### Position
<img src="fig/f1tenth_position.png" width="200"/>

*Position* defines the translation of the vehicle in some global or local frame. It's respective to the vehicle's center of gravity (CoG) or a pre-defined based frame.

Normally, the $x$- and $y$-positions have **meters** as their units.