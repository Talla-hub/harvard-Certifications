import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    purchases = db.execute(
        "SELECT symbol, name, price, quantity, total_price FROM purchases WHERE user_id = ? ", session["user_id"])
    initial_cash = db.execute("SELECT cash FROM users")[0]['cash']
    total = db.execute(f"SELECT SUM(total_price)as total FROM purchases WHERE user_id = {
                       session["user_id"]}")[0]['total']
    cash = round(initial_cash-total, 2)
    return render_template("index.html", purchases=purchases, cash=f"{cash:,}", TOTAL=f"{round(total+cash, 2):,}")
    # return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_quantity = request.form.get("shares")
        if not symbol or lookup(symbol) == None:
            return apology("the stock doesn't exist")
        total_price = float(lookup(symbol)["price"])*float(shares_quantity)
        initial_cash = db.execute("SELECT cash FROM users")[0]['cash']
        total = db.execute(f"SELECT SUM(total_price)as total FROM purchases WHERE user_id = {
                           session["user_id"]}")[0]['total']
        if (initial_cash < total + (total_price)):
            return apology("You can't afford these shares")
        symbol_tab = db.execute("SELECT symbol FROM purchases")
        for key1 in symbol_tab:
            if symbol == key1['symbol']:
                k = db.execute(f"SELECT quantity FROM purchases WHERE symbol='{
                               key1['symbol']}'")
                total_price = float(
                    lookup(symbol)["price"])*float(k[0]['quantity']+int(shares_quantity))
                db.execute(f"UPDATE purchases SET quantity = {k[0]['quantity']+int(shares_quantity)},price=? ,total_price = ? WHERE user_id = {
                           session["user_id"]} AND symbol= '{key1['symbol']}' LIMIT 1", lookup(symbol)["price"], round(total_price, 2))
                transaction(session["user_id"],'buy',symbol,lookup(symbol)["price"],int(shares_quantity))
                return redirect(url_for('index'))

        db.execute("INSERT INTO purchases (user_id, symbol, name, price, quantity,total_price) VALUES(?,?,?,?,?,?)", session["user_id"], lookup(symbol)["symbol"], lookup(symbol)["name"],
                   lookup(symbol)["price"], int(shares_quantity), round(total_price, 2))
        transaction(session["user_id"],'buy',symbol,lookup(symbol)["price"],int(shares_quantity))
        return redirect(url_for('index'))
    return render_template("buy.html")
    # return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("""SELECT transaction_type, symbol, price, shares_quantity
                             FROM stock_transactions WHERE user_id = ? """, session["user_id"])
    if transaction:
        return render_template("history.html",transactions=transactions)

    return apology("TODO")


def transaction(user_id,type,symbol,price,quantity):
    db.execute("""INSERT INTO stock_transactions (user_id,transaction_type, symbol, price, shares_quantity)
                VALUES (?,?,?,?,?)""",user_id,type,symbol,price,quantity)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get(
                "username")
        )
        print(rows)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("the stock doesn't exist")
        return render_template("quoted.html", symbols=lookup(symbol))

    return render_template("quote.html")
    # return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    username_database = db.execute("SELECT username FROM users")
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        user_password = request.form.get("password")
        user_password_confirmation = request.form.get("confirmation")
        try:
            if not username or username in username_database:
                apologize = "Your username is blank "
                return apology(apologize)
            elif not user_password or user_password != user_password_confirmation:
                apologize = "Your password is wrong"
                return apology(apologize)
            hash_password = generate_password_hash(
                user_password, method='scrypt', salt_length=16)
            db.execute("INSERT INTO users (username,hash) VALUES(?,?)",
                       username, hash_password)
            return redirect("/login")
        except ValueError:
            apologize = "Your username is already existed"
            return apology(apologize)

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = db.execute("SELECT symbol FROM purchases")
        shares_quantity = request.form.get("shares")
        sym = request.form.get("symbol")
        for key1 in symbol:
            if sym == key1['symbol']:
                k = db.execute(f"SELECT quantity FROM purchases WHERE symbol='{
                               key1['symbol']}'")
                if (int(shares_quantity) <= k[0]['quantity']):
                    total_price = float(
                        lookup(sym)["price"])*float(k[0]['quantity']-int(shares_quantity))
                    db.execute(f"""UPDATE purchases SET quantity = {k[0]['quantity']-int(shares_quantity)},
                               price=? ,total_price = ? WHERE user_id = {
                               session["user_id"]} AND symbol= '{key1['symbol']}' LIMIT 1""",
                               lookup(sym)["price"], round(total_price, 2))
                    transaction(session["user_id"],'sell',sym,lookup(sym)["price"],int(shares_quantity))
                    return redirect(url_for('index'))
                else:
                    return apology("your quantity is not enought")

        #
        # if not symbol or lookup(symbol) == None:
        #     return apology("the stock doesn't exist")
        # total_price = float(lookup(symbol)["price"])*float(shares_quantity)
        # initial_cash=db.execute("SELECT cash FROM users")[0]['cash']
        # total=db.execute(f"SELECT SUM(total_price)as total FROM purchases WHERE user_id = {session["user_id"]}")[0]['total']
        # if (initial_cash<total + (total_price)):
        #     return apology("You can't afford these shares")
        # db.execute("INSERT INTO purchases (user_id, symbol, name, price, quantity,total_price) VALUES(?,?,?,?,?,?)", session["user_id"], lookup(symbol)["symbol"], lookup(symbol)["name"],
        #            lookup(symbol)["price"], int(shares_quantity), round(total_price,2))
        # return redirect(url_for('index'))
    return render_template("sell.html")

    # return render_template("sell.html")
    # return apology("TODO")
