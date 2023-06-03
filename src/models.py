import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=True)
    user_name = Column(String(250), nullable=True)
    password = Column(String(250))
    followers_quantity = Column(Integer)
    following_quantity = Column(Integer)
    post_quantity = Column(Integer)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    followers_id = Column(Integer, ForeignKey('followers.id'))
    following_id = Column(Integer, ForeignKey('following.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_img = Column(String(250))
    user = relationship(User)

class Followers(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key=True,nullable=True)
    follower_user_name = Column(String(250), nullable=True)
    user = relationship(User)

class Following(Base):
    __tablename__ = 'following'

    id = Column(Integer, primary_key=True,nullable=True)
    following_user_name = Column(String(250), nullable=True)
    user = relationship(User)
    
class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True,nullable=True)
    location = Column(String(250), nullable=True)
    image = Column(String(250))
    description = Column(String(250))
    likes = Column(Integer)
    comments = Column(String(250))
    favorites = relationship(Favorites)
    user = relationship(User)

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
