import os
import csv
from datetime import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
FILE_NAME = "expenses.csv"
FIELDS = ["date", "item",  "category", "amount"]
categories =["food", "travel", "bills", "shopping", "other"]

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["amount"] = float(r["amount"])
        r["category"] = r.get("category") or "other"
    return rows

def save_expenses(expenses):
      with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


@app.route("/")
def home():
    month = request.args.get("month") or datetime.now().strftime("%Y-%m")
    all_expenses = load_expenses()

    expenses = []
    total = 0
    by_category = {}
    for i, e in enumerate(all_expenses):
        if month == "all" or e["date"].startswith(month):
             e["id"] = i
             expenses.append(e)
             total = total + e["amount"]
             cat = e["category"]
             by_category[cat] = by_category.get(cat, 0) + e["amount"]

    return render_template("index.html", expenses=expenses, total=total,
                           by_category=by_category, categories=categories,
                           month=month)
    


@app.route("/add", methods=["POST"])
def add():
    expenses = load_expenses()          # <-- Step 1: purane kharche laao
    expenses.append({
        "date": request.form["date"],
        "item": request.form["item"],
        "category": request.form["category"],
        "amount": float(request.form["amount"]),
    })                                  # <-- Step 2: naya jodo
    save_expenses(expenses)             # <-- Step 3: sab save karo
    return redirect("/")

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)
    return redirect(request.referrer or "/")


app.run(host="0.0.0.0", debug=False)