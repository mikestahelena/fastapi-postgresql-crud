from tortoise import fields, models


class Customer(models.Model):
    first_name = fields.TextField()
    last_name = fields.TextField()
    document = fields.TextField()
    birthdate = fields.DateField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.document
