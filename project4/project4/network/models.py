from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db import models
from django.urls import reverse

"""
posts, follows and likes (and comments)

A user can:
    - create and edit posts
    - follow other users but not self
    - likes or not, a post
    - comment on other users posts, or self posts
"""
class User(AbstractUser):
    follower = models.ManyToManyField("self", symmetrical=False)

    def following(self):
        return User.objects.filter(follower__exact=self).count()


@receiver(m2m_changed, sender=User.follower.through)
def m2m_changed_follower(sender, instance, action, pk_set, *args, **kwargs):
    if action == "pre_add":
        # if self id is in follows, remove it
        if instance.id in pk_set:
            pk_set.remove(instance.id)
            # raise ValidationError("Can't self follow")


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    like = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post #{self.id}, authored by: {self.author}"

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    def liked(self):
        self.like += 1
        self.save(update_fields='like')

    def not_liked(self):
        if self.like - 1 >= 0:
            self.like -= 1
            self.save(update_fields='like')

    def serialize(self):
        return {
            "id": self.id,
            "author": self.author.username,
            "content": self.content,
            "created_at": self.created_at.strftime("%b %d %Y, %I:%M %p"),
            "like": self.like
        }


class Comment(models.Model):
    op = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_comments")
    content = models.TextField()
    like = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment #{self.id}, on {self.op}"

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    def liked(self):
        self.like += 1
        self.save(update_fields='like')

    def not_liked(self):
        if self.like - 1 >= 0:
            self.like -= 1
            self.save(update_fields='like')

