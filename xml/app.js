const express = require('express')
var xml = require('xml');
const PouchDB = require('pouchdb');
const db = new PouchDB('students');

const app = express()
const port = 5000

function serialize(xml){
    const serializer = new XMLSerializer();
    return serializer.serializeToString(xmlDocument);
}

function deserialize(string){
    const parser = new DOMParser();
    return parser.parseFromString(xmlString, "text/xml");
}

app.get('/', (req, res) => {
    db.put({_id: '101907' , name: 'Aubrey Omondi', course: 'ICS'}, function callback(err, result) {
        if (!err) {
            console.log('Inserted into DB');
        }
    });
  
    db.get('101907').then(function(doc) {
        res.set('Content-Type', 'text/xml');
        res.send(xml(doc));
      }).catch(function (err) {
        console.log(err);
      });
    
})

app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`)
})