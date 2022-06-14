from flask import Flask, render_template, url_for, Markup
from plot import get_chart, pnf_text, scale

app = Flask(__name__)

# The next parameters will be selected by web form:
box_size = 10
reversal_size = 3
# scale = generate_scale(start=np.floor(price_data['Low'].min()), end=np.ceil(price_data['High'].max()), box_size=box_size)
# scale = np.arange(260,430, 10)


@app.route("/")
@app.route("/home")
def home():
    columns = get_chart()
    chart = pnf_text(scale, columns)
    chart = chart.split('\n')
    return render_template('home.html', title="XOX - Point-And-Figure", chart=chart)

@app.route("/about")
def about():
    return render_template('about.html', title="XOX-PnF - About")


if __name__ == "__main__":
    app.run(debug=True)