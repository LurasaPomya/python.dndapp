from dndapp import db


# Base Class
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


# Spell Model
class Spell(Base):

    __tablename__ = 'spells'

    name = db.Column(db.String(255), unique=True, nullable=False)
    level = db.Column(db.SmallInteger, nullable=False)
    school = db.Column(db.String(255), nullable=False)
    spell_class = db.Column(db.String(255), nullable=False)
    casting_time = db.Column(db.String(255), nullable=False)
    spell_range = db.Column(db.String(50))
    duration = db.Column(db.String(50))
    page = db.Column(db.String(10))
    saving_throw = db.Column(db.String(25))
    damage_type = db.Column(db.String(50))
    damage = db.Column(db.String(50))
    description = db.Column(db.Text)
    at_higher = db.Column(db.Text)
    ritual = db.Column(db.Boolean, default=False)
    concentration = db.Column(db.Boolean, default=False)
    m_comp = db.Column(db.Boolean, default=False)
    s_comp = db.Column(db.Boolean, default=False)
    v_comp = db.Column(db.Boolean, default=False)
