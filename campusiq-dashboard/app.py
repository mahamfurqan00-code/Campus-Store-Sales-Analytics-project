from flask import Flask, render_template, request, jsonify, Response
from analytics import load_sales, filter_sales, summarize_sales, chart_data
import io

app = Flask(__name__)
DATA = "data/sales.csv"

def current_data():
    return filter_sales(load_sales(DATA), request.args.get("start"), request.args.get("end"),
                        request.args.get("category"), request.args.get("region"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/dashboard")
def dashboard():
    df = current_data()
    raw = load_sales(DATA)
    return jsonify({"summary": summarize_sales(df), "charts": chart_data(df),
                    "filters": {"categories": sorted(raw.category.unique()),
                                "regions": sorted(raw.region.unique())}})

@app.route("/api/export")
def export():
    out = io.StringIO()
    current_data().to_csv(out, index=False)
    return Response(out.getvalue(), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=campusiq_sales.csv"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
