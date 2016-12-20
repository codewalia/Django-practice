from web1.models import Publisher
 
p1= Publisher(name='Apress',address='2855 Telegraph Avenue',city='Berkley',state_province='CA',country='U.S.A',website='http://www.apress.com/')
p1.save()

publisher_list = Publisher.objects.all()
#publisher_list[<Publisher: Publisher object>, <Publisher: Publisher object>]