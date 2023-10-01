from app import create_app, db
from models import Bird

app = create_app()

with app.app_context():
    db.create_all()

    print('Deleting existing birds...')
    Bird.query.delete()

    print('Creating bird objects...')
    chickadee = Bird(name='Black-Capped Chickadee', species='Poecile Atricapillus')
    grackle = Bird(name='Grackle', species='Quiscalus Quiscula')
    starling = Bird(name='Common Starling', species='Sturnus Vulgaris')
    dove = Bird(name='Mourning Dove', species='Zenaida Macroura')

    print('Adding bird objects to transaction...')
    db.session.add_all([chickadee, grackle, starling, dove])

    print('Committing transaction...')
    db.session.commit()

    print('Complete.')
