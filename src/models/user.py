from mongoengine import Document
from mongoengine import StringField,EmailField,IntField,BooleanField

class User(Document):
    """
    TASK: Create a model for user with minimalistic
          information required for user authentication

    HINT: Do not store password as is.
    """
    username = StringField(max_length=20,unique=True,required=True)
    first_name = StringField(max_length=20,required=True)
    last_name = StringField(max_length=20,required=True)
    email = EmailField(required=True,unique=True)
    password = StringField(min_length=8,required=True)
    admin = BooleanField(default=None)


    def __str__(self):
        return self.username
 
