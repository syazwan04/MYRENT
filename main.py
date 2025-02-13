from website import create_app #because website is python package, what ever you put in __init__.py folder it is become python package

app = create_app()

if __name__ == "__main__": # only if we run this file not import this file then will executed this app
    app.run(debug=True) #if we change the python code, the line automatically rerun the app