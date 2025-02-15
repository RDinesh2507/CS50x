CS50x Final Project - Pet Adoption Web Application:

Project Overview:

The Pet Adoption Web Application is a simple yet powerful platform designed to help users adopt pets online. This web-based application allows users to view available pets, learn about their breed, age, and more, and submit adoption requests. The backend is powered by Python using the Flask framework, while the frontend is developed using HTML, CSS, and JavaScript. The application uses an SQL database to store pet details and adoption requests, which facilitates interaction between users and the pets available for adoption.

Project Structure:

The project is divided into several components that handle different tasks. The main files in the project include:

index.html (Frontend - HTML) styles.css (Frontend - CSS) app.js (Frontend - JavaScript) app.py (Backend - Python/Flask) pets.db (Database - SQLite)

Each of these files plays an important role in the functionality of the web application, providing both the user interface and server-side logic.

File Breakdown:

index.html (Frontend - HTML):
The index.html file is the core of the application’s frontend. It contains the HTML structure of the application, defining the layout and sections visible to the user. The file has two main sections:

Pets List Section: This section displays available pets for adoption. Each pet is represented by a card containing details like the pet's name, breed, age, and an image of the pet. A button labeled “Adopt Now” allows the user to express interest in adopting the pet.

Adopt Form Section: Below the pets list, there is a form where users can input their name and the pet ID they want to adopt. The form allows users to submit an adoption request, sending the data to the backend for processing.

The form is simple but effective, capturing the necessary information for adoption requests while maintaining a clean and user-friendly design.

styles.css (Frontend - CSS):
The styles.css file is used to style the HTML components. It defines the appearance of the elements, such as the layout, color scheme, typography, and buttons. Key styling decisions include:

Color Scheme: The color scheme of the application is kept simple, using green for buttons and headers to evoke a sense of calmness, nature, and well-being — suitable for a pet adoption website. The footer is styled with a dark color to visually separate it from the rest of the page.

Pet Card Design: The pet cards are designed with a clean white background and a border radius to give them a soft, approachable feel. The images of the pets are set to be fully responsive to fit within the card, ensuring that they display correctly regardless of the screen size.

Form Styling: The form inputs are styled for clarity and accessibility. The buttons are large and have hover effects, making them easy to click.

app.js (Frontend - JavaScript):
The app.js file handles the client-side functionality of the application. It manages the dynamic aspects of the web page, such as fetching pet data from the backend and submitting adoption requests.

Fetching Pets: When the page loads, the JavaScript fetches data from the backend (Flask server) by making a GET request to the /pets route. The response is expected to be a list of available pets, which is dynamically rendered as cards on the page.

Adoption Requests: When the user fills out the adoption form and clicks the "Adopt" button, the JavaScript submits the form data to the backend using a POST request. The request includes the user’s name and the ID of the pet they wish to adopt. After submission, the form is reset, and the user is shown a message indicating the success or failure of their adoption request.

app.py (Backend - Python/Flask):
The app.py file serves as the backend of the application, using the Flask framework to handle incoming requests and serve data to the frontend. The backend consists of two main routes:

GET /pets: This route is responsible for fetching the list of pets available for adoption from the database. It queries the database for pets marked as "not adopted" and returns a JSON response containing the pet details (name, breed, age, image, etc.).

POST /adopt: This route handles the submission of adoption requests. When a user submits the adoption form, the backend receives the data (name and pet ID), checks if the pet is available for adoption, and creates an entry in the AdoptionRequest table. It also marks the pet as adopted in the Pet table.

The Flask app uses SQLAlchemy to interact with the SQLite database, which stores pet and adoption request data. The app is simple but highly functional, ensuring that pet adoption requests are properly stored and processed.

pets.db (Database - SQLite):
The pets.db file is the SQLite database used to store pet and adoption data. It consists of two tables:

Pet: This table stores information about each pet, such as its name, breed, age, image URL, and adoption status (whether the pet is available for adoption or not).

AdoptionRequest: This table stores details about each adoption request, including the user’s name and the pet they wish to adopt. The database is created and initialized automatically by the Flask app when it is first run.

Design Choices While developing this project, I made several key design choices that were aimed at ensuring simplicity, functionality, and usability.

Database Choice: I chose SQLite as the database because it is lightweight, easy to set up, and sufficient for a small-scale project like this. While MySQL or PostgreSQL might be better suited for production-level applications with more traffic, SQLite was an appropriate choice given the scope of this project.

UI/UX Design: The UI of the application is designed to be clean and minimalistic, with a focus on the core functionality: pet adoption. I decided to use simple cards to display pet details because they are easy to read and visually appealing. The decision to keep the layout responsive ensures that users have a good experience across devices.

Adoption Flow: I implemented the adoption flow as a simple form submission, where the user inputs their name and the pet’s ID. While I could have added more complex features like user authentication or detailed pet profiles, I opted for simplicity in this version of the app to ensure that the core functionality was implemented effectively.

JavaScript for Interactivity: JavaScript is used to make the website interactive without needing to reload the page. This decision improves the user experience by ensuring that pet details are loaded dynamically and adoption requests are handled seamlessly.

Conclusion:

In summary, the Pet Adoption Web Application provides a simple and effective platform for users to browse pets available for adoption and submit adoption requests. By using a combination of HTML, CSS, JavaScript, Python (Flask), and SQLite, this project demonstrates core web development concepts, including frontend-backend interaction, database management, and form submission. While the design is simple, it is fully functional, and I am excited about the potential to expand and improve this application in the future.





