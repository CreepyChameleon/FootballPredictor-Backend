# FootballPredictor-Backend
This provides the backend for updating the MongoDB database where the data for the frontend app is stored

### Repository links:
- [FootballPredictor-Server](https://github.com/CreepyChameleon/FootballPredictor-Server)
	- The server that runs on Heroku that the frontend app pulls from
- [FootballPredictor-Frontend](https://github.com/CreepyChameleon/FootballPredictor-Frontend)
	- The frontend iOS app written in Swift

## How to use
As a user all of the functions can be executed from the command line

```
python3 updateDatabase.py FUNCTION_NAME WEEK_NUMBER
```
A user can either call the function *updateDatabase* or *updateCBS*, and with a week number as the argument.

```
python3 updateDatabase.py updateDatabase 9
```
