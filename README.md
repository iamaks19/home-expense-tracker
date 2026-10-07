# 🏠 Home Expense Tracker

A simple web app to track daily household expenses, built with **Python (Flask), HTML, and CSS**. Expenses are stored in a plain CSV file, so no database setup is needed.

This is my first Python web project, built to learn how backend, frontend, and file storage work together.

## Features

- Add an expense with date, product, category, and amount
- Delete an expense
- Filter by month and see that month's total
- View all months at once
- Category-wise spending summary (food, travel, bills, shopping, other)
- Data is saved in `expenses.csv`, so it stays after the server is stopped
- Clean, responsive design with CSS
- Accessible from other devices (e.g. family phones) on the same home WiFi

## Tech Stack

| Part | Technology |
|---|---|
| Backend | Python 3, Flask |
| Frontend | HTML, Jinja2 templates, CSS |
| Storage | CSV file |

## Project Structure

```
Expense Tracker Project/
├── main.py              # Flask app: routes, load/save logic
├── expenses.csv         # Expense data (created automatically)
├── templates/
│   └── index.html       # Page layout (form, summary, table)
└── static/
    └── style.css        # Styling
```

## How to Run

1. Install Python 3 from [python.org](https://www.python.org/downloads/) (tick "Add Python to PATH").
2. Install Flask:
   ```
   pip install flask
   ```
3. Open a terminal in the project folder and run:
   ```
   python main.py
   ```
4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

### Use from another device on the same WiFi

1. Find your computer's IPv4 address with `ipconfig` (Windows).
2. On the other device, open `http://<your-ip>:5000`.

> **Note:** There is no login or password, so use it only on a trusted home network. Set `debug=False` in `main.py` when sharing over WiFi.

## How It Works

- `GET /` shows the expenses for the selected month (or all months with `?month=all`)
- `POST /add` reads the form, appends the new expense, and saves the CSV
- `POST /delete/<id>` removes the expense at that position in the file
- Each expense gets its real position in the file as an `id`, so deleting works correctly even when a month filter is applied

## What I Learned

- Python basics: lists, dictionaries, loops, functions
- Reading and writing CSV files
- Flask routing, GET vs POST, handling form data
- Jinja2 templating (`for` loops, variables)
- Styling with CSS
- Reading error messages and debugging

## Future Improvements

- [ ] Monthly budget with a warning when exceeded
- [ ] Edit an existing expense
- [ ] Category pie chart
- [ ] Export / backup option
- [ ] Simple login for shared use

## Screenshots

*Add a screenshot of the app here:*

```
![App screenshot](screenshot.png)
```
