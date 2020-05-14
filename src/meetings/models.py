
from django.db import models
from users.models import Student, Mentor
from TeamMap.models import Team

class Meeting(models.Model):
    name = models.CharField(max_length=100)
    video = models.CharField(max_length=50)
    info = models.CharField(max_length=1000)
    step = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.name)

    # in progress is update/create view
    #need something for complete?

class StudentMeeting(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    web_task = models.CharField(max_length=10000)

    def __str__(self):
        return "{} {}".format(self.student, self.meeting)


class MentorMeeting(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE) #meeting connects to team, team connects to mentor
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE) #need check to make sure just one mentor makes it
    team_data = models.CharField(max_length=100000, default="null")
    # problem = models.CharField(max_length=1000, default=0)
    # become_educated = models.FileField(upload_to='media/', default=0)
    # solution = models.CharField(max_length=400, default=0)
    # action_blueprint = models.CharField(max_length=500, default=0)
    # solution_results = models.CharField(max_length=600, default=0)
    in_progress = models.BooleanField(default=False)
    not_started = models.BooleanField(default=True)


    def __str__(self):
        return "{} {}".format(self.mentor, self.meeting)




