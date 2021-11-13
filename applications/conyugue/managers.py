from django.db import models

class ConygueManager(models.Manager):

    def context_conyugue(self, kword):
        if self.filter(pk=kword).exists() == True:
            return self.get(pk=kword)

        else:
            return None