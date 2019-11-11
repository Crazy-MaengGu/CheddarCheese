from django.db import models

# Create your models here.


class Contract(models.Model):
    saleTypeChoices = (('직판', '직판'), ('T1', 'T1'), ('T2', 'T2'), ('기타', '기타'))
    saleIndustryChoices = (('금융', '금융'), ('공공', '공공'), ('유통 & 제조', '유통 & 제조'), ('통신 & 미디어', '통신 & 미디어'), ('기타', '기타'))
    contractStepChoices = (('Opportunity', 'Opportunity'), ('Firm', 'Firm'), ('Drop', 'Drop'))
    depositConditionChoices = (('계산서 발행 후', '계산서 발행 후'), ('당월', '당월'), ('익월', '익월'), ('당월 말', '당월 말'), ('익월 초', '익월 초'), ('익월 말', '익월 말'))
    modifyContractPaperChoices = (('N', 'N'), ('Y', 'Y'))
    newCompanyChoices = (('N', 'N'), ('Y', 'Y'))

    cont_id = models.AutoField(primary_key=True)
    cont_code = models.CharField(max_length=30)
    cont_name = models.CharField(max_length=200)
    cont_emp_name = models.CharField(max_length=30)
    cont_emp_dept_name = models.CharField(max_length=30)
    cont_sal_type_id = models.ForeignKey(SalesType, on_delete=models.CASCADE, related_name='cont_sal_type_id')
    cont_sal_industry_id = models.ForeignKey(SalesIndustryType, on_delete=models.CASCADE, related_name='cont_sal_industry_id')
    cont_cate_main = models.CharField(max_length=200)
    cont_cate_sub = models.CharField(max_length=200)
    cont_date = models.DateField()
    cont_step = models.CharField(max_length=20, choices=contractStepChoices, default='Opportunity')
    cont_start_date = models.DateField(null=True, blank=True)
    cont_end_date = models.DateField(null=True, blank=True)
    cont_depo_con = models.CharField(max_length=20, choices=depositConditionChoices, default='계산서 발행 후', null=True, blank=True)
    cont_depo_con_day = models.IntegerField(default=0, null=True, blank=True)
    cont_paper = models.FileField(null=True, blank=True, upload_to="contractPaper/%Y_%m")
    cont_order_paper = models.FileField(null=True, blank=True, upload_to="orderPaper/%Y_%m")
    cont_comt = models.CharField(max_length=200, null=True, blank=True)
    cont_modify_order_paper = models.CharField(max_length=1, choices=modifyContractPaperChoices, default='N', null=True, blank=True)
    newCompany = models.CharField(max_length=10, choices=newCompanyChoices, default='N')

    def __str__(self):
        return self.cont_name


class ContractManager(models.Model):
    cont_mng_cont_id = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='cont_mng_cont_id', primary_key=True)
    cont_mng_emp_code = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='cont_mng_emp_code', primary_key=True)
    cont_mng_date = models.DateField()
    cont_mng_sal_price = models.BigIntegerField()
    cont_mng_profit_price = models.BigIntegerField()
    cont_mng_profit_ratio = models.FloatField()
    cont_mng_cust_id = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='cont_mng_cust_id')

    def __str__(self):
        return 'Contract Mng : {} {}'.format(self.cont_mng_cont_id, self.cont_mng_date)


class Revenue(models.Model):
    reve_cont_id = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='reve_cont_id', primary_key=True)
    reve_emp_id = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='reve_emp_id', primary_key=True)
    reve_id = models.AutoField(primary_key=True)
    reve_price = models.BigIntegerField()
    reve_profit_price = models.BigIntegerField()
    reve_profit_ratio = models.FloatField()
    reve_pred_billing_date = models.DateField(null=True, blank=True)
    reve_billing_date = models.DateField(null=True, blank=True)
    reve_pred_depo_date = models.DateField(null=True, blank=True)
    reve_depo_date = models.DateField(null=True, blank=True)
    reve_stat = models.CharField(max_length=1, null=True, default='N')
    reve_comt = models.CharField(max_length=200, null=True, blank=True)
    reve_com_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='reve_com_id')

    def __str__(self):
        return 'Revenue {} {} {}'.format(self.reve_cont_id, self.reve_emp_id, self.reve_id)


class Purchase(models.Model):
    purc_cont_id = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='purc_cont_id', primary_key=True)
    purc_emp_id = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='purc_emp_id', primary_key=True)
    purc_id = models.AutoField(primary_key=True)
    purc_price = models.BigIntegerField()
    purc_pred_billing_date = models.DateField(null=True, blank=True)
    purc_billing_date = models.DateField(null=True, blank=True)
    purc_pred_withdraw_date = models.DateField(null=True, blank=True)
    purc_withdraw_date = models.DateField(null=True, blank=True)
    purc_stat = models.CharField(max_length=1, null=True, default='N')
    purc_comt = models.CharField(max_length=200, null=True, blank=True)
    purc_com_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='purc_com_id')

    def __str__(self):
        return 'Purchase {} {} {}'.format(self.purc_cont_id, self.purc_emp_id, self.purc_id)


class SalesType(models.Model):
    sal_type_id = models.AutoField(primary_key=True)
    sal_type_comt = models.CharField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.sal_type_id, self.sal_type_comt)


class SalesIndustryType(models.Model):
    sal_industry_id = models.AutoField(primary_key=True)
    sal_industry_comt = models.CharField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.sal_industry_id, self.sal_industry_comt)


class Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    cate_comt = models.CharField(max_length=200)
    cate_depen_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='cate_depen_id')

    def __str__(self):
        return '{} {}'.format(self.cate_id, self.cate_comt)


class ContractItem(models.Model):
    cont_id = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='cont_id', primary_key=True)
    cont_item_cate_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='cont_item_cate_id', primary_key=True)
    cont_item_id = models.AutoField(primary_key=True)
    cont_item_comt = models.CharField(max_length=200)
    cont_item_num = models.SmallIntegerField()
    cont_item_price = models.BigIntegerField()

    def __str__(self):
        return 'ContractItem {} {} {}'.format(self.cont_id, self.cont_item_cate_id, self.cont_item_id)


class Goal(models.Model):
    goal_id = models.AutoField(primary_key=True)
    goal_dept_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='goal_dept_id', null=True)
    goal_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='goal_emp_id', null=True)
    year = models.BigIntegerField()
    sales1 = models.BigIntegerField()
    sales2 = models.BigIntegerField()
    sales3 = models.BigIntegerField()
    sales4 = models.BigIntegerField()
    sales5 = models.BigIntegerField()
    sales6 = models.BigIntegerField()
    sales7 = models.BigIntegerField()
    sales8 = models.BigIntegerField()
    sales9 = models.BigIntegerField()
    sales10 = models.BigIntegerField()
    sales11 = models.BigIntegerField()
    sales12 = models.BigIntegerField()
    salesq1 = models.BigIntegerField()
    salesq2 = models.BigIntegerField()
    salesq3 = models.BigIntegerField()
    salesq4 = models.BigIntegerField()
    profit1 = models.BigIntegerField()
    profit2 = models.BigIntegerField()
    profit3 = models.BigIntegerField()
    profit4 = models.BigIntegerField()
    profit5 = models.BigIntegerField()
    profit6 = models.BigIntegerField()
    profit7 = models.BigIntegerField()
    profit8 = models.BigIntegerField()
    profit9 = models.BigIntegerField()
    profit10 = models.BigIntegerField()
    profit11 = models.BigIntegerField()
    profit12 = models.BigIntegerField()
    profitq1 = models.BigIntegerField()
    profitq2 = models.BigIntegerField()
    profitq3 = models.BigIntegerField()
    profitq4 = models.BigIntegerField()
    year_sales_sum = models.BigIntegerField()
    year_profit_sum = models.BigIntegerField()

    def __str__(self):
        return '{}년 {} {} 목표'.format(self.year, self.goal_dept_id, self.goal_emp_id)


