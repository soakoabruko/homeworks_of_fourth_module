from django.db import models

class Advertisment( models.Model ):
    title = models.CharField( 'Название', max_length = 100 )
    description = models.TextField( 'Описание' )
    price = models.DecimalField( 'Цена', max_digits = 10, decimal_places = 2 )
    auction = models.BooleanField( 'Торг', help_text = 'Отметьте, если торг уместен.' )
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now_add = True )

    class Meta:
        db_table = 'advertisements'

    def __str__( self ):
        return f'Advertisment( id = { self.id }, title = { self.title }, price = { self.price } )'