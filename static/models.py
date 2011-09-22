drom django.db import models

class Birth(models.Model):

    COUNTRY_CHOICES = ()
    BIRTH_PLACE_CHOICES = (('hb', 'HomeBirth'), ('hs','Hospital'), ('ot','Other'))

    title = models.CharField(max_length=30)
    content = models.CharText()
    summary = models.CharText()
    slug  = models.SlugField(max_length=20) 
    year =  models.IntegerField()
    place = models.CharField(choices=BIRTH_PLACE_CHOICES)
    city = models.CharField(max_length=30)
    country = models.CharField(choices=COUNTRY_CHOICES), default='uy')
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    published_date = models.DateField(auto_add_now=True)
    active = models.BooleanField(default=False, help_text='This field is gonna be not displayed in the front page if it is False.')

    def save(self):
      self.summary = truncate(self.content)
      super(Birth, self).save()

    def truncate(value, limit=30):
      """
      Truncates a string after a given number of chars keeping whole words.
      """
      try:
        limit = int(limit)
      # invalid literal for int()
      except ValueError:
        # Fail silently.
        return value
    
      # Make sure it's unicode
      value = unicode(value)
    
      # Return the string itself if length is smaller or equal to the limit
      if len(value) <= limit:
        return value
    
      # Cut the string
      value = value[:limit]
    
      # Break into words and remove the last
      words = value.split(' ')[:-1]
    
      # Join the words and return
      return ' '.join(words) + '...'
