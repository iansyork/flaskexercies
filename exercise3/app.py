from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded list of organizations
ORGANIZATIONS = ["Organization A", "Organization B", "Organization C", "Organization D", "Organization E"]

# Global dictionary to store registered users
registered_users = {}

# Home page with registration form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']
        if not name:
            error = 'Name is required'
        elif not organization:
            error = 'Organization is required'
        elif organization not in ORGANIZATIONS:
            error = 'Invalid organization'
        elif name in registered_users:
            error = 'User already registered'
        else:
            registered_users[name] = organization
            return redirect(url_for('registered'))
        return render_template('home.html', organizations=ORGANIZATIONS, error=error)
    else:
        return render_template('home.html', organizations=ORGANIZATIONS)


# Registered users page
@app.route('/registered')
def registered():
    return render_template('registered.html', registered_users=registered_users)


if __name__ == '__main__':
    app.run(debug=True)

