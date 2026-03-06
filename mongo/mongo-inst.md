## Install

brew install mongodb-community@8.0

## Start

mongod --config /opt/homebrew/etc/mongod.conf --fork

## Shutdown

start mongosh
use admin
db.shutdownServer()

MongoDB Documentation link https://www.mongodb.com/docs/v8.0/tutorial/install-mongodb-on-os-x/
