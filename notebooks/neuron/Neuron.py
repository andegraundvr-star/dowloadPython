import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from sklearn.metrics import accuracy_score

# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ (вне класса) ==========

def sigmoid(z):
    """Сигмоидная функция активации"""
    return 1 / (1 + np.exp(-z))

def show_data(X, y, labels_cmap):
    """Визуализация данных"""
    plt.figure(figsize=(5, 5))
    plt.scatter(X[:, 0], X[:, 1], s=120, color=labels_cmap(y))

def generate_simple_data(N, a, b, c, max_x=5, max_y=5):
    """Генерация линейно разделимых данных"""
    np.random.seed(10)
    X = np.random.rand(N, 2)
    X[:, 0] = X[:, 0] * max_x
    X[:, 1] = X[:, 1] * max_y
    y = np.zeros(N)
    y[X[:, 0] * a + X[:, 1] * b + c > 0] = 1
    return X, y

def create_neuron(a, b, c, prob_output=False):
    """Функциональный стиль создания нейрона"""
    if prob_output:
        return lambda x: sigmoid(a*x[:, 0] + b*x[:, 1] + c)
    else:
        return lambda x: a*x[:, 0] + b*x[:, 1] + c

# ========== КЛАСС NEURON ==========

class Neuron:
    def __init__(self, a, b, c, prob_output=True):
        self.a = a
        self.b = b
        self.c = c
        self.prob_output = prob_output

    def __call__(self, x: np.ndarray) -> np.ndarray:
        assert np.ndim(x) == 2 and x.shape[1] == 2
        if self.prob_output:
            return sigmoid(self.a * x[:, 0] + self.b * x[:, 1] + self.c)
        else:
            return self.a * x[:, 0] + self.b * x[:, 1] + self.c

    def predict_class(self, x: np.ndarray) -> np.ndarray:
        prediction = self.__call__(x)
        if self.prob_output:
            return (prediction > 0.5).astype(np.int32)
        else:
            return (prediction > 0.0).astype(np.int32)

    # ДОПОЛНИТЕЛЬНЫЕ МЕТОДЫ КЛАССА (если они нужны именно как методы)
    def visualize(self, X, y, limits=((0, 5), (0, 5))):
        """Визуализация границы решения этого нейрона"""
        return show_descision_boundary(self, limits, X=X, y=y)


# ========== ДРУГИЕ ФУНКЦИИ (вне класса) ==========

def show_descision_boundary(clf, limits, binary=False, X=None, y=None,
                            n_lines=10, show_lines=False, figsize=(5, 5),
                            ax=None, labels_cmap=None, main_cmap=None):
    """Визуализация границы решения"""
    xs, ys = limits
    x_min, x_max = xs
    y_min, y_max = ys

    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))

    if ax is None:
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(1, 1, 1)

    # Исправление ошибки: было xx.ravel(), xx.ravel() - нужно xx.ravel(), yy.ravel()
    grid_points = np.c_[xx.ravel(), yy.ravel()]

    if binary:
        Z = clf.predict_class(grid_points)
        norm = Normalize(vmin=0., vmax=1.)
    else:
        Z = clf(grid_points)
        if hasattr(clf, 'prob_output') and clf.prob_output:
            norm = Normalize(vmin=0., vmax=1.)
        else:
            norm = Normalize(vmin=-10., vmax=10., clip=True)

    Z = Z.reshape(xx.shape)
    Z = Z.astype(np.float32)

    ax.contourf(xx, yy, Z, n_lines, alpha=0.4, cmap=main_cmap, norm=norm)
    if show_lines:
        cp = ax.contour(xx, yy, Z, n_lines)
        ax.clabel(cp, inline=True, fontsize=10, colors="green")

    if y is not None:
        X = np.array(X)
        y = np.array(y)
        ax.scatter(X[:, 0], X[:, 1], s=120, color=labels_cmap(y),
                   zorder=4)

def eval_clf(clf, X, y):
    """Оценка точности классификатора"""
    acc = accuracy_score(clf.predict_class(X), y)
    print(f"Accuracy {acc}")
    return acc