import matplotlib.pyplot as plt


def plot_pie(data: dict) -> None:
    labels = data.keys()
    amount = data.values()
    explode = (0.1, 0, 0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(amount, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')

    plt.show()


def plot_column(data: dict) -> None:
    category = data.keys()
    amount = data.values()
    plt.bar(category, amount)
    plt.show()


def plot_charts(data: dict) -> None:
    category = data.keys()
    amount = data.values()
    explode = tuple([0 for _ in range(len(category))])
    fig1, (p, c) = plt.subplots(1, 2)

    # pie chart
    p.pie(amount, explode=explode, labels=category, autopct='%1.1f%%',
          shadow=True, startangle=90)
    p.axis('equal')

    # bar chart
    c.bar(category, amount)

    plt.show()
