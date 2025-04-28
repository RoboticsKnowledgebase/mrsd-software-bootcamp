# Linear Algebra & `NumPy` for Robotics
Robots **sense**, **think**, and **move** in the physical world—activities that can all be expressed with *linear algebra*.  
Vectors describe positions and forces; matrices embody rotations, translations, and the dynamics that link state variables over time.  
Mastering these ideas—and the Python tool that makes them fast and friendly, **NumPy**—gives you a direct line from theory to working code.

> **Why start here?**  
> * Writing controllers? You will multiply Jacobians by error vectors.  
> * Running a Kalman filter? You need matrix inversions at every time-step.  
> * Training a neural network for perception? Its weights are learned with linear-algebra kernels under the hood.  

Grasp the math, wield the library, and the rest of the robotics stack (optimization, SLAM, MPC, etc.) becomes dramatically easier.

## 1. Introduction to Linear Algebra

### 1.1 Core Objects
| Object | Notation | Example Use in Robotics |
|--------|----------|-------------------------|
| **Scalar** | \($a \in \mathbb{R}$\) | Time-step ∆t, wheel radius |
| **Vector** | \($\mathbf{v}\in\mathbb{R}^n$\) | Position \($ [x,y,z]^\top $\), joint velocities |
| **Matrix** | \($A\in\mathbb{R}^{m\times n}$\) | Rotation \($R_{^\mathcal{I}\!T}$\), robot Jacobian |
| **Tensor** | \($ \mathcal{T}\in\mathbb{R}^{n_1\times n_2\times\cdots} $\) | RGB-D image stack, inertia tensor field |

### 1.2 Vector Operations
* **Addition / Subtraction**   \($ \mathbf{v} \pm \mathbf{w} $\)  
* **Scalar multiplication**   \($ \alpha\mathbf{v} $\)  
* **Dot product**   \($ \mathbf{v}\!\cdot\!\mathbf{w} = \sum_i v_i w_i $\) → angle / projection  
* **Cross product (3-D)**   \($ \mathbf{v}\times\mathbf{w} $\) → torque from force and lever-arm  
* **Norm**   \($ \lVert\mathbf{v}\rVert_2 = \sqrt{\mathbf{v}\!\cdot\!\mathbf{v}} $\)

### 1.3 Matrix Operations
* **Matrix–vector product**   \($ A\mathbf{v} $\) → rotate or transform a pose  
* **Matrix–matrix product**   \($ AB $\) → chain two transformations  
* **Transpose**   \($ A^\top $\) → swap rows/columns (important for dot products)  
* **Determinant**   \($\det(A)$\) → volume scaling; non-zero ⇒ invertible  
* **Inverse**   \($ A^{-1} $\) → “undo” a transformation  
* **Rank**   number of linearly independent columns → controllability/observability  
* **Eigen-decomposition**   \($A\mathbf{x}=\lambda\mathbf{x}$\) → modal analysis, PCA  
* **Singular-value decomposition (SVD)**   \($A=U\Sigma V^\top$\) → least-squares, pseudoinverse

## 2. External Learning Resources

### 2.1 Textbooks
1. [**Gilbert Strang** – *Introduction to Linear Algebra* (6 th ed.)](https://math.mit.edu/~gs/linearalgebra/ila6/indexila6.html)
2. [**Stephen Boyd & Lieven Vandenberghe** – *Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares*](https://vmls-book.stanford.edu/)
3. [**David C. Lay** – *Linear Algebra and Its Applications* (5 th ed.)](https://www.amazon.com/Linear-Algebra-Its-Applications-5th/dp/032198238X)

### 2.2 Interactive / Online Courses
1. [**Khan Academy – Linear Algebra**](https://www.khanacademy.org/math/linear-algebra)
2. [**MIT OpenCourseWare 18.06 – Linear Algebra**](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
3. [**Coursera – Linear Algebra for Machine Learning**](https://www.coursera.org/learn/linear-algebra-machine-learning)

### 2.3 YouTube Playlists
1. [**3Blue1Brown – “Essence of Linear Algebra”**](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
2. [**Steve Brunton – “Control Bootcamp (Linear-Algebra Refresh)”**](https://www.youtube.com/playlist?list=PLMrJAkhIeNNR20Mz-VpzgfQs5zrYi085m)
3. [**Stanford SEE – EE263 “Introduction to Linear Dynamical Systems”**](https://www.youtube.com/playlist?list=PL06960BA52D0DB32B)



## 3. Introduction to NumPy


`NumPy` is the *de-facto* standard for numerical computing in Python.

* **Performance without pain** `ndarray` objects are thin, Python-friendly handles on top of contiguous, typed C arrays. Element-wise and linear-algebra kernels dispatch to highly tuned BLAS & LAPACK libraries, giving you C/Fortran speed while writing clean Python.  
* **Vectorization & broadcasting** Idiomatic NumPy code replaces slow, error-prone loops with concise array expressions that the CPU—or GPU via CuPy/JAX—can crunch in parallel.  
* **Universal data currency** Most data-science, ML, and robotics libraries—**SciPy, pandas, scikit-learn, TensorFlow, PyTorch, JAX, OpenCV, ROS 2 `rclpy`, Drake, MoveIt, Isaac Sim,** and thousands more—*speak NumPy arrays natively.* Pass an `ndarray` in, get an `ndarray` out.  
* **Interoperability & ecosystem glue** Plot with Matplotlib or Plotly, optimize with SciPy, serialize with HDF5, stream over ZeroMQ—every package assumes its inputs are NumPy arrays, so nothing gets copied or converted.  
* **Maturity & community** Born in 2006, NumPy now powers the majority of peer-reviewed computational science. A massive community means battle-tested functions, exhaustive docs, and answers to almost any array question you’ll ever search for.  

> **Bottom line:** If you learn just one Python tool for linear algebra, make it **NumPy**.


### 3.1 Installation

<details>
<summary>pip install</summary>

```bash
python -m pip install numpy
```
</details> 

<details> 
<summary>Conda env</summary>

```bash
conda create -n mrsd python=3.12 numpy
conda activate mrsd
```
</details>

### 3.2 Import Convention
```python
import numpy as np
```

### 3.3 Quick-Start Cheatsheet
| Task | Code |
|------|------|
| **Create** | `a = np.array([1, 2, 3])`<br>`Z = np.zeros((3, 4))`<br>`I = np.eye(4)` |
| **Shape** | `a.shape`<br>`a.reshape(3, 1)` |
| **Index / slice** | `a[0]`<br>`A[1:3, ::-1]`<br>boolean masks |
| **Math** | `a + b`<br>`a * b` (element-wise)<br>`np.dot(A, B)` or `A @ B` |
| **Broadcasting** | `A + b` (vector `b` auto-expands to rows of `A`) |
| **Linear algebra** | `np.linalg.inv(A)`<br>`np.linalg.eig(A)`<br>`np.linalg.svd(A)` |
| **Random** | `r = np.random.default_rng().normal(size=1000)` |
| **Save / Load** | `np.save('mat.npy', A)`<br>`np.load('mat.npy')` |

### 3.4  Deeper Tools  

- `np.linalg` — BLAS/LAPACK wrappers (`qr`, `cholesky`, `solve`, …)  
- `np.einsum` — Einstein notation for fast tensor ops  
- `np.broadcast_to`, `np.tile`, `np.newaxis` — fine-grained reshaping  
- `memoryview`, `np.ascontiguousarray` — control layout for C-extensions  
- **dtype gymnastics** — structured arrays for sensor packets  
- `numba`, `cupy`, `jax` — drop-in accelerated back-ends when the CPU isn’t enough  

### 3.5  Official Docs & Cheat Sheets  

- [**NumPy User Guide**](https://numpy.org/doc/stable/user/)  
- [**NumPy API Reference**](https://numpy.org/doc/stable/reference/)  
- [**SciPy-NumPy Cheat Sheet (PDF)**](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_SciPy_Cheat_Sheet_Linear_Algebra.pdf)  

## 4. Hands-On Exercises 🔧
First make a new script, named `la_numpy_bootcamp.py`. Then, copy the snippets into `la_numpy_bootcamp.py`, run them, and **read the printed output**. Each exercise illustrates a core robotics concept plus a NumPy idiom.

---

### Exercise 1 – Pose Composition  

Combine two 2-D homogeneous transforms and interpret the result.

```python
import numpy as np

R1 = np.array([[0, -1],
               [1,  0]])         # 90° rotation
t1 = np.array([1, 0])
T1 = np.block([[R1, t1[:, None]],
               [0, 0, 1]])       # 3×3 homogeneous

R2 = np.eye(2)                   # identity rotation
t2 = np.array([0, 2])
T2 = np.block([[R2, t2[:, None]],
               [0, 0, 1]])

T_world_to_obj = T2 @ T1         # ⬅️ composition
print(T_world_to_obj)
```

> **What to do:**  
> 1. Verify the rotation part is still 90 °.  
> 2. Explain why the final translation is `[ -2, 1 ]ᵀ` (draw the frames).  

---

### Exercise 2 – Jacobian Determinant Check  

A non-zero Jacobian determinant tells us the manipulator can **generate motion in any Cartesian direction** from the current joint angles (i.e., it is *nonsingular*). At a singularity the robot **loses a degree of freedom**—important for trajectory planning and force control.

```python
import numpy as np
l1, l2 = 0.5, 0.5                # link lengths
th1, th2 = np.pi/4, np.pi/2       # joint angles

J = np.array([[-l1*np.sin(th1) - l2*np.sin(th1+th2),
               -l2*np.sin(th1+th2)],
              [ l1*np.cos(th1) + l2*np.cos(th1+th2),
                l2*np.cos(th1+th2)]])

detJ = np.linalg.det(J)
print("det J =", detJ)
```

* If `det J ≈ 0`: the arm is at or near a singular configuration—velocity commands may explode and the inverse-kinematics solution becomes ill-conditioned.  
* If `det J ≠ 0`: the arm can reach *local* Cartesian velocities in any direction; differential IK is well-behaved.

Try changing `th1`, `th2` to `[0, π]` (fully stretched). `det J` should drop to zero—why?

---

### Exercise 3 – Batch Inverse Kinematics (Vectorized)

Generate 100 random reachable end-points and compute the two-link arm joint angles *without Python loops*.

```python
import numpy as np

# workspace sampling -------------------------------------------------
n  = 100
rng = np.random.default_rng(42)
r   = rng.uniform(0.05, l1 + l2, n)      # radius
phi = rng.uniform(-np.pi, np.pi, n)      # angle
x   = r * np.cos(phi)
y   = r * np.sin(phi)

# analytic two-link IK (elbow-down) ----------------------------------
c2  = (x**2 + y**2 - l1**2 - l2**2) / (2*l1*l2)
s2  = -np.sqrt(np.clip(1 - c2**2, 0, 1))
th2 = np.arctan2(s2, c2)

k1  = l1 + l2 * c2
k2  = l2 * s2
th1 = np.arctan2(y, x) - np.arctan2(k2, k1)

angles = np.vstack((th1, th2)).T   # shape (100,2)
print(angles[:5], "...")
```

*Validate* by plugging a few pairs back into forward kinematics.

---

### Exercise 4 – Monte-Carlo Propagation

Simulate a noisy 1-D point-mass (`x = [p, v]ᵀ`) for 10 s at 1 kHz and plot the final covariance ellipse.

```python
import numpy as np
import matplotlib.pyplot as plt

dt  = 0.001
N   = int(10 / dt)
A   = np.array([[1, dt],
                [0, 1]])
Q   = np.diag([1e-6, 1e-4])        # process noise
sqrtQ = np.linalg.cholesky(Q)

M   = 5000                         # Monte-Carlo runs
x0  = np.zeros((M, 2))

for _ in range(N):
    w  = sqrtQ @ np.random.randn(2, M)
    x0 = (A @ x0.T).T + w.T        # vectorized propagation

cov = np.cov(x0.T)
print("Final covariance:\n", cov)

plt.figure()
plt.scatter(x0[:, 0], x0[:, 1], s=1, alpha=0.1)
plt.xlabel("position [m]")
plt.ylabel("velocity [m s⁻¹]")
plt.title("MC scatter after 10 s")
plt.axis("equal")
plt.show()
```

---

### Exercise 5 – Speed Challenge

Compare a pure-Python triple loop against NumPy’s BLAS-backed `dot`.

```python
import numpy as np
import time

N = 1000
A = np.random.rand(N, N)
B = np.random.rand(N, N)

# NumPy BLAS
t0 = time.perf_counter()
C = A @ B
t1 = time.perf_counter()
print(f"NumPy  {t1-t0:.3f} s")

# naive Python
C_py = np.zeros_like(C)
t0 = time.perf_counter()
for i in range(N):
    for j in range(N):
        s = 0.0
        for k in range(N):
            s += A[i, k] * B[k, j]
        C_py[i, j] = s
t1 = time.perf_counter()
print(f"Python {t1-t0:.3f} s")
```

You should observe a **1000×–10 000×** speed-up—courtesy of vectorization, cache-friendly layout, and optimized BLAS kernels.

---
