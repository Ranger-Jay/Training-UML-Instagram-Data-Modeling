import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer,primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    follower = relationship(Follower)
    username = Column(String(250) , nullable=False)
    firstname = Column(String(250) , nullable=False)
    lastname = Column(String(250) , nullable=False)
    email = Column(String(250) , unique=True , nullable=False)
    comment = relationship(Comment)
    post = relationship(Post)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer , primary_key=True)
    user_id = Column(Integer , ForeignKey('user.id'))
    media = relationship(Media)
    comment = relationship(Comment)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer , primary_key=True)
    media_type = Column(Integer) 
    url = Column(String(250)) ##string used as placeholder until I can figure out enum
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base): 
    __tablename__ = 'comment'
    id = Column(Integer , primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer , ForeignKey('user.id'))
    post_id = Column(Integer , ForeignKey('post.id'))




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
