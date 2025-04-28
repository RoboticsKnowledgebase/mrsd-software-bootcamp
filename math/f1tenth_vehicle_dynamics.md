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

### **Position**

<img src="fig/f1tenth_position.png" width="200"/>

*Position* defines the translation of the vehicle in some global or local frame. It's respective to the vehicle's center of gravity (CoG) or a pre-defined based frame. Normally, the $x$- and $y$-positions have **meters** as their units.

### **Heading**

<img src="fig/f1tenth_heading.png" width="200">

*Heading* defines the rotation of the vehicle in some local and global frame. This is usually with respect to the $x$-axis of the local frame. 

When represented as a single angle reading, heading can be displayed in ranges from:
- $[-\pi, \pi] = [-180^\circ, 180^\circ]$
- $[0, 2\pi] = [0^\circ, 360^\circ]$

The heading angle can be represented as RPY, Rotation Matrix, Quaternion, etc.

### **Linear Velocity and Acceleration**

<img src="fig/f1tenth_linear.png" width="230">

*Linear velocity and acceleration* are measured in the $x$- and $y$- (and $z$-) axis in the coordinate system of the vehicle. 
For vehicles, there are **longitudinal** ($x$-axis) and **lateral** ($y$-axis) velocities and accelerations. Here, the right-hand-rule is used.

Velocity is measured in meters per second [$m/s$] and acceleration in meters per second squared [$m/s^2$].

These can be measured with GPS, IMU, wheel speed sensors, pitot sensors, etc. 

### **Angular Velocity and Acceleration**

<img src="fig/f1tenth_angular.png" width="400">

### **Steering Angle**

<img src="fig/f1tenth_steering.png" width="200">

*Steering angle* $\delta$ is the angle formed by the direction the front wheels are pointing at and the vehicle's $x$-axis. Steering angle is the same for both front wheels and are in radians or degrees.

### **Slip Angles**

**Sideslip**

<img src="fig/f1tenth_sideslip.png" width="200">

*Sideslip* angle $\beta$ is between the direction of travel and the $x$-axis of the chassis. 

**Slip**

<img src="fig/f1tenth_slip.png" width="250">

*Slip* angle $\alpha$ is between the direction of travel and the angle the wheel is pointing towards.

**Wheelslip**

<img src="fig/f1tenth_wheelslip.png" width="200">

*Wheelslip* ratio is the normalized difference between a wheel's circumferential speed and the vehicle's actual ground speed. This indicates how much the tire is spinning or skidding relative to the road surface.

$$\text{wheelslip ratio } \% = \left( \frac{\Omega \; R_c}{V} - 1\right) \times 100 \%$$

> Essentially, sideslip is the angle when you drift and slip is whenever there's steering. Wheelslip is when you're doing a burnout.

## 2. Vehicle Dynamics Model Types