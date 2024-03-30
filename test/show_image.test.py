import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 初始化数据
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [3, 4, 3, 2, 5, 6, 5, 4, 7]


def show_last_image(x, y):
    # 创建图形和坐标轴
    fig, ax = plt.subplots()
    # 绘制初始折线
    (line,) = ax.plot(x, y)

    # 更新函数，用于更新折线
    def update_line(frame):
        line.set_xdata(x[: frame + 1])
        line.set_ydata(y[: frame + 1])
        return (line,)

    def init_func():
        # line.set_data(x, y)
        line.set_data([], [])
        return (line,)

    def show_image():
        # 初始化动画
        ani = animation.FuncAnimation(
            fig,
            update_line,
            init_func=init_func,
            frames=range(len(x)),
            interval=1,
        )
        # 显示图表
        plt.show()

    return show_image()


show_last_image(x, y)
