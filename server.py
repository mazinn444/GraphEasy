from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)
version = "1.0.0"

def calcular_grafico(a, b, c):
    try:
        a, b, c = map(float, (a, b, c))

        delta = b**2 - 4*a*c
        if delta < 0:
            resultado = "A equação não possui raízes reais."
            x1 = x2 = None
        else:
            x1 = (-b + np.sqrt(delta)) / (2 * a)
            x2 = (-b - np.sqrt(delta)) / (2 * a)

            plt.clf()
            x = np.linspace(min(x1, x2) - 1, max(x1, x2) + 1, 400)
            y = a * x**2 + b * x + c
            plt.plot(x, y, label=f'{a:.1f}x² + {b:.1f}x + {c:.1f}')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Gráfico da Função Quadrática')
            plt.grid(True)

            if delta >= 0:
                plt.scatter([x1, x2], [0, 0], color='red', label='Raízes')

            plt.legend()
            plt.tight_layout()

            plot_path = 'static/results/output_plot.png'
            plt.savefig(plot_path, transparent=True)
            resultado = plot_path

        return resultado, x1, x2

    except ValueError:
        return "Por favor, insira números válidos.", None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')
        c = request.form.get('c')
        resultado, x1, x2 = calcular_grafico(a, b, c)
        return render_template('index.html', resultado=resultado, x1=x1, x2=x2,version=version)
    return render_template('index.html', resultado=None, version=version)

@app.route('/sobre')
def about():
    return render_template('about.html')

@app.route('/error-500')
def errorpage():
    return render_template('InternalErrorPage.html')

@app.errorhandler(404)
def pagenotfound(error):
    return redirect(url_for('index'))

@app.errorhandler(500)
def internalerror(error):
    return redirect(url_for('errorpage'))

if __name__ == '__main__':
    app.run(debug=True)
