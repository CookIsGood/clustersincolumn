import numpy as np
import matplotlib.pyplot as plt


def create_matrix(run=True):
    if run:
        # X - исходная матрица
        X = np.random.randint(0, 2, (10, 10))  # (2, 10) - 1 число кол-во строк 2 число кол-во столбцов
        np.savetxt('matrix.npy', X)
        return X

%hello misha
def load_matrix(run=True):
    if run:
        X = np.loadtxt('matrix.npy')
        return X


def calc_str(X):
    b = np.argwhere(X)
    b_size = b.shape
    str = b_size[0]
    num_clusters = 0
    curr = 0
    liner = 0
    clustinline = np.zeros((X.shape[0]))
    maxline = np.zeros((X.shape[0]))
    random_colors = np.random.random((str, 3))
    color = np.zeros((str, 3))
    length = 0
    for k in range(str):
        curr += 1
        if (b[k, 0] == b[k - 1, 0]) and (b[k, 1] == b[k - 1, 1] + 1):
            curr -= 1
            length += 1
        else:
            if b[k, 0] != b[k - 1, 0]:
                length = 0
            if length > maxline[b[k, 0]]:
                maxline[b[k, 0]] = length
            length = 0
            num_clusters += 1
            liner += 1
            length += 1
        if length > maxline[b[k, 0]]:
            maxline[b[k, 0]] = length
        if b[k, 1] == X.shape[1] - 1:
            if length > maxline[b[k, 0]]:
                maxline[b[k, 0]] = length
                length = 0
        if b[k, 0] != b[k - 1, 0]:
            clustinline[b[k - 1, 0]] = liner
            liner = 0
        color[k, :] = random_colors[curr, :]
    clustinline[X.shape[0] - 1] = (num_clusters - (np.sum(clustinline) - 1))
    print("Количество кластеров")
    print(num_clusters)
    # print(color)
    print("Количество кластеров в линии")
    print(clustinline)
    print("Макс длина")
    print(maxline)
    plt.title("Кластеризация")
    plt.xlabel("Номер полосы")
    plt.ylabel("Время")
    plt.scatter(b[:, 0], b[:, 1], c=color)
    plt.show()


def plot_to_iter(X, max_iter=2):
    size_X = np.shape(X)
    sizex = size_X[0]
    print("Количество повторений", max_iter)
    number_speed = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    print("Массив скоростей", number_speed)
    for i in range(max_iter):
        for k in range(sizex):
            X[k, :] = np.roll(X[k, :], number_speed[k])
        print("Матрица после смещения. Итерация номер", i)
        print(X)
        calc_str(X)


def main():
    create_matrix(run=False)
    X = load_matrix(run=True)
    print("Матрицы до алгоритма")
    print(X)
    X_rotate = X.swapaxes(0, 1)
    print("Перевернутая матрица")
    print(X_rotate)
    x1 = np.argwhere(X_rotate)
    plt.title("Исходная матрица")
    plt.xlabel("Номер полосы")
    plt.ylabel("Время")
    plt.scatter(x1[:, 0], x1[:, 1])
    plt.show()
    calc_str(X_rotate)
    plot_to_iter(X_rotate, max_iter=2)


if __name__ == '__main__':
    main()
