## Install

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

## Course

crear database:
`use databaseName`

crear user:

```
db.createUser({
  user: "sasa",
  pwd: "sasa",
  customData: {startDate: new Date()},
  roles: [
    {role: "clusterAdmin", db: "admin"},
    {role: "readAnyDatabase", db: "admin"},
    "readWrite"
  ]
})
```

Ver users:
`db.getUsers()`

Delete user:
`db.dropUser(john)`
