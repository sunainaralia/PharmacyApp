from django.db import models
from v1.api.account.models import User

# model for rating app
class Rating(models.Model):
  rater_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='rating_given')
  ratee_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='rating')
  star=models.IntegerField()
  comment=models.TextField()
  rater_experience=models.TextField()




