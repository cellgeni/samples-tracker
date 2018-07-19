from django.db import models
from django.utils import timezone


class Owner(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Action(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Sample(models.Model):
    sid = models.CharField(max_length=100)

    def __str__(self):
        return str(self.sid)


class Stage(models.Model):
    action = models.ForeignKey(Action, null=True, blank=True, on_delete=models.SET_NULL)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    active = models.BooleanField(default=False, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.action) + " " + str(self.date) + " " + str(self.sample)


class WarehouseSample(models.Model):
    name = models.CharField(max_length=100)
    supplier_name = models.CharField(max_length=255)
    donor_id = models.CharField(max_length=255)
    cohort = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)
    public_name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    phenotype = models.CharField(max_length=255)
    cost_code = models.CharField(max_length=20)

    warehouse_view = """
     SELECT DISTINCT 
    1 id,
    sample.name , 
    sample.supplier_name,
    sample.donor_id, 
    sample.`cohort`,
    sample.`gender`,
    sample.`public_name`,
    sample.`common_name`,
    sample.`description`,
    sample.`phenotype`,
    iseq_flowcell.cost_code

FROM iseq_flowcell
   JOIN study USING(id_study_tmp)
   JOIN sample USING(id_sample_tmp)
   JOIN iseq_product_metrics USING(id_iseq_flowcell_tmp)
WHERE  iseq_flowcell.cost_code = "S4436"                
     """

    class Meta:
        managed = False
        # db_table = 'warehouse'

    def __str__(self):
        return self.name


class Project(models.Model):
    year_to_date = models.CharField(max_length=15)
    this_month = models.CharField(max_length=15)
    accrep_text = models.CharField(max_length=255)
    fund_type = models.CharField(max_length=25)
    funding = models.CharField(max_length=25)
    project_text = models.CharField(max_length=25)
    project = models.CharField(max_length=25)
    balance_of_grant_avail = models.CharField(max_length=15)
    ltd_budget = models.CharField(max_length=15)
    ltd_actual = models.CharField(max_length=15)

    class Meta:
        managed = False
        # db_table = 'AGR55.CELLGEN_NON_CORE_PROJECTS'
        db_table = 'AGR55.CELLGEN_CORE_PROJECTS'

    def __str__(self):
        return self.project
