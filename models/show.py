from date import alchemy
from . import epsod

class ShowModel(alchemy.Model):
    __tablename__ = 'shows'
    
    
    id = alchemy.Column(alchemy.Integer, primary_key = True)
    name = alchemy.Column(alchemy.String(80))
    
    epsode = alchemy.relationship(epsod.EpsodeModel, lazy='dynamic')
    
    def __init__(self, name):
        self.name = name
        
    def json(self):
        return {'id': 'self.id', 'name': 'self.name'}
    
    def saveDB(self):
        alchemy.session.add(self)
        alchemy.session.commit()
        
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter.by(name=name).first()
        
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter.by(id=id).first()
        