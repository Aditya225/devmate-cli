javascript
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON request bodies
app.use(bodyParser.json());

// Define the main route
app.get('/', (req, res) => {
    res.send('Hello World!');
});

// Define an additional route
app.get('/about', (req, res) => {
    res.send('About This App');
});

// Catch-all route for handling 404 errors
app.use((req, res) => {
    res.status(404).send('404 - Not Found');
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});