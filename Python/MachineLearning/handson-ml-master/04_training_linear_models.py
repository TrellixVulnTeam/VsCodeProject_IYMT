'''
------------------------------------------------------------------------------------------------------------------------
Setup
------------------------------------------------------------------------------------------------------------------------
'''
# Common imports
import numpy as np
import os

# to make this notebook's output stable across runs
np.random.seed(42)

# To plot pretty figures
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

CHAPTER_ID = "training_linear_models"

def save_fig(fig_id, tight_layout=True):
    path = "python/MachineLearning/handson-ml-master/images/" + CHAPTER_ID + fig_id + ".png"
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format='png', dpi=300)

# Ignore useless warnings (see SciPy issue #5998)
import warnings
warnings.filterwarnings(action="ignore", message="^internal gelsd")

'''
------------------------------------------------------------------------------------------------------------------------
4.1 Linear regression
------------------------------------------------------------------------------------------------------------------------
'''
print('---------------------------------------------------------------------------------------------------------------\n'
      '                                4.1.1 Linear regression using the Normal Equation                              \n'
      '---------------------------------------------------------------------------------------------------------------\n')
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

plt.plot(X, y, "b.")
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.axis([0, 2, 0, 15])
save_fig("generated_data_plot")
plt.show()

X_b = np.c_[np.ones((100, 1)), X]  # add x0 = 1 to each instance
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print('theta_best = \n{0}'.format(theta_best))
print()

print('---< predict data at x = 0 and at x = 2. >---')
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]  # add x0 = 1 to each instance
y_predict = X_new_b.dot(theta_best)
print('y_predict = \n{0}'.format(y_predict))

plt.plot(X_new, y_predict, "r-")
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()
print()

print('---< These caluculation is tarasformed at sklearn. >---')
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
print('lin.leg.intercept_ = {0} \n lin_reg.coef_ = {1}\n'.format(lin_reg.intercept_, lin_reg.coef_))
print()
print('---< predict data with new data. >---')
print('lin_reg.predict(X_new) = \n{0}'.format(lin_reg.predict(X_new)))
print()

'''
The LinearRegression class is based on the scipy.linalg.lstsq() function (the name stands for "least squares"),
 which you could call directly:
'''
theta_best_svd, residuals, rank, s = np.linalg.lstsq(X_b, y, rcond=1e-6)
print('theta_best_svd = \n{0}'.format(theta_best_svd))
print()

'''
This function computes  𝐗+𝐲 , where  𝐗+  is the pseudoinverse of  𝐗  (specifically the Moore-Penrose inverse).
 You can use np.linalg.pinv() to compute the pseudoinverse directly:
'''
print('np.linalg.pinv(X_b).dot(y) = \n{0}'.format(np.linalg.pinv(X_b).dot(y)))
print()

'''
------------------------------------------------------------------------------------------------------------------------
4.2 grandient descent
------------------------------------------------------------------------------------------------------------------------
'''
print('---------------------------------------------------------------------------------------------------------------\n'
      '                             4.2.1 Linear regression using batch gradient descent                              \n'
      '---------------------------------------------------------------------------------------------------------------\n')
eta = 0.1
n_iterations = 1000
m = 100
theta = np.random.randn(2,1)

for iteration in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - eta * gradients

print('theta = \n{0}'.format(theta))
print()

print('---< predict y data at x = 0 ans x = 2. >---')
print('X_new_b.dot(theta) = \n{0}'.format(X_new_b.dot(theta)))
print()

print('---------------------------------------------------------------------------------------------------------------\n'
      '                             Gradient descent at various learning rates                                        \n'
      '---------------------------------------------------------------------------------------------------------------\n')

theta_path_bgd = []

def plot_gradient_descent(theta, eta, theta_path=None):
    m = len(X_b)
    plt.plot(X, y, "b.")
    n_iterations = 1000
    for iteration in range(n_iterations):
        if iteration < 10:
            y_predict = X_new_b.dot(theta)
            style = "b-" if iteration > 0 else "r--"
            plt.plot(X_new, y_predict, style)
        gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
        theta = theta - eta * gradients
        if theta_path is not None:
            theta_path.append(theta)
    plt.xlabel("$x_1$", fontsize=18)
    plt.axis([0, 2, 0, 15])
    plt.title(r"$\eta = {}$".format(eta), fontsize=16)

np.random.seed(42)
theta = np.random.randn(2,1)  # random initialization

plt.figure(figsize=(10,4))
plt.subplot(131); plot_gradient_descent(theta, eta=0.02)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.subplot(132); plot_gradient_descent(theta, eta=0.1, theta_path=theta_path_bgd)
plt.subplot(133); plot_gradient_descent(theta, eta=0.5)

save_fig("gradient_descent_plot")
plt.show()
print()

'''
------------------------------------------------------------------------------------------------------------------------
4.2.2 Stochastic Gradient Descent
------------------------------------------------------------------------------------------------------------------------
'''
print('---------------------------------------------------------------------------------------------------------------\n'
      '                                   4.2.2-1 Stochastic Gradient Descent                                         \n'
      '---------------------------------------------------------------------------------------------------------------\n')
theta_path_sgd = []
m = len(X_b)
np.random.seed(42)

n_epochs = 50
t0, t1 = 5, 50  # learning schedule hyperparameters

def learning_schedule(t):
    return t0 / (t + t1)

theta = np.random.randn(2,1)  # random initialization

for epoch in range(n_epochs):
    for i in range(m):
        if epoch == 0 and i < 20:                    # not shown in the book
            y_predict = X_new_b.dot(theta)           # not shown
            style = "b-" if i > 0 else "r--"         # not shown
            plt.plot(X_new, y_predict, style)        # not shown
        random_index = np.random.randint(m)
        xi = X_b[random_index:random_index+1]
        yi = y[random_index:random_index+1]
        gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
        eta = learning_schedule(epoch * m + i)
        theta = theta - eta * gradients
        theta_path_sgd.append(theta)                 # not shown

plt.plot(X, y, "b.")                                 # not shown
plt.xlabel("$x_1$", fontsize=18)                     # not shown
plt.ylabel("$y$", rotation=0, fontsize=18)           # not shown
plt.axis([0, 2, 0, 15])                              # not shown
save_fig("sgd_plot")                                 # not shown
plt.show()                                           # not shown
print()

print('theta = \n{0}'.format(theta))
print()

print('---------------------------------------------------------------------------------------------------------------\n'
      '                   4.2.2-2 Stochastic Gradient Descent with scikit-learn                                       \n'
      '---------------------------------------------------------------------------------------------------------------\n')
from sklearn.linear_model import SGDRegressor
sgd_reg = SGDRegressor(max_iter=50, tol=-np.infty, penalty=None, eta0=0.1, random_state=42)
sgd_reg.fit(X, y.ravel())

print('sgd_reg.intercept_ = {0}, sgd_reg.coef_ = {1}'.format(sgd_reg.intercept_, sgd_reg.coef_))
print()

'''
------------------------------------------------------------------------------------------------------------------------
4.2.3 Mini-batch gradient descent
------------------------------------------------------------------------------------------------------------------------
'''
print('---------------------------------------------------------------------------------------------------------------\n'
      '                                   4.2.3 Mini-batch gradient descent                                           \n'
      '---------------------------------------------------------------------------------------------------------------\n')
theta_path_mgd = []

n_iterations = 50
minibatch_size = 20

np.random.seed(42)
theta = np.random.randn(2,1)  # random initialization

t0, t1 = 200, 1000
def learning_schedule(t):
    return t0 / (t + t1)

t = 0
for epoch in range(n_iterations):
    shuffled_indices = np.random.permutation(m)
    X_b_shuffled = X_b[shuffled_indices]
    y_shuffled = y[shuffled_indices]
    for i in range(0, m, minibatch_size):
        t += 1
        xi = X_b_shuffled[i:i+minibatch_size]
        yi = y_shuffled[i:i+minibatch_size]
        gradients = 2/minibatch_size * xi.T.dot(xi.dot(theta) - yi)
        eta = learning_schedule(t)
        theta = theta - eta * gradients
        theta_path_mgd.append(theta)

print('theta = \n{0}'.format(theta))
print()

theta_path_bgd = np.array(theta_path_bgd)
theta_path_sgd = np.array(theta_path_sgd)
theta_path_mgd = np.array(theta_path_mgd)

plt.figure(figsize=(7,4))
plt.plot(theta_path_sgd[:, 0], theta_path_sgd[:, 1], "r-s", linewidth=1, label="Stochastic")
plt.plot(theta_path_mgd[:, 0], theta_path_mgd[:, 1], "g-+", linewidth=2, label="Mini-batch")
plt.plot(theta_path_bgd[:, 0], theta_path_bgd[:, 1], "b-o", linewidth=3, label="Batch")
plt.legend(loc="upper left", fontsize=16)
plt.xlabel(r"$\theta_0$", fontsize=20)
plt.ylabel(r"$\theta_1$   ", fontsize=20, rotation=0)
plt.axis([2.5, 4.5, 2.3, 3.9])
save_fig("gradient_descent_paths_plot")
plt.show()
print()

'''
------------------------------------------------------------------------------------------------------------------------
4.3 Polynomial regression
------------------------------------------------------------------------------------------------------------------------
'''
print('---------------------------------------------------------------------------------------------------------------\n'
      '                                      4.3 Polynomial regression                                                \n'
      '---------------------------------------------------------------------------------------------------------------\n')
import numpy as np
import numpy.random as rnd

np.random.seed(42)

m = 100
X = 6 * np.random.rand(m, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(m, 1)

plt.plot(X, y, "b.")
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.axis([-3, 3, 0, 10])
save_fig("quadratic_data_plot")
plt.show()
print()

'''
Using scikit-learn's PolynomialFeatures Class, add the square of each feature to the training set as a new feature.
'''
from sklearn.preprocessing import PolynomialFeatures
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)
print('X[0] = {0}'.format(X[0]))
print()

print('X_poly[0] = {0}'.format(X_poly[0]))
print()

lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)

print('lin_reg.intercept_ = {0}, lin_reg.coef_ = {1}'.format(lin_reg.intercept_, lin_reg.coef_))
print()

X_new=np.linspace(-3, 3, 100).reshape(100, 1)
X_new_poly = poly_features.transform(X_new)
y_new = lin_reg.predict(X_new_poly)
plt.plot(X, y, "b.")
plt.plot(X_new, y_new, "r-", linewidth=2, label="Predictions")
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.legend(loc="upper left", fontsize=14)
plt.axis([-3, 3, 0, 10])
save_fig("quadratic_predictions_plot")
plt.show()
print()

'''
------------------------------------------------------------------------------------------------------------------------
4.4 Learning curve
------------------------------------------------------------------------------------------------------------------------
'''
print('---------------------------------------------------------------------------------------------------------------\n'
      '                                         4.4 Learning curve                                                    \n'
      '---------------------------------------------------------------------------------------------------------------\n')
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

for style, width, degree in (("g-", 1, 300), ("b--", 2, 2), ("r-+", 2, 1)):
    polybig_features = PolynomialFeatures(degree=degree, include_bias=False)
    std_scaler = StandardScaler()
    lin_reg = LinearRegression()
    polynomial_regression = Pipeline([
            ("poly_features", polybig_features),
            ("std_scaler", std_scaler),
            ("lin_reg", lin_reg),
        ])
    polynomial_regression.fit(X, y)
    y_newbig = polynomial_regression.predict(X_new)
    plt.plot(X_new, y_newbig, style, label=str(degree), linewidth=width)

plt.plot(X, y, "b.", linewidth=3)
plt.legend(loc="upper left")
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.axis([-3, 3, 0, 10])
save_fig("high_degree_polynomials_plot")
plt.show()
print()

print('---< Given a training set, define a function that draws the learning curve of the model. >---')
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def plot_learning_curves(model, X, y):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=10)
    train_errors, val_errors = [], []
    for m in range(1, len(X_train)):
        model.fit(X_train[:m], y_train[:m])
        y_train_predict = model.predict(X_train[:m])
        y_val_predict = model.predict(X_val)
        train_errors.append(mean_squared_error(y_train[:m], y_train_predict))
        val_errors.append(mean_squared_error(y_val, y_val_predict))

    plt.plot(np.sqrt(train_errors), "r-+", linewidth=2, label="train")
    plt.plot(np.sqrt(val_errors), "b-", linewidth=3, label="val")
    plt.legend(loc="upper right", fontsize=14)   # not shown in the book
    plt.xlabel("Training set size", fontsize=14) # not shown
    plt.ylabel("RMSE", fontsize=14)              # not shown

lin_reg = LinearRegression()
plot_learning_curves(lin_reg, X, y)
plt.axis([0, 80, 0, 3])                         # not shown in the book
save_fig("underfitting_learning_curves_plot")   # not shown
plt.show()                                      # not shown
print()

from sklearn.pipeline import Pipeline

polynomial_regression = Pipeline([
        ("poly_features", PolynomialFeatures(degree=10, include_bias=False)),
        ("lin_reg", LinearRegression()),
    ])

plot_learning_curves(polynomial_regression, X, y)
plt.axis([0, 80, 0, 3])           # not shown
save_fig("learning_curves_plot")  # not shown
plt.show()                        # not shown
print()

'''
------------------------------------------------------------------------------------------------------------------------
4.5 Regularized models
------------------------------------------------------------------------------------------------------------------------
'''
print('---------------------------------------------------------------------------------------------------------------\n'
      '                                       4.5.1 Ridge regression                                                  \n'
      '---------------------------------------------------------------------------------------------------------------\n')
from sklearn.linear_model import Ridge

np.random.seed(42)
m = 20
X = 3 * np.random.rand(m, 1)
y = 1 + 0.5 * X + np.random.randn(m, 1) / 1.5
X_new = np.linspace(0, 3, 100).reshape(100, 1)

def plot_model(model_class, polynomial, alphas, **model_kargs):
    for alpha, style in zip(alphas, ("b-", "g--", "r:")):
        model = model_class(alpha, **model_kargs) if alpha > 0 else LinearRegression()
        if polynomial:
            model = Pipeline([
                    ("poly_features", PolynomialFeatures(degree=10, include_bias=False)),
                    ("std_scaler", StandardScaler()),
                    ("regul_reg", model),
                ])
        model.fit(X, y)
        y_new_regul = model.predict(X_new)
        lw = 2 if alpha > 0 else 1
        plt.plot(X_new, y_new_regul, style, linewidth=lw, label=r"$\alpha = {}$".format(alpha))
    plt.plot(X, y, "b.", linewidth=3)
    plt.legend(loc="upper left", fontsize=15)
    plt.xlabel("$x_1$", fontsize=18)
    plt.axis([0, 3, 0, 4])

plt.figure(figsize=(8,4))
plt.subplot(121)
plot_model(Ridge, polynomial=False, alphas=(0, 10, 100), random_state=42)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.subplot(122)
plot_model(Ridge, polynomial=True, alphas=(0, 10**-5, 1), random_state=42)

save_fig("ridge_regression_plot")
plt.show()
print()

from sklearn.linear_model import Ridge
ridge_reg = Ridge(alpha=1, solver="cholesky", random_state=42)
ridge_reg.fit(X, y)
print('ridge_reg.predict([[1.5]]) = {0}'.format(ridge_reg.predict([[1.5]])))
print()

sgd_reg = SGDRegressor(max_iter=50, tol=-np.infty, penalty="l2", random_state=42)
sgd_reg.fit(X, y.ravel())
print('ridge_reg.predict([[1.5]]) = {0}'.format(ridge_reg.predict([[1.5]])))
print()

from sklearn.linear_model import Ridge
ridge_reg = Ridge(alpha=1, solver="sag", random_state=42)
ridge_reg.fit(X, y)
print('ridge_reg.predict([[1.5]]) = {0}'.format(ridge_reg.predict([[1.5]])))
print()

print('---------------------------------------------------------------------------------------------------------------\n'
      '                                       4.5.2 Lasso regression                                                  \n'
      '---------------------------------------------------------------------------------------------------------------\n')
from sklearn.linear_model import Lasso

plt.figure(figsize=(8,4))
plt.subplot(121)
plot_model(Lasso, polynomial=False, alphas=(0, 0.1, 1), random_state=42)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.subplot(122)
plot_model(Lasso, polynomial=True, alphas=(0, 10**-7, 1), tol=1, random_state=42)

save_fig("lasso_regression_plot")
plt.show()
print()

