import os
from flask_admin import Admin
from models import db, User, Character, Planet, FavoritePlanet, FavoriteCharacter
from flask_admin.contrib.sqla import ModelView

class FavoritePlanetAdmin(ModelView):
    column_list = ('id', 'user', 'planet')
    form_columns = ('user', 'planet')

class FavoriteCharacterAdmin(ModelView):
    column_list = ('id', 'user', 'character')
    form_columns = ('user', 'character')

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(FavoritePlanetAdmin(FavoritePlanet, db.session))
    admin.add_view(FavoriteCharacterAdmin(FavoriteCharacter, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))