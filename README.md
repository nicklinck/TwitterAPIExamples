# TwitterAPIExamples
A demonstration of how to use Python to access the Twitter API
This is meant to be starter code for anyone who wants to build an application using the Twitter API and python.

TwitterAPI.py contains all of the code required to pull tweets from a specific user and then pull all of the replies to that given tweet. 

## Getting Started
Go to https://developer.twitter.com/ and create a developer account in order to get a bearer token to access the API.

Once you have a bearer token, 'git clone' this repository.

## Quick Setup
If you want to get up an running without setting up your own python environment. Go to https://jupyter.org/try and click 'try classic notebook'. 

Create a new cell with the '+' icon and copy the contents of TwitterAPI.py from the cloned repository into the newly created cell.

In the function 'create_headers' follow the instructions in the code in order to add your bearer token to the code. Alternatively you can set an enviroment variable so that you do not need to include your bearer token in the code. NEVER post your bearer token publicly! 

Now press the play button at the top of the notebook while you have the cell selected that contains the TwitterAPI.py code. 

You should see output from your favorite tweeter! (Control output in '__main__' by setting variables 'DEBUG' and 'INFO' to 'True' or 'False')

## Details
'process_tweets()' is the main function that will call other helper functions from the Twitter API class. Modify this if you would like to do something new with the code. 'process_tweets()' is meant to be an example for your to build your own application. The helpwer functions 'get_tweets(user)' and 'get_replies(id)' are where the main functionality of the Twitter API is stored.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[Apache License](http://www.apache.org/licenses/)