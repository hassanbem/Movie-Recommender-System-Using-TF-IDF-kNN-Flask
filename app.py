@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    query = ""
    if request.method == "POST":
        query = request.form.get("movie")
        recommendations = recommend_movie(query, 5)
    return render_template("index.html", recommendations=recommendations, query=query)

# ----------------------------
# 4. Run App
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
