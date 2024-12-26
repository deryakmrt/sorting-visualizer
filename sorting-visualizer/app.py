from flask import Flask, render_template, jsonify
import random
from sorting_algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, heap_sort, radix_sort

app = Flask(__name__)

# 1-100 arasinda rastgele 20 sayi uret
def generate_random_data():
    return [random.randint(1, 100) for _ in range(20)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-random-data')
def get_random_data():
    random_data = generate_random_data()
    return jsonify(random_data)

@app.route('/sort/<algorithm>', methods=['POST'])
def sort_data(algorithm):
    data = generate_random_data()
    steps = []

    if algorithm == 'bubble':
        steps = bubble_sort(data)
    elif algorithm == 'insertion':
        steps = insertion_sort(data)
    elif algorithm == 'selection':
        steps = selection_sort(data)
    elif algorithm == 'merge':
        steps = merge_sort(data)
    elif algorithm == 'heap':
        steps = heap_sort(data)
    elif algorithm == 'radix':
        steps = radix_sort(data)

    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)
