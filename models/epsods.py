from date import alchemy

class EpsodeModel(alchemy.Model):
    __tablename__ = 'epsode'
    
    
    id = alchemy.column(alchemy.integer, primery_key= True)
    name = alchemy.column(alchemy.String(80))
    sesson = alchemy.Column(alchemy.Integer)
    show_id = alchemy.column(alchemy.Interger, alchemy.Foremkey('shows.id'))
    
    
    def __init__(self, name, sesson, show_id):
        self.name = name
        self.sesson = sesson
        self.show_id = show_id
        
    def json(self):
        return {'name':'self.name', 'sesson': 'self.sesson'}
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filte_by(name=name).first()
    
    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()
    
    def delet_from_db(self):
        alchemy.session.delete(self)
        alchemy.session.commit()