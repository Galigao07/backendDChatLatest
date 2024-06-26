from django.db import models

class Employee(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField()
    emp_id = models.IntegerField(default=0)
    last_name = models.CharField(max_length=55, default=' ')
    first_name = models.CharField(max_length=55, default=' ')
    middle_name = models.CharField(max_length=55, default=' ')
    department = models.CharField(max_length=50, default=' ')
    designation = models.CharField(max_length=75, default=' ')
    home_phone_no = models.CharField(max_length=15, default=' ')
    mobile_no = models.CharField(max_length=25, default=' ')
    fax_no = models.CharField(max_length=15, default=' ')
    st_address = models.CharField(max_length=60, default=' ')
    city_address = models.CharField(max_length=30, default=' ')
    zip_code = models.IntegerField(default=0)
    date_of_birth = models.DateField(default='0000-01-01')
    place_of_birth = models.CharField(max_length=100, default='0.000')
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    date_as_of = models.DateField(default='0000-01-01')
    remarks = models.CharField(max_length=100, default=' ')
    active = models.CharField(max_length=5, default='Y')
    employee_image = models.BinaryField(null=True)  # For BYTEA data type
    date_entered = models.DateField(default='0000-01-01')
    ul_code = models.IntegerField(default=0)
    manual_yn = models.CharField(max_length=1, default='')
    schedule = models.IntegerField(default=0)
    civil_stat = models.CharField(max_length=15, default='Single')
    confidential = models.CharField(max_length=5, default='N')
    finger_id = models.CharField(max_length=20, default=' ')
    auto_filldtr = models.CharField(max_length=5, default=' ')
    basic_comp = models.CharField(max_length=1, default='Y')
    perjob_comp = models.CharField(max_length=1, default='N')
    acct_no = models.CharField(max_length=20, default=' ')
    paid_lunch = models.CharField(max_length=5, default='N')
    sss_chk = models.CharField(max_length=5, default='Y')
    phic_chk = models.CharField(max_length=5, default='Y')
    hdmf_chk = models.CharField(max_length=5, default='Y')
    tax_chk = models.CharField(max_length=5, default='Y')
    release_type = models.CharField(max_length=10, default='CASH')
    flexibreak = models.CharField(max_length=5, default='N')
    gender = models.CharField(max_length=1, default='')
    responsibility_center_code = models.CharField(max_length=11, default='')
    responsibility_center = models.CharField(max_length=250, default='')
    desc_department = models.CharField(max_length=999, default='')
    tax_exemption = models.CharField(max_length=50, default='')
    cola = models.CharField(max_length=1, default='N')
    cola_taxable = models.CharField(max_length=1, default='N')
    cola_based_on_dtr = models.CharField(max_length=1, default='N')
    cola_amount = models.CharField(max_length=999, default='0')
    fixed_schedule = models.CharField(max_length=2, default='N')
    emp_status = models.CharField(max_length=50, default='')
    date_fired = models.CharField(max_length=50, default='')
    bir_schedule = models.CharField(max_length=10, default='0')
    dtr_rotation_id = models.CharField(max_length=20, default='0')
    am_only = models.CharField(max_length=2, default='Y')
    pm_only = models.CharField(max_length=2, default='Y')
    salary_type = models.CharField(max_length=25, default='')
    restday = models.CharField(max_length=20, null=True)
    flexitime = models.CharField(max_length=20, null=True)
    flexifirstin = models.CharField(max_length=20, null=True)
    flexifirstout = models.CharField(max_length=20, null=True)
    flexisecondin = models.CharField(max_length=20, null=True)
    flexisecondout = models.CharField(max_length=20, null=True)
    flexithirdin = models.CharField(max_length=20, null=True)
    flexithirdout = models.CharField(max_length=20, null=True)
    sl_category = models.CharField(max_length=50, default='')
    edtr = models.CharField(max_length=30, default='')
    dtar = models.CharField(max_length=1, default='N')
    mdtr = models.CharField(max_length=30, default='')
    mdtr_type = models.CharField(max_length=30, default='')
    unworkedholidaypay = models.CharField(max_length=2, default='N')
    unworkedholidayrestdaypay = models.CharField(max_length=2, default='N')
    locale = models.CharField(max_length=50, default='')
    nogrosspay = models.CharField(max_length=2, default='N')
    noholidaypay = models.CharField(max_length=2, default='N')
    nootpay = models.CharField(max_length=2, default='N')
    otwopay = models.CharField(max_length=4, default='N')
    min_take_home_pay = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    include_payroll = models.CharField(max_length=1, default='Y')
    sync_status = models.CharField(max_length=4, default='NO')

    class Meta:
        db_table = 'tbl_employee'
        
class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255)
    bdate = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


    class Meta:
        db_table = 'tbluser'