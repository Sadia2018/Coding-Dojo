from app import app
from app.controllers import public
from app.controllers import private

if __name__ == "__main__":
    app.run(debug=True)