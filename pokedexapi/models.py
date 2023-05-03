from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Pokemon (models.Model):
    
    name = models.CharField(_("name"), max_length=255)
    type_1 = models.CharField(_("type 1"), max_length=255)
    type_2 = models.CharField(_("type 2"), max_length=255)
    total = models.IntegerField(_("total"))
    hp = models.IntegerField(_("hp"))
    attack = models.IntegerField(_("attack"))
    defense = models.IntegerField(_("defense"))
    sp_atk = models.IntegerField(_("SP. Atk"))
    sp_def = models.IntegerField(_("Sp. Def"))
    speed = models.IntegerField(_("speed"))
    generation = models.IntegerField(_("generation"))
    legendary = models.BooleanField(_("legendary"))


