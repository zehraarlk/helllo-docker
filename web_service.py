from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mesajları listede tutuyoruz (şimdilik veritabanı yok)
mesajlar = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        isim = request.form.get("isim")
        mesaj = request.form.get("mesaj")

        if isim and mesaj:
            mesajlar.append({
                "isim": isim,
                "mesaj": mesaj
            })

        # Yeniden anasayfaya yönlendir
        return redirect(url_for("index"))

    return render_template("index.html", mesajlar=mesajlar)


if __name__ == "__main__":
    # Docker için host 0.0.0.0 olmalı
    app.run(host="0.0.0.0", port=5000, debug=True)
