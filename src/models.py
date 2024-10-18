import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Enum
from eralchemy2 import render_er

Base = declarative_base()

{
    "id": "",
    "name": "",
    "posts": [
        {
            "user": "",
            "media": [
                {
                    "imagenes": ""
                }
            ]
        }
    ]
}


class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50),unique=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50),unique=True, nullable=False)

    posts=relationship('Post', back_populates='user')
    comments=relationship('Comment', back_populates='author')
    followers=relationship('Follower', foreign_keys='follower.user_from_id', backref='follower')
    followings=relationship('Follower', foreign_keys='follower.user_to_id', backref='followings')



class Post(Base):
     __tablename__ = 'post'

     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))

     user=relationship('User', back_populates='posts')
     media=relationship('Media', back_populates='posts')
     comments=relationship('Comments', back_populates='post')



class Comment(Base):

    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column (String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    author= relationship('User', back_populates='comments')
    post=relationship('Post', back_populates='comments')

class Media(Base):

    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column (String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    type =  Column(Enum("video", "imagen"), nullable=False)

    post= relationship('Post', back_populates='media')

class Followers(Base):

    __tablename__ = 'followers'
    user_from_id = Column(Integer,ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer,ForeignKey('user.id'), primary_key=True)








# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     # person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
