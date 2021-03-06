from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
     areaID = models.AutoField(primary_key=True)
     name = models.CharField(max_length=128)
     picture = models.ImageField(upload_to='area_images', blank=True)
     rarity = models.IntegerField(default=1)
     backstory = models.CharField(max_length=128)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    level = models.IntegerField(default=1, blank=False)
    maxHP = models.IntegerField(default=100, blank=False)
    currentHP = models.IntegerField(default=100, blank=False)
    strength = models.IntegerField(default=10, blank=False)
    dexterity = models.IntegerField(default=10, blank=False)
    intelligence = models.IntegerField(default=10, blank=False)
    areaID = models.ForeignKey(Area, default=0, blank=False)
    
    def __unicode__(self):
        return self.user.username
     
    

class Monster(models.Model):
    monsterID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='monster_images', blank=True)
    rarity = models.IntegerField(default=50)
    difficulty = models.IntegerField(default=1)
    boss = models.BooleanField(default=False)
    baseXP = models.IntegerField(default=10)
    areaID = models.ForeignKey(Area, default=0)

    def __unicode__(self):
                return self.name

class Item(models.Model): # Abstract class defining common attributes of all items
    itemID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='item_images', blank=True)

    def __unicode__(self):
        return self.name

class Weapon(Item):
    minD = models.IntegerField(default=1)
    maxD = models.IntegerField(default=1)

class Armor(Item):
    defence = models.IntegerField(default=1)

class Usable(Item):
    effect = models.IntegerField(default=0)

class ItemTables(models.Model):
    userID = models.ForeignKey(UserProfile)
    itemID = models.ForeignKey(Item)
    amount = models.IntegerField(default=0)

class DropTables(models.Model):
    monsterID = models.ForeignKey(Monster)
    itemID = models.ForeignKey(Item)
    rarity = models.IntegerField(default=0)
    
    
