import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Matplotlib Style Gallery: https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
plt.style.use('ggplot')

x_sicaklik = []
y_sicaklik = []
x_yukseklik = []
y_yukseklik = []
x_basinc = []
y_basinc = []
x_nem = []
y_nem = []
x_hiz = []
y_hiz = []
x_dayaniklilik = []
y_dayaniklilik = []

plt.plot(x_sicaklik, y_sicaklik)
plt.plot(y_yukseklik, y_yukseklik)
plt.plot(y_basinc, y_basinc)
plt.plot(x_nem, y_nem)
plt.plot(x_hiz, y_hiz)
plt.plot(x_dayaniklilik, y_dayaniklilik)


index = count()

i = 0


def animate(i):
    x_sicaklik.append(i)
    y_sicaklik.append(random.randint(0, 50))

    x_yukseklik.append(i)
    y_yukseklik.append(random.randint(0, 500))

    x_basinc.append(i)
    y_basinc.append(random.randint(0, 100))

    x_nem.append(i)
    y_nem.append(random.randint(0, 10))

    x_hiz.append(i)
    y_hiz.append(random.randint(0, 20))

    x_dayaniklilik.append(i)
    y_dayaniklilik.append(random.randint(0, 30))

    plt.subplot(2, 3, 1)
    plt.plot(x_sicaklik, y_sicaklik, color='r')
    plt.xlabel('Süre(sn)')
    plt.ylabel('Sıcaklık')
    plt.title('Sıcaklık (C)', color='r')

    plt.subplot(2, 3, 2)
    plt.plot(x_yukseklik, y_yukseklik, color='blue')
    plt.xlabel('Süre(sn)')
    plt.ylabel('Yükselik')
    plt.title('Yükseklik')

    plt.subplot(2, 3, 3)
    plt.plot(x_basinc, y_basinc, color='blue')
    plt.xlabel('Süre(sn)')
    plt.ylabel('Basinc')
    plt.title('Basinc')

    plt.subplot(2, 3, 4)
    plt.plot(x_nem, y_nem, color='blue')
    plt.xlabel('Süre(sn)')
    plt.ylabel('Nem')
    plt.title('Nem')

    plt.subplot(2, 3, 5)
    plt.plot(x_hiz, y_hiz, color='blue')
    plt.xlabel('Süre(sn)')
    plt.ylabel('Hız')
    plt.title('Hız')

    plt.subplot(2, 3, 6)
    plt.plot(x_dayaniklilik, y_dayaniklilik, color='blue')
    plt.xlabel('Süre(sn)')
    plt.ylabel('Dayanıklılık')
    plt.title('Dayanıklılık')

    i += 1


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
