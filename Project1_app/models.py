# from django.db import models


#
#
# class User(models.Model):
#     user_id = models.CharField(max_length=10, primary_key=True)
#     Phone_number = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150)
#
#
# class Group(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#
#
# class Roles(models.Model):
#     roles = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('user1', 'User1'), ('user2', 'User2')])
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     Group_name = models.ForeignKey(Group, on_delete=models.CASCADE)
#
#
# class Permissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     codename = models.CharField(max_length=50)


from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group'


class Permissions(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class Roles(models.Model):
    roles = models.CharField(max_length=100, choices=[('admin', 'Admin'), ('user1', 'User1'), ('user2', 'User2')])
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'roles'


class RolesPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_permissions'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(db_column='Phone_number', max_length=100)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user'
