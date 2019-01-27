from django.db import models
# Create your models here.

class AbstractFile(models.Model):
    file_filed = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=31)
    timestamp = models.DateTimeField(auto_now_add=True)

class FileCategory(models.Model):
    '''
    The Category entries are managed by the system,
    automatically created via a Django data migration.
    '''
    STUDENT = 1
    TEACHER = 2
    SECRETARY = 3
    SUPERVISOR = 4
    ADMIN = 5
    FILECATEGORY_CHOICES = (
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (SECRETARY, 'secretary'),
        (SUPERVISOR, 'supervisor'),
        (ADMIN, 'admin'),
    )
    category_id = models.PositiveSmallIntegerField(choices=FILECATEGORY_CHOICES)

    def __str__(self):
        return self.get_id_display()
        # return str(self.role_id)
    
    def get_id_display(self):
        for key, value in self.FILECATEGORY_CHOICES:
            if self.category_id == key:
                return value
        return 'unknown role.'

    def get_role(self):
        for key, value in self.FILECATEGORY_CHOICES:
            if self.role_id == value:
                return {'category_id':key, 'cat_name': value}
        return 'unknown role.'

class File(AbstractFile):
    uuid = models.UUIDField(db_index=True, unique=True, blank=True, null=True)
    file_category = models.ManyToManyField(FileCategory, blank = True)

    def __str__(self):
        return str(self.id)