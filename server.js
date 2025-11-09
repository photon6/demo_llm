const express = require('express');
const fs = require('fs');
const app = express();
// const port = 3000;

// Load config from file
const config = JSON.parse(fs.readFileSync('conf/config.json', 'utf-8'));

app.use(express.static('public')); // Serve files from 'public' folder (put index.html there)

app.get('/', (req, res) => {
  res.send(__dirname + '/public/index.html');
});

app.listen(config.ui_port, () => {
  console.log(`Server running at http://localhost:${config.ui_port}`);
});