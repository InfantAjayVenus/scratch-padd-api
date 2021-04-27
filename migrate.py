from scratch_padd import create_app
from scratch_padd.models import db, Pad

create_app().app_context().push()
db.create_all()
