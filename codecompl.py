from server import app, db
from server.models import *

if __name__ == "__main__":
  # Import model definitions and then create the database
    db.create_all()
    db.session.commit()
    app.run(debug=True)
