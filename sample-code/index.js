const express = require('express');
const path = require('path');
var nodemailer = require('nodemailer');
const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');
const app = express();

// Connection URL
const url = 'removed'


// Database Name
const dbName = 'removed';
// Create a new MongoClient
const client = new MongoClient(url);

// Use connect method to connect to the Server
client.connect(function(err) {
	assert.equal(null, err);
	console.log("Databse Connected to server");
	const databse = client.db(dbName);
		findDocuments(database, function() {
			client.close();
		});
});


app.use(express.static(path.join(__dirname, 'websiteCode')));

var transporter = nodemailer.createTransport({
	'removed'
	}
});

//DELETED: CODE TO SEND EMAIL UPON ACCOUNT BEING CREATED

//DELETED: CODE TO SEND USER A SECURE PASSWORD WE MADE

//DELETED: CODE TO SEE IF LOGIN INFORMATION IS IN DATABASE

//IMPORTANT
const PORT = process.env.PORT || 9060;
app.listen(PORT, () => console.log('Started server'));

//DELETED CODE TO ADD USER NAME AND PASSWORD TO DATABASE
