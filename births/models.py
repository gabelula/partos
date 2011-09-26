#encoding= utf-8
from django.db import models
from django_countries import CountryField
from django_extensions.db.fields import AutoSlugField

class Birth(models.Model):

    BIRTH_PLACE_CHOICES = (('hb', 'Parto en Casa'), ('hs','Hospital'), ('ot','Otro'))

    title = models.CharField(max_length=30, verbose_name=u'título')
    content = models.TextField(verbose_name="historia")
    summary = models.TextField()
    slug  = AutoSlugField(max_length=20, unique=True, populate_from=('title',)) 
    year =  models.IntegerField(verbose_name=u'año del parto')
    place = models.CharField(max_length=20, verbose_name="lugar", choices=BIRTH_PLACE_CHOICES)
    city = models.CharField(max_length=30, verbose_name="ciudad")
    country = CountryField(default='UY', verbose_name=u'país')
    name = models.CharField(max_length=30, verbose_name="firma")
    email = models.EmailField(verbose_name="correo electronico")
    published_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False, help_text='Muestra si una historia está desplegada en la pagina principal o no.')

    def __unicode__(self):
        return self.title

    def save(self):
      self.summary = self.truncate(self.content)
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
