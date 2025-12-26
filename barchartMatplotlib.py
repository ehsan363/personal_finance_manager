from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

def initiation():
    figure = Figure()  # Blank canvas
    canvas = FigureCanvas(figure) # Convertion of canvas for Qt widget
    return figure, canvas
def plot_bar_chart(figure, canvas):
    income = {
        'Jan': 25,
        "Feb": 25,
        "Mar": 25,
        "Apr": 25,
        'May': 25,
        'Jun': 25,
        'Jul': 25,
        'Aug': 25,
        'Sep': 25,
        'Oct': 25,
        'Nov': 25,
        'Dec': 25
    }
    expense = {
        'Jan': 20,
        "Feb": 20,
        "Mar": 20,
        "Apr": 20,
        'May': 20,
        'Jun': 20,
        'Jul': 20,
        'Aug': 20,
        'Sep': 20,
        'Oct': 20,
        'Nov': 20,
        'Dec': 20
    }

    ax = figure.add_subplot(111)  # <-- Don't use during update
    ax.clear()
    ax.bar(income.keys(), income.values())
    ax.bar(expense.keys(), expense.values())
    canvas.draw()