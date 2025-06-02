# System Dynamics:  What it is and Why it Matters

In this section, we will introduce some basic concepts for system dynamics and the importance of dynamic modeling.

Robots are **dynamic systems** – their states change continuously in response to control inputs and external disturbances. Dynamic modeling is the how we derive real-world system dynamics into forms that could be used by us, the engineers.
Dynamic modeling plays a critical role in understanding and predicting a robot's behavior under various operating conditions. By using mathematical representations, engineers can simulate responses, optimize control strategies, and improve performance safety.

| Goal | Example |
|------|---------|
| **Predict** | How fast a quadrotor will tilt after a given motor command |
| **Design**  | Tune a PID or LQR gain that stabilises a two-link arm |
| **Optimise**| Plan a minimum-energy path while respecting actuator limits |
| **Validate**| Check safety constraints before running code on real hardware |

> In short: *No model, no reliable control nor prediction.*

## 1. Types of Dynamics Models  

Below are not all of the types of dynamics models used by engineers and researchers. However, they cover a pretty large chunk of what's available. 

| Category | Core idea | Pros | Cons |
|----------|-----------|------|------|
| **Analytical** | Derive $f$ from first principles (Newton, Euler-Lagrange) | Interpretable, generalises outside training data | Requires physics insight; often neglects some variables to simplify dynamics |
| **Data-driven** | Fit $f_{\text{NN}}$ from logged trajectories | Captures hard-to-model effects | Needs lots of data; poor extrapolation |
| **Residual Physics** | Combine analytical base + learned correction | Good accuracy with less data | Added complexity |
| **Hybrid / Sim** | Mix analytical, learned, and full physics engines | Flexible | Heavy computation; tuning effort |

**This course focuses on the *analytical* approach.**  
Understanding the math behind $f$ and $g$ (or $A,B,C$) equips you to:

* design controllers (e.g. MPC, LQR)  
* prove stability and safety properties  
* port models between simulators and embedded code

---

## 2. What is a System Dynamics?  

A system dynamics relates an **input** $u(t)$ to an **output** $y(t)$ through hidden **states** $x(t)$ that evolve according to ordinary differential equations (ODEs).

The standard system description consists of the *system dynamics* and the *output equation*. The former describes the behavior over time of the states as a reaction to the inputs and the initial state. The latter describes the relation between the state and the output. 

- $x$ – **states** are variables which allow us to formulate the system behavior in form of a set of first-order ODE for each of the variable. Examples include pose, velocity, battery SOC, etc.  
- $u$ – **inputs** are how the robot acts in the world such as thrusts, torques, acceleration, etc..  
- $y$ - **outputs** are what we measure or regulate (speed, force).
* $A$  – **system matrix** (physics & geometry)  
* $B$  – **input matrix** (actuator directions)  
* $C$  – **output matrix** (sensors or variables we care about)

### 2.1 Linear, Time-Invariant (LTI)

$$
\begin{aligned}
\dot{x} &= A\,x + B\,u, \\
y &= C\,x
\end{aligned}
$$

| Term | Meaning |
|------|---------|
| **Linear** | The dynamics obey the *superposition* and *homogeneity* principles:  <br>if inputs/states $(x_1,u_1)$ and $(x_2,u_2)$ produce $\dot{x}_1$ and $\dot{x}_2$, then for any scalars $\alpha,\beta$  <br>$\alpha x_1 + \beta x_2,\; \alpha u_1 + \beta u_2 \;\Longrightarrow\; \alpha\dot{x}_1 + \beta\dot{x}_2$  <br>Mathematically, $\dot{x}=A x + B u$ and $y=C x + D u$ are *affine* in $(x,u)$ with no products or powers. |
| **Time-Invariant** | The matrices $A,B,C,D$ (or functions $f,h$) **do not depend explicitly on time**. A delayed input behaves the same later:  <br>if $u(t)\mapsto y(t)$ then $u(t-\tau)\mapsto y(t-\tau)$. |

**Why LTI is powerful**  
- Closed-form solutions via exponentials: $x(t)=e^{At}x_0+\int e^{A(t-\tau)}B\,u(\tau)\,d\tau$.
- Frequency-domain tools (transfer functions, Bode plots) apply.
- Stability, controllability, observability reduce to **eigenvalue** tests.
- Efficient software (MATLAB, SciPy) provides out-of-the-box solvers and controllers. |

---

### 2.2 Non-Linear Form  

A system is **non-linear** when its state equation contains products, powers, saturations, trigonometric terms, etc.

$$
\begin{aligned}
\dot{x} &= f(x,u), \\
y &= h(x)
\end{aligned}
$$
*Examples*:  
* Inverted-pendulum: $\dot{\theta}_2 = \frac{g}{l}\sin\theta$ – sine makes it non-linear.  
* Quadrotor: aerodynamics introduce $u_i^2$ thrust terms.  

**Implications**  
* Superposition no longer holds.  
* Stability analysis uses Lyapunov or linearization.  
* Control design often linearizes the model around an operating point, then applies LTI tools.

---

### 2.3 Time-Varying Systems  

A system is **time-varying** if its dynamics change explicitly with $t$:

$$
\begin{aligned}
\dot{x} &= A(t)\,x + B(t)\,u , \\
y &= C(t)\,x
\end{aligned}
$$

*Examples*  
* Satellite with moving solar arrays ⇒ inertia $I(t)$ varies.  
* Battery-powered rover ⇒ mass and voltage change as energy drains.  

**Consequences**  
* Shift property breaks; a controller tuned at one moment may under-perform later.  
* Some time-varying systems can be converted to time-invariant form by state augmentation, but often at the cost of higher dimension.

---


> **Take-away** LTI models are the “sweet spot’’ for analysis and controller synthesis.  When reality is non-linear or time-varying we either (i) linearize around an operating point, (ii) update the linear model online (gain scheduling), or (iii) design non-linear controllers directly.

<br>
<br>

## Example System Dynamics

Below are two classic robotic systems: a **linear time-invariant** (LTI) mass–spring–damper and a **non-linear** pendulum.  
Each is presented with states, inputs, LaTeX equations, and a NumPy implementation you can paste directly into your own file.

---

### LTI Example - Mass–Spring–Damper  

| Symbol | Meaning |
|--------|---------|
| $x_1$  | position $p$ [m] |
| $x_2$  | velocity $\dot{p}$ [m/s] |
| $u$    | external force $F$ [N] |

$$
\begin{aligned}
\dot x_1 &= x_2 \\
\dot x_2 &= -\tfrac{k}{m}\,x_1 - \tfrac{b}{m}\,x_2 + \tfrac{1}{m}\,u
\end{aligned}
$$

with state vector $x=\begin{bmatrix}x_1\\x_2\end{bmatrix}$, matrices  $A=\begin{bmatrix} 0 & 1 \\ -k/m & -b/m \end{bmatrix},\quad B=\begin{bmatrix} 0 \\ 1/m \end{bmatrix} $.

```python
import numpy as np

# system constants
m, k, b = 1.0, 5.0, 0.8          # kg, N/m, N·s/m

A = np.array([[0,           1],
              [-k/m,  -b/m]])
B = np.array([[0],
              [1/m]])

def lti_step(x, u, dt):
    """
    Euler step for mass–spring–damper.
    x : shape (2,)
    u : scalar force
    dt: timestep
    """
    dx = A @ x + B.flatten() * u
    return x + dt * dx

# demo
x = np.array([0.1, 0.0])         # 10 cm stretch, zero velocity
for _ in range(10):
    x = lti_step(x, u=0.0, dt=0.01)
print("state after 0.1 s:", x)
```  

---

### Non-linear Example – Pendulum with Torque  

| Symbol | Meaning |
|--------|---------|
| $x_1$  | angle $\theta$ [rad] |
| $x_2$  | angular rate $\dot\theta$ [rad/s] |
| $u$    | motor torque $\tau$ [N·m] |

$$
\begin{aligned}
\dot x_1 &= x_2 \\
\dot x_2 &= -\frac{g}{l}\,\sin x_1 - \frac{b}{I}\,x_2 + \frac{1}{I}\,u
\end{aligned}
$$

```python
import numpy as np

g, l   = 9.81, 0.3               # gravity [m/s²], rod length [m]
m, b   = 0.5, 0.02               # mass [kg], viscous friction [N·m·s]
I     = m * l**2                 # moment of inertia

def pendulum_step(x, u, dt):
    """
    Pendulum Euler step (non-linear dynamics).
    x : shape (2,)  [theta, omega]
    u : torque
    dt: timestep
    """
    theta, omega = x
    dtheta = omega
    domega = -(g/l) * np.sin(theta) - (b/I) * omega + u / I
    return x + dt * np.array([dtheta, domega])

# demo swing-up pulse
x = np.array([0.0, 0.0])         # hanging down
for _ in range(100):
    x = pendulum_step(x, u=0.2, dt=0.02)
print("state after 2 s:", x)
```  

> **Tip** If you need Jacobians for linearization, wrap the dynamics with SymPy’s `symbols` and `diff`:

```python
import sympy as sp
theta, omega, tau = sp.symbols('theta omega tau')
f = sp.Matrix([omega,
               -(g/l)*sp.sin(theta) - (b/I)*omega + tau/I])
A_jac = f.jacobian([theta, omega])       # ∂f/∂x
B_jac = f.jacobian([tau])                # ∂f/∂u
print(sp.simplify(A_jac))
```  

### Exercise!
Now you have both analytical and non-linear models ready for simulation, control design, or further analysis. 

**Try to plot out how the states change over time!!!**
