# Optimization & `SciPy` for Robotics

Robots need to **decide**: where to move, how to move, how fast to go.  
These decisions often boil down to solving **optimization problems**—minimizing a cost (e.g., energy, time, error) under physical or logical constraints.

Python’s `SciPy.optimize` module makes it easy to define and solve these problems with minimal overhead and maximal flexibility.

---

## 1. Why Optimization Matters in Robotics

* **Trajectory planning** – minimize time or energy while avoiding obstacles  
* **Parameter tuning** – auto-calibrate models and controllers  
* **Inverse kinematics** – find joint angles that achieve a task  
* **System ID** – fit parameters to observed robot data  
* **Control** – MPC, LQR, and reinforcement learning all involve optimization  
* **Perception** – SLAM, bundle adjustment, and point cloud registration are optimization problems under the hood

---

## 2. External Learning Resources

### 2.1 Books
* [Boyd & Vandenberghe – *Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/)
* [Nocedal & Wright – *Numerical Optimization*](https://www.springer.com/gp/book/9780387303031)
* [SciPy Optimization Docs](https://docs.scipy.org/doc/scipy/reference/optimize.html)

### 2.2 Courses
* [MIT 6.252 – Nonlinear Programming](https://ocw.mit.edu/courses/6-252j-nonlinear-programming-spring-2003/)
* [Stanford EE364a – Convex Optimization](https://web.stanford.edu/class/ee364a/)
* [Khan Academy – Optimization with Constraints](https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives)

---

## 3. Core SciPy Optimization Tools

| Task | Function |
|------|----------|
| Unconstrained minimize | `scipy.optimize.minimize` |
| Least-squares fitting | `scipy.optimize.least_squares` |
| Constrained nonlinear optimization | `minimize(..., constraints=...)` |
| Bounds on variables | `bounds=` keyword |
| Global optimization | `basinhopping`, `differential_evolution` |
| Root finding | `root`, `fsolve` |
| Curve fitting | `curve_fit` |

---

## 4. Installation

<details>
<summary>pip install</summary>

```bash
python -m pip install scipy
```

</details>

<details>
<summary>conda env</summary>

```bash
conda create -n optboot python=3.12 scipy
conda activate optboot
```

</details>

---

## 5. Hands-On Exercises 🔧

---

### Exercise 1 – Scalar Function Minimization

Minimize the function `f(x) = (x - 3)^2 + 5`.

```python
from scipy.optimize import minimize

f = lambda x: (x - 3)**2 + 5
res = minimize(f, x0=[0])
print("Minimum x* =", res.x, "f(x*) =", res.fun)
```

---

### Exercise 2 – Multivariable Function Minimization

Minimize `f(x, y) = x² + 2y² + xy + x`.

```python
import numpy as np
from scipy.optimize import minimize

f = lambda v: v[0]**2 + 2*v[1]**2 + v[0]*v[1] + v[0]
res = minimize(f, x0=[1, 1])
print("opt =", res.x)
```

---

### Exercise 3 – Optimization with Bounds

Minimize `f(x) = x²` with bounds `-1 ≤ x ≤ 2`.

```python
res = minimize(lambda x: x**2, x0=[0.5], bounds=[(-1, 2)])
print("x* =", res.x)
```

---

### Exercise 4 – Constrained Optimization (equality/inequality)

Minimize `f(x) = x[0]² + x[1]²`  
subject to constraint: `x[0] + x[1] = 1`.

```python
cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - 1})
res = minimize(lambda x: x[0]**2 + x[1]**2, x0=[0.5, 0.5], constraints=cons)
print(res.x)
```

Try changing to an inequality: `'type': 'ineq'` for `x[0] + x[1] ≤ 1`.

---

### Exercise 5 – Nonlinear Least Squares

Fit parameters `a`, `b` in `y = a * exp(bx)` to noisy data.

```python
import numpy as np
from scipy.optimize import curve_fit

# synthetic data
x = np.linspace(0, 4, 50)
y = 2.5 * np.exp(1.3 * x) + np.random.normal(0, 1, size=x.shape)

# model
def model(x, a, b):
    return a * np.exp(b * x)

popt, _ = curve_fit(model, x, y)
print("a =", popt[0], "b =", popt[1])
```

---

### Exercise 6 – Inverse Kinematics via Optimization

Given end-effector target `(x, y)`, find `th1`, `th2` such that  
`x = l1*cos(th1) + l2*cos(th1+th2)`  
`y = l1*sin(th1) + l2*sin(th1+th2)`

```python
import numpy as np
from scipy.optimize import minimize

l1, l2 = 1.0, 1.0
target = np.array([1.2, 0.8])

def objective(th):
    x = l1*np.cos(th[0]) + l2*np.cos(th[0]+th[1])
    y = l1*np.sin(th[0]) + l2*np.sin(th[0]+th[1])
    err = np.linalg.norm([x, y] - target)
    return err

res = minimize(objective, x0=[0, 0])
print("th1, th2 =", res.x)
```

---

### Exercise 7 – MPC Toy Example (no dynamics)

Minimize squared error from target over horizon:

```python
import numpy as np
from scipy.optimize import minimize

N = 10
target = np.ones(N)

def cost(u):
    return np.sum((u - target)**2)

bounds = [(0, 1)] * N
res = minimize(cost, x0=np.zeros(N), bounds=bounds)
print("u* =", res.x)
```

This is a basic structure for model predictive control: optimize control input `u` to minimize cost over time.

---

## 6. Tips for Success

* **Always inspect `res.success` and `res.message`** – to check if the solver converged  
* **Scale your variables** – optimization performs better when variables are on similar scales  
* **Use gradients (Jacobian) if possible** – speeds up and stabilizes convergence  
* **Visualize your objective function** – surface/contour plots often reveal pathologies  
* **Test multiple solvers** – try `'BFGS'`, `'SLSQP'`, `'trust-constr'`, etc. via `method=` keyword

---

## 7. Official Docs & Cheatsheets

* [SciPy Optimization Reference](https://docs.scipy.org/doc/scipy/reference/optimize.html)
* [Optimization Benchmarks](https://scipy-lectures.org/advanced/mathematical_optimization/)
* [SciPy Cookbook](https://scipy-cookbook.readthedocs.io/items/)

---
