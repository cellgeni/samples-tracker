from django.db import models
from django.utils import timezone

NON_CORE_PROJECTS = "AGR55.CELLGEN_NON_CORE_PROJECTS"
CORE_PROJECTS = "AGR55.CELLGEN_CORE_PROJECTS"

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

    def __str__(self):
        return self.name


class Project(models.Model):
    cost_code = models.CharField(max_length=25, primary_key=True)
    title = models.CharField(max_length=25)
    funding = models.CharField(max_length=25)
    fund_type = models.CharField(max_length=25)
    accrep_text = models.CharField(max_length=255)
    year_to_date = models.CharField(max_length=15)
    project_text = models.CharField(max_length=25)
    ltd_budget = models.CharField(max_length=15)
    ltd_actual = models.CharField(max_length=15)
    balance_avail = models.CharField(max_length=15)

    core_view = lambda cost_code: f"""
        SELECT project as cost_code, 
        accrep_text, 
        "Year to Date" as year_to_date, 
        "Year to Date Budget" year_to_date_budget, 
        "Annual Budget" as annual_budget, 
        "Balance of Grant Available" as balance_avail 
        FROM {CORE_PROJECTS}
        WHERE project = '{cost_code}'   
         """
    non_core_view = lambda cost_code: f"""
           SELECT project as cost_code, 
        project_text as title,
        funding,
        fund_type,
        accrep_text,
        "Year to Date" as year_to_date, 
        "LTD Actual" as ltd_actual,
        "LTD Budget" as ltd_budget,
        "Balance of Grant Available" as balance_avail 
        FROM {NON_CORE_PROJECTS}
        WHERE project = '{cost_code}'
    """
    count_balance = lambda table, cost_code: f"""
    SELECT SUM("Balance of Grant Available")
    FROM {table}
    WHERE project='{cost_code}'
    """


class Meta:
    managed = False


def __str__(self):
    return self.cost_code
