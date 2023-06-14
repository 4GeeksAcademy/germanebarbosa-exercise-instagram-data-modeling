import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True,nullable=True)
    location = Column(String(250), nullable=True)
    image = Column(String(250))
    description = Column(String(250))
    likes = Column(Integer)
    comments = Column(String(250))
    favorites = relationship(Favorites)
    user_id = Column(Integer, ForeignKey('user.id'))
    
class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True,nullable=True)
    follower_user_name = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True,nullable=True)
    following_user_name = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=True)
    name = Column(String(250), nullable=True)
    password = Column(String(250))
    profile_description = Column(String(500))
    email = Column(String(100))
    post = relationship(Post)
    favorites = relationship(Favorites)
    followers = relationship(Followers)
    following = relationship(Following)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
