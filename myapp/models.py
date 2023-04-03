from mongoengine import Document, fields,connect
# Create your models here.
from myproject.settings import MONGO_NAME
class Blogs(Document):
   name = fields.StringField()
   topic = fields.StringField()
   date = fields.DateTimeField()
   addition_info = fields.StringField()
   class Meta:
      db_table = 'Blog'
      
