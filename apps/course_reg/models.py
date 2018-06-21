from django.db import models
from django.contrib import messages

class UserManager(models.Manager):
    def validate(self, request):       
        if request.method == "POST":
            valid = True
            if len(request.POST['name']) < 6:
                valid = False
                messages.error(request,"Course name must be more than 5 characters")
            if len(request.POST['description']) < 16:
                valid = False
                messages.error(request,"Description must be more than 15 characters")
            if valid == True:
                c = Course(name=request.POST['name'])
                c.save()
                d = Description(course=c, desc=request.POST['description'])
                d.save()

    def delete(self, request, id):
        c = Course.objects.filter(id=id)
        if len(c) > 0:
            c = c[0]
        c.delete()
        messages.success(request, "Deleted Course")

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()
    
    def __repr__(self):
        return "<Course object: {}, {}>".format(self.name, self.created_at)
    
    def __str__(self):
        return self.name

class Description(models.Model):
    course = models.OneToOneField(
        Course, 
        on_delete=models.CASCADE,
        primary_key=True,
    )
    desc = models.CharField(max_length=500)

    def __repr__(self):
        return "<Description object: {} {}>".format(self.course.name, self.desc)

    def __str__(self):
        return self.desc