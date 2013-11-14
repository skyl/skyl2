from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from django.conf import settings

from taggit.managers import TaggableManager

t = settings.TWITTER


class Member(models.Model):
    """
    Piece of content.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    content = models.TextField()
    published = models.BooleanField(default=False)

    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    class Meta:
        ordering = ['-created_dt']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Member, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": self.slug})
    url = get_absolute_url

    def edit_url(self):
        u = reverse('admin:feeder_member_change', args=[self.id])
        return u

    def publish(self):
        self.published = True
        t.statuses.update(self.gen_tweet())
        self.save()

    def gen_tweet(self):
        # TODO
        return self.title


from docutils.parsers.rst import directives
from .directives import Pygments
directives.register_directive('sourcecode', Pygments)
directives.register_directive('code-block', Pygments)
