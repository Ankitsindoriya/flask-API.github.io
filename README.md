# flask-API.github.io
This Python script is a basic implementation of a Flask web application that provides two routes using the Flask framework. Here's a description of what each part of the code does:

Importing Required Libraries:
The script begins by importing the necessary libraries. Flask is imported from the flask module to create the web application, and jsonify is imported to convert Python dictionaries into JSON format.

Creating the Flask App:
The app object is created using Flask(__name__). This object will represent the web application.

Defining Routes:
The script defines two routes using the @app.route decorator. Routes are URL paths that users can access in the web application.

Route 1 ('/'): This route responds with a simple "Hello, World!" message when a user accesses the root URL.

Route 2 ('/armstrong/<int:n>'): This dynamic route takes an integer n as a URL parameter. The function armstrong(n) calculates whether the given number is an Armstrong number or not. It does this by computing the sum of the digits raised to the power of the number of digits in the original number. If the sum matches the original number, it's an Armstrong number. A JSON response is returned containing information about the number's Armstrong status and a mock "server ip" value.

Armstrong Number Calculation:
The armstrong(n) function calculates whether the given number n is an Armstrong number. It calculates the sum of the digits raised to the power of the number of digits in the original number. If the sum matches the original number, it's an Armstrong number. The function constructs a dictionary containing information about the number, its Armstrong status, and a mock "server ip."

Running the App:
The if __name__ == "__main__": block ensures that the web application is only run when the script is executed directly (not imported as a module). It starts the app with debugging enabled, allowing for easy error detection.

Overall, this script creates a simple Flask web application with two routes. One route displays a "Hello, World!" message, while the other route takes an integer input, checks if it's an Armstrong number, and returns a JSON response with relevant information. Please note that the "server ip" values are hardcoded and should be replaced with actual server information if this code were used in a real-world scenario.
