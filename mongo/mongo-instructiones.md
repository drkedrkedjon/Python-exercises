# Install

`brew tap mongodb/brew
brew install mongodb-community@8.0`

## Start Mongo

`mongod --config /opt/homebrew/etc/mongod.conf --fork`

## Start mongo shell

`mongosh`

## Shutdown

### if not in mongosh

mongosh
`use admin
db.<shutdownServer>()`

MongoDB Documentation link https://www.mongodb.com/docs/v8.0/tutorial/install-mongodb-on-os-x/

# Usuarios

crear database:
`use databaseName`

crear user:

```js
db.createUser({
  user: "sasa",
  pwd: "sasa",
  customData: { startDate: new Date() },
  roles: [
    { role: "clusterAdmin", db: "admin" },
    { role: "readAnyDatabase", db: "admin" },
    "readWrite",
  ],
});
```

Ver users:
`db.getUsers()`

Delete user:
`db.dropUser(john)`

# Colectiones (tables)

crear colection
`db.createCollection()`

ver colectiones
`show collections`

## Adding documents

Insert one:

```js
db.books.insertOne({
  name: "Mongo DB",
  publishedDate: new Date(),
  authors: [{ name: "Caty" }, { name: "Sasa" }],
});
```

Insert varios documentos:

```js
db.books.insertManu([
  {
    name: "Caty en Bilbao",
    publishedDate: new Date(),
    authors: [{ name: "Kobu" }, { name: "Simba" }],
  },
  {
    name: "Sasa en Bilbao",
    publishedDate: new Date(),
    authors: [{ name: "Simba" }],
  },
  {
    name: "Cubi y Boni en Bilbao",
    publishedDate: new Date(),
    authors: [{ name: "Kobu" }, { name: "Simba" }],
  },
]);
```

## Query (solicitud a ver) todos documentos con find()

`db.books.find()` Ahora devuelve .pretty() por defecto

`db.books.find().pretty()`

## Query un documento especifico

Comando .find() retorna uno o varios con la misma query.
El mismo comando pero .findOne() retorna el primer

```js
db.books.find({
  name: "Caty en Bilbao",
});
```

## MongoDB proyectiones

Son queries con .find() donde enviamos el segundo objeto con campos que queremos que nos los devuelve. Osea, en un documento con 14 entradas podemos retornar solo las 2 solicitadas. Si no la queremos no la mencionamos menos ID cual si no queremos ponemos 0

```js
db.books.find(
  {
    name: "Caty en Bilbao",
  },
  {
    _id: 0,
    name: 1,
    authors: 1,
  },
);
```
