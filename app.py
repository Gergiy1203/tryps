from flask import Flask

app = Flask(__name__)

def init_db():
     conn = sqlie3.connect('orders.db')
     c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY,name TEXT,phone TEXT,details TEXT)'''):
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        details = request.form.get("details")

        if not name or not phone:
            return "Fill required fields"

        conn = sqlite3.connect('orders.db')
        c = conn.cursor()
        c.execute("INSERT INTO orders (name, phone, details) VALUES (?, ?, ?)",
                  (name, phone, details))
        conn.commit()
        conn.close()

        return redirect("/orders")

    return render_template("index.html")


@app.route("/orders")
def orders():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("SELECT * FROM orders ORDER BY id DESC")
    data = c.fetchall()
    conn.close()

    return render_template("orders.html", orders=data)


if name == "main":
    init_db()
    app.run(host="0.0.0.0", port=5000)
