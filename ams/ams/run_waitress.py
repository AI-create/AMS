from waitress import serve
from ams.wsgi import application  # Ensure this matches your Django project name

if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=8000)
