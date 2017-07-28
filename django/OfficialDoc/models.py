class Fundinfo(models.Model):
	c_tenantid = models.CharField(max_length=20)
	c_tacode = models.CharField(max_length=2)
	c_fundcode = models.CharField(max_length=12)
	c_fundname = models.CharField(max_length=40)
	c_fundcharacter = models.CharField(max_length=80)
	c_fundstatus = models.CharField(max_length=1)

	def __str__(self):
		return self.c_fundname	