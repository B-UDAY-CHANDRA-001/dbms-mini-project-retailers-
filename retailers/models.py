from django.db import models


class Items(models.Model):
    Product_id = models.CharField(max_length=6)
    Product_name = models.CharField(max_length=40)
    Cost_price = models.IntegerField()
    Sell_price = models.IntegerField()
    Rating = models.CharField(max_length=10)


class Customers(models.Model):
    Customer_id = models.CharField(max_length=6)
    Full_name = models.CharField(max_length=20)
    City = models.CharField(max_length=10)
    State = models.CharField(max_length=10)
    PhoneNo = models.IntegerField()


class Cart(models.Model):
    Customer_id = models.CharField(max_length=6)
    Order_id = models.CharField(max_length=6)
    Product_id = models.CharField(max_length=6)
    Quantity = models.IntegerField()
    Price = models.IntegerField()


class Orders(models.Model):
    Order_id = models.CharField(max_length=6)
    Customer_id = models.CharField(max_length=6)
    Date = models.CharField(max_length=10)
    Order_status = models.CharField(max_length=10)
    class Meta:
        db_table = "retailers_orders"


class Cart_contains(models.Model):
    Customer_id = models.CharField(max_length=6)
    Order_id = models.CharField(max_length=6)
    Product_id = models.CharField(max_length=6)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    Date = models.CharField(max_length=30)
    Order_status = models.CharField(max_length=15)


class Meta:
    db_table = "items"

