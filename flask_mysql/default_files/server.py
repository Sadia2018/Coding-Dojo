from app import app
from app.controllers import public
#import private controller if needed.

if __name__ == "__main__":
    app.run(debug=True)