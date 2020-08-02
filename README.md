# deploy_ml_model

How to deply classifier model with flask

Step1. Train and save a model
        Here's the link https://github.com/Deepakmehtansit/deploy_ml_model.git code to building a simple classification model and then saving the model by serializing it using pickle,
        Python pickle module is used for serializing and de-serializing a Python object structure.
        The idea is that this character stream contains all the information necessary to reconstruct the object in another python script
    
Step2. Now the model is ready and saved. It’s time to building a flask application.
    create virtual environment assuming python is already installed
    --> virtualenv venv
    activate virtual environment
    --> on linux --> source venv/bin/activate
    --> on window --> venv/Scripts/activate
    
    now install required libraries
    
Step3 Creating the PREDICTION API
    1 Initiate flask application
    2 load saved model
    3 redirecting the api to the homepage
        We use @app.route(‘/’) to define functions which are used to redirect them into any number of URI with respect to the API. So, when you start the flask server, it redirects to index.html
    4 redirect the api to predict the result
    5 it will be a post ( @app.route(‘predict/’) ) request, so we get input values from user and do some preprocessing before feeding it to the model
    6 Starting the flask server 
     --> python app.py