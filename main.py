from flask import Flask, request

app = Flask(__name__)

logins = {}
logins["david"] = {"email": "rdlnk@example.com", "password": "baldy1"}
logins["katie"] = {"email": "rdlnk@example.com", "password": "kat12"}
logins["yul"] = {"email": "plsgq@example.com", "password": "herm1"}

@app.route("/login", methods=["POST"])
def login():
  form = request.form
  isThere = False
  details = {}
  try:
    details = logins[form["username"]]
    isThere = True
  except:
    return "Username, email, or password incorrect"
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "You are logged in"
  else:
    return "Username, email, or password incorrect"



@app.route('/')
def index():
  page = """<form method="post" action="login">
    <p>Username: <input type="text" name="username" required></p>
    <p>Email: <input type="Email" name="email" required></p>
    <p>Password: <input type="password" name="password" required></p>
    <p>Gender:
      <select name="gender">
        <option value="male">Male</option>
        <option value="female">Female</option>
        <option value="other">Other</option>
      </select>
    </p>
    <button type="submit">Login</button>
  </form>
    """
  return page

app.run(host='0.0.0.0', port=81)