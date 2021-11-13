from django.db import models

class CodeudorManager(models.Manager):

    def context_codeudor(self, kword):
        if self.filter(pk=kword).exists() == True:
            return self.get(pk=kword)

        else:
            return None