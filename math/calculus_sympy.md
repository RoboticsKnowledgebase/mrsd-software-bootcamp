# Calculus & SymPy for Robotics  

Robotic systems constantly **change**—motors spin, drones accelerate, sensors integrate rates.  
Calculus provides the language for that change, letting us model velocities, forces, and accumulated error.  
SymPy brings symbolic calculus to Python, while NumPy/SciPy turn those symbolic formulas into lightning-fast numeric kernels.

---

## 1. Why Calculus Matters in Robotics  

* Derivatives give joint **velocities**, **accelerations**, and **Jacobians** for manipulators.  
* Integrals convert IMU angular rates into orientation, add wheel encoder ticks into distance, and compute energy or work.  
* Differential equations model quadrotor flight, arm dynamics, and battery discharge—controllers need their solutions.  

---

## 2. Introduction to Calculus  

### 2.1 Core Ideas  
| Concept | Robotics snapshot |
|---------|-------------------|
| **Derivative** \( $\tfrac{d}{dt}\,x(t)$ \) | end–effector speed, PID error rate |
| **Gradient / Jacobian** | mapping joint speeds to Cartesian speeds |
| **Integral** \( $\int_0^T \tau(t)\,dt$ \) | work done, pose from velocity |
| **ODE** \( $\dot{x}=f(x,u)$ \) | state-space model for control & estimation |

---

## 3. External Learning Resources  

### 3.1 Textbooks  
* [“Calculus: Early Transcendentals” – Stewart](https://www.cengage.com/c/calculus-early-transcendentals-9e-stewart/)  
* [“Advanced Engineering Mathematics” – Kreyszig](https://www.wiley.com/en-us/Advanced+Engineering+Mathematics%2C+10th+Edition-p-9780470458365)  
* [“Mathematical Methods for Physics & Engineering” – Riley • Hobson • Bence](https://www.cambridge.org/9780521679718)  

### 3.2 Interactive / Online Courses  
* [MIT OCW 18.01 – Single-Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)  
* [Khan Academy – Calculus I & II](https://www.khanacademy.org/math/calculus-1)  
* [Coursera – “Calculus: Single Variable” (UPenn)](https://www.coursera.org/learn/calculus1)  

### 3.3 YouTube Playlists  
* [3Blue1Brown – “Essence of Calculus”](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)  
* [Professor Leonard – Full Calculus Lecture Series](https://www.youtube.com/user/professorleonard57/playlists)  
* [MIT OCW – 18.01 Fall 2007 Lectures](https://www.youtube.com/playlist?list=PL590CCC2BC5AF3BC1)  

---

## 4. Introduction to SymPy  

SymPy is Python’s **pure-symbolic** math library.  
* Perform exact derivatives, integrals, series, equation solving, matrix calculus.  
* `lambdify` turns symbolic expressions into NumPy-powered callables—ideal for simulation loops.  
* Tight SciPy hooks: feed analytic Jacobians or ODE RHS directly to `scipy.integrate.solve_ivp`.  
* Code generators spit out C, C++, Fortran, or LLVM—drop into ROS nodes or micro-controllers.

### 4.1 Installation  
``python
python -m pip install sympy
``  

### 4.2 Quick-Start Cheatsheet  
| Task | Snippet |
|------|---------|
| declare symbols | ``x, t = sympy.symbols('x t')`` |
| differentiate | ``sympy.diff(sympy.sin(x)*x, x)`` |
| integrate | ``sympy.integrate(sympy.exp(-x**2), (x, -sympy.oo, sympy.oo))`` |
| substitute | ``expr.subs(x, 2.0)`` |
| numeric callable | ``f = sympy.lambdify(x, sympy.sin(x), 'numpy')`` |
| series | ``sympy.series(sympy.cos(x), x, 0, 4)`` |

### 4.3 Deeper Tools  
* **`sympy.matrices`** – analytic inverses, determinants, eigen-pairs  
* **`sympy.physics.mechanics`** – multibody dynamics, Kane’s method  
* **`sympy.solvers.ode`** – exact ODE solutions, Laplace transforms  
* **`sympy.tensor`** – index notation, Riemann geometry  
* **`sympy.codegen`** – C/Fortran/LLVM emission with NumPy-compatible signatures  

### 4.4 Official Docs & Cheat Sheets  
* [SymPy Documentation](https://docs.sympy.org/latest/index.html)  
* [SymPy Cheatsheet PDF](http://daabzlatex.s3.amazonaws.com/9065616cce623384fe5394eddfea4c52.pdf)  
* [Introduction to Sympy and the Jupyter Notebook for engineering calculations](https://dynamics-and-control.readthedocs.io/en/latest/0_Getting_Started/Notebook%20introduction.html) <-- This is great!  

---

## 5. Hands-On Exercises 🔧  

### Exercise 1 - Trajectory Velocities  
Differentiate a cubic position spline and evaluate velocity/acceleration at \( t=0.8 s \).  
```python
import sympy as sp
t = sp.symbols('t')
p = 0.5*t**3 - 1.2*t**2 + 0.3*t      # pos [m]
v = sp.diff(p, t)
a = sp.diff(v, t)
print("v(0.8) =", v.subs(t, 0.8).evalf())
print("a(0.8) =", a.subs(t, 0.8).evalf())
```  

---

### Exercise 2 - Planar Arm Jacobian  
Create symbolic forward-kinematics, derive the Jacobian, then lambdify.  
```python
l1, l2, th1, th2 = sp.symbols('l1 l2 th1 th2')
x = l1*sp.cos(th1) + l2*sp.cos(th1+th2)
y = l1*sp.sin(th1) + l2*sp.sin(th1+th2)
J = sp.Matrix([x, y]).jacobian([th1, th2])
fk = sp.lambdify((th1, th2, l1, l2), [x, y], 'numpy')
jac = sp.lambdify((th1, th2, l1, l2), J, 'numpy')
print("J(π/4, π/3) =", jac(3.1416/4, 3.1416/3, 0.5, 0.4))
```  

---

### Exercise 3 - Numerical Integration via `lambdify`  
Generate a SymPy RHS for a damped spring, convert to NumPy, integrate with SciPy.  
```python
import numpy as np, sympy as sp, scipy.integrate as si
k, c, m = 20.0, 2.0, 1.0
x, v, t = sp.symbols('x v t')
dx = v
dv = -(k/m)*x - (c/m)*v
rhs = sp.lambdify((t, [x, v]), [dx, dv], 'numpy')
sol = si.solve_ivp(rhs, [0, 5], [0.1, 0.0], t_eval=np.linspace(0,5,500))
print("max disp =", sol.y[0].max())
```  

---

### Exercise 4 - Energy of a Quadrotor Thrust Profile  
Integrate thrust × velocity over time to compute work done.  
```python
T, v, t = sp.symbols('T v t')
thrust = 9.8 + 5*sp.sin(2*sp.pi*t)           # N
velocity = 0.5*t                             # m/s
work = sp.integrate(thrust*velocity, (t, 0, 4))
print("Work [J] =", work.evalf())
```  

---

### Exercise 5 - C Code Generation for Embedded Controller  
Produce C code for a PID control law \( u = K_p e + K_d \dot{e} + K_i \int e dt \).  
```python
Kp, Kd, Ki, e, de, ie = sp.symbols('Kp Kd Ki e de ie')
u = Kp*e + Kd*de + Ki*ie
sp.ccode(u, assign_to="control_output", standard='c11')
```

---
