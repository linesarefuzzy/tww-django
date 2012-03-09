# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Accountclasses(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    classid = models.CharField(max_length=765, db_column='ClassID') # Field name made lowercase.
    superclassid = models.CharField(max_length=765, db_column='SuperClassID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name') # Field name made lowercase.
    nombre = models.CharField(max_length=765, db_column='Nombre') # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AccountClasses'

class Accounttypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    class Meta:
        db_table = u'AccountTypes'

class Accounts(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    externalaccountingid = models.CharField(unique=True, max_length=45, db_column='ExternalAccountingID', blank=True) # Field name made lowercase.
    name = models.CharField(unique=True, max_length=255, db_column='Name') # Field name made lowercase.
    nombre = models.CharField(max_length=765, db_column='Nombre') # Field name made lowercase.
    externalaccountingname = models.CharField(max_length=765, db_column='ExternalAccountingName', blank=True) # Field name made lowercase.
    divisionid = models.IntegerField(db_column='DivisionID') # Field name made lowercase.
    currency = models.IntegerField(db_column='Currency') # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    type = models.IntegerField(db_column='Type') # Field name made lowercase.
    externalparty = models.IntegerField(null=True, db_column='ExternalParty', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Accounts'

class Basicprojects(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    type = models.CharField(max_length=90, db_column='Type') # Field name made lowercase.
    length = models.FloatField(db_column='Length') # Field name made lowercase.
    nivel = models.CharField(max_length=600, db_column='Nivel') # Field name made lowercase.
    coordinator = models.IntegerField(null=True, db_column='Coordinator', blank=True) # Field name made lowercase.
    assistant = models.IntegerField(null=True, db_column='Assistant', blank=True) # Field name made lowercase.
    goal = models.IntegerField(null=True, db_column='Goal', blank=True) # Field name made lowercase.
    startdate = models.DateTimeField(null=True, db_column='StartDate', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name') # Field name made lowercase.
    shortdescription = models.TextField(db_column='ShortDescription') # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'BasicProjects'

class Blog(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    title = models.CharField(max_length=765, db_column='Title') # Field name made lowercase.
    text = models.TextField(db_column='Text') # Field name made lowercase.
    type = models.CharField(max_length=765, db_column='Type') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    class Meta:
        db_table = u'Blog'

class Checks(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    banco = models.CharField(max_length=600, db_column='Banco') # Field name made lowercase.
    numerodecheque = models.CharField(max_length=150, db_column='NumeroDeCheque') # Field name made lowercase.
    accountholder = models.CharField(max_length=765, db_column='AccountHolder') # Field name made lowercase.
    amount = models.FloatField(db_column='Amount') # Field name made lowercase.
    loanid = models.IntegerField(db_column='LoanID') # Field name made lowercase.
    dateentered = models.DateField(db_column='DateEntered') # Field name made lowercase.
    datedue = models.DateField(db_column='DateDue') # Field name made lowercase.
    dateremoved = models.DateField(null=True, db_column='DateRemoved', blank=True) # Field name made lowercase.
    datebounced = models.DateField(null=True, db_column='DateBounced', blank=True) # Field name made lowercase.
    exidente = models.FloatField(null=True, db_column='Exidente', blank=True) # Field name made lowercase.
    gastosfinancieros = models.FloatField(null=True, db_column='GastosFinancieros', blank=True) # Field name made lowercase.
    impuesto = models.FloatField(null=True, db_column='Impuesto', blank=True) # Field name made lowercase.
    bounced = models.IntegerField(null=True, db_column='Bounced', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Checks'

class Cooperatives(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    labase_fund_account_id = models.IntegerField(null=True, db_column='LaBaseFundAccountID', blank=True) # Field name made lowercase.
    redtekufenfund_account_id = models.IntegerField(null=True, db_column='RedTekufenFundAccountID', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=750, db_column='Name') # Field name made lowercase.
    alias = models.CharField(max_length=600, db_column='Alias', blank=True) # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=600, db_column='City') # Field name made lowercase.
    country = models.CharField(max_length=600, db_column='Country') # Field name made lowercase.
    web = models.CharField(max_length=765)
    contact = models.TextField(db_column='Contact', blank=True) # Field name made lowercase.
    ownership = models.CharField(max_length=750, db_column='Ownership', blank=True) # Field name made lowercase.
    ownership_change_date = models.DateTimeField(null=True, db_column='OwnershipChangeDate', blank=True) # Field name made lowercase.
    recuperada = models.IntegerField(db_column='Recuperada') # Field name made lowercase.
    sector = models.CharField(max_length=600, db_column='Sector', blank=True) # Field name made lowercase.
    industry = models.CharField(max_length=600, db_column='Industry', blank=True) # Field name made lowercase.
    source = models.CharField(max_length=750, db_column='Source', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Cooperatives'
    def __unicode__(self):
        return self.name

class Currencies(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    symbol = models.CharField(max_length=60, db_column='Symbol') # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    defaultcurrency = models.IntegerField(db_column='DefaultCurrency') # Field name made lowercase.
    country = models.CharField(max_length=765, db_column='Country') # Field name made lowercase.
    exchangerate = models.FloatField(db_column='ExchangeRate') # Field name made lowercase.
    class Meta:
        db_table = u'Currencies'

class Divisions(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name') # Field name made lowercase.
    externalname = models.CharField(max_length=765, db_column='ExternalName', blank=True) # Field name made lowercase.
    accountdivision = models.IntegerField(db_column='AccountDivision') # Field name made lowercase.
    superdivision = models.IntegerField(null=True, db_column='SuperDivision', blank=True) # Field name made lowercase.
    country = models.CharField(max_length=360, db_column='Country') # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    class Meta:
        db_table = u'Divisions'

class Exchangerates(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    currencyid = models.IntegerField(db_column='CurrencyID') # Field name made lowercase.
    exchangerate = models.FloatField(db_column='ExchangeRate') # Field name made lowercase.
    datestart = models.DateField(db_column='DateStart') # Field name made lowercase.
    dateend = models.DateField(db_column='DateEnd') # Field name made lowercase.
    class Meta:
        db_table = u'ExchangeRates'

class Goals(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    dateactivated = models.DateField(db_column='DateActivated') # Field name made lowercase.
    datedisactivated = models.DateField(null=True, db_column='DateDisactivated', blank=True) # Field name made lowercase.
    supergoal = models.IntegerField(null=True, db_column='SuperGoal', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Goals'

class Grouptransactionids(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    startertransaction = models.IntegerField(null=True, db_column='StarterTransaction', blank=True) # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated') # Field name made lowercase.
    class Meta:
        db_table = u'GroupTransactionIDs'

class Inflowtypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=150, db_column='Name') # Field name made lowercase.
    nombre = models.CharField(max_length=765, db_column='Nombre', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    scope = models.CharField(max_length=210, db_column='Scope') # Field name made lowercase.
    fromaccount = models.CharField(max_length=765, db_column='FromAccount', blank=True) # Field name made lowercase.
    toaccount = models.CharField(max_length=765, db_column='ToAccount', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'InflowTypes'

class Inventory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    productid = models.CharField(max_length=150, db_column='ProductID') # Field name made lowercase.
    productsubtype = models.IntegerField(null=True, db_column='ProductSubtype', blank=True) # Field name made lowercase.
    location = models.CharField(max_length=300, db_column='Location') # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity') # Field name made lowercase.
    current = models.IntegerField(db_column='Current') # Field name made lowercase.
    datemodified = models.DateTimeField(db_column='DateModified') # Field name made lowercase.
    class Meta:
        db_table = u'Inventory'

class Languages(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    code = models.CharField(max_length=6, db_column='Code') # Field name made lowercase.
    name = models.CharField(max_length=600, db_column='Name') # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority') # Field name made lowercase.
    class Meta:
        db_table = u'Languages'

class Loanagenttransactions(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    account = models.IntegerField(db_column='Account') # Field name made lowercase.
    memberid = models.IntegerField(null=True, db_column='MemberID', blank=True) # Field name made lowercase.
    loan = models.IntegerField(null=True, db_column='Loan', blank=True) # Field name made lowercase.
    inflowtype = models.IntegerField(null=True, db_column='InflowType', blank=True) # Field name made lowercase.
    outflowtype = models.IntegerField(null=True, db_column='OutflowType', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    details = models.TextField(db_column='Details', blank=True) # Field name made lowercase.
    datecash = models.DateField(null=True, db_column='DateCash', blank=True) # Field name made lowercase.
    formula = models.CharField(max_length=765, db_column='Formula', blank=True) # Field name made lowercase.
    amount = models.FloatField(null=True, db_column='Amount', blank=True) # Field name made lowercase.
    linkedtransaction = models.IntegerField(null=True, db_column='LinkedTransaction', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LoanAgentTransactions'

class Loaninstallments(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    loanid = models.IntegerField(db_column='LoanID') # Field name made lowercase.
    datedue = models.DateField(db_column='DateDue') # Field name made lowercase.
    capitalcuota = models.IntegerField(db_column='CapitalCuota') # Field name made lowercase.
    interestcuota = models.IntegerField(null=True, db_column='InterestCuota', blank=True) # Field name made lowercase.
    daterefinanced = models.DateField(null=True, db_column='DateRefinanced', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LoanInstallments'

class Loanquestions(models.Model):
    id = models.IntegerField(primary_key=True)
    orden = models.IntegerField(db_column='Orden') # Field name made lowercase.
    question = models.TextField()
    grupo = models.IntegerField(null=True, db_column='Grupo', blank=True) # Field name made lowercase.
    type = models.CharField(max_length=60, db_column='Type') # Field name made lowercase.
    active = models.IntegerField(db_column='Active') # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='dateCreated') # Field name made lowercase.
    class Meta:
        db_table = u'LoanQuestions'

class Loanrequests(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=300, db_column='Name') # Field name made lowercase.
    contact = models.CharField(max_length=600, db_column='Contact') # Field name made lowercase.
    location = models.CharField(max_length=600, db_column='Location') # Field name made lowercase.
    members = models.CharField(max_length=765, db_column='Members', blank=True) # Field name made lowercase.
    unit = models.CharField(max_length=150, db_column='Unit') # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    daterequested = models.DateTimeField(db_column='DateRequested') # Field name made lowercase.
    answered = models.IntegerField(db_column='Answered') # Field name made lowercase.
    class Meta:
        db_table = u'LoanRequests'

class Loanresponsesets(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    responsesetid = models.IntegerField(unique=True, db_column='ResponseSetID') # Field name made lowercase.
    loanid = models.IntegerField(unique=True, db_column='LoanID') # Field name made lowercase.
    class Meta:
        db_table = u'LoanResponseSets'

class Loanresponses(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    questionid = models.IntegerField(db_column='QuestionID') # Field name made lowercase.
    responsesetid = models.IntegerField(db_column='ResponseSetID') # Field name made lowercase.
    answer = models.TextField(db_column='Answer') # Field name made lowercase.
    rating = models.IntegerField(null=True, db_column='Rating', blank=True) # Field name made lowercase.
    saved = models.IntegerField(db_column='Saved') # Field name made lowercase.
    created = models.DateTimeField(null=True, db_column='Created', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LoanResponses'

class Loantypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    englishname = models.CharField(max_length=765, db_column='EnglishName') # Field name made lowercase.
    spanishname = models.CharField(max_length=765, db_column='SpanishName') # Field name made lowercase.
    englishdescription = models.TextField(db_column='EnglishDescription') # Field name made lowercase.
    spanishdescription = models.TextField(db_column='SpanishDescription', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'LoanTypes'

class Loans(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    amount = models.IntegerField(null=True, db_column='Amount', blank=True) # Field name made lowercase.
    rate = models.FloatField(null=True, db_column='Rate', blank=True) # Field name made lowercase.
    length = models.IntegerField(null=True, db_column='Length', blank=True) # Field name made lowercase.
    loantype = models.IntegerField(db_column='LoanType') # Field name made lowercase.
    sourcedivision = models.IntegerField(db_column='SourceDivision') # Field name made lowercase.
    nivel = models.CharField(max_length=600, db_column='Nivel') # Field name made lowercase.
    cooperative = models.ForeignKey(Cooperatives, db_column='CooperativeID') # Field name made lowercase.
    cooperative_members = models.IntegerField(null=True, db_column='CooperativeMembers', blank=True) # Field name made lowercase.
    point_person = models.IntegerField(db_column='PointPerson') # Field name made lowercase.
    second = models.IntegerField(null=True, db_column='Second', blank=True) # Field name made lowercase.
    representative_id = models.IntegerField(null=True, db_column='RepresentativeID', blank=True) # Field name made lowercase.
    signing_date = models.DateField(null=True, db_column='SigningDate', blank=True) # Field name made lowercase.
    first_interest_payment = models.DateField(null=True, db_column='FirstInterestPayment', blank=True) # Field name made lowercase.
    first_payment_date = models.DateField(null=True, db_column='FirstPaymentDate', blank=True) # Field name made lowercase.
    fecha_de_finalizacion = models.DateTimeField(null=True, db_column='FechaDeFinalizacion', blank=True) # Field name made lowercase.
    contrato_electronico = models.CharField(max_length=765, db_column='ContratoElectronico', blank=True) # Field name made lowercase.
    prospective = models.IntegerField(null=True, db_column='Prospective', blank=True) # Field name made lowercase.
    projected_return = models.FloatField(null=True, db_column='ProjectedReturn', blank=True) # Field name made lowercase.
    short_description = models.TextField(db_column='ShortDescription') # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    short_description_english = models.TextField(db_column='ShortDescriptionEnglish', blank=True) # Field name made lowercase.
    description_english = models.TextField(db_column='DescriptionEnglish', blank=True) # Field name made lowercase.
    nivel_publico = models.CharField(max_length=300, db_column='NivelPublico', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Loans'
    def __unicode__(self):
        return 'Loan ID ' + unicode(self.id)

class Media(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    priority = models.IntegerField(null=True, db_column='Priority', blank=True) # Field name made lowercase.
    mediapath = models.CharField(max_length=600, db_column='MediaPath') # Field name made lowercase.
    contexttable = models.CharField(max_length=765, db_column='ContextTable') # Field name made lowercase.
    contextid = models.IntegerField(db_column='ContextID') # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID') # Field name made lowercase.
    oldcaption = models.TextField(db_column='OldCaption', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Media'

class Members(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    firstname = models.CharField(max_length=450, db_column='FirstName') # Field name made lowercase.
    lastname = models.CharField(max_length=450, db_column='LastName', blank=True) # Field name made lowercase.
    username = models.CharField(max_length=300, db_column='Username', blank=True) # Field name made lowercase.
    password = models.CharField(max_length=300, db_column='Password', blank=True) # Field name made lowercase.
    passcode = models.CharField(max_length=300, db_column='Passcode', blank=True) # Field name made lowercase.
    accessstatus = models.IntegerField(null=True, db_column='AccessStatus', blank=True) # Field name made lowercase.
    nationalid = models.CharField(max_length=105, db_column='NationalID', blank=True) # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=600, db_column='City', blank=True) # Field name made lowercase.
    country = models.CharField(max_length=600, db_column='Country', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=150, db_column='Phone', blank=True) # Field name made lowercase.
    mobile = models.CharField(max_length=180, blank=True)
    cooperativeid = models.IntegerField(null=True, db_column='CooperativeID', blank=True) # Field name made lowercase.
    birthdate = models.DateTimeField(null=True, db_column='BirthDate', blank=True) # Field name made lowercase.
    payroll = models.IntegerField(db_column='Payroll') # Field name made lowercase.
    class Meta:
        db_table = u'Members'

class Notasdeasambleas(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    note = models.TextField(db_column='Note') # Field name made lowercase.
    class Meta:
        db_table = u'NotasDeAsambleas'

class Notes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID') # Field name made lowercase.
    notedid = models.IntegerField(db_column='NotedID') # Field name made lowercase.
    notedtable = models.CharField(max_length=600, db_column='NotedTable') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    note = models.TextField(db_column='Note') # Field name made lowercase.
    class Meta:
        db_table = u'Notes'

class Orders(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(null=True, db_column='UserID', blank=True) # Field name made lowercase.
    transactionid = models.IntegerField(null=True, db_column='TransactionID', blank=True) # Field name made lowercase.
    donation = models.FloatField(null=True, db_column='Donation', blank=True) # Field name made lowercase.
    shipping = models.FloatField(null=True, db_column='Shipping', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name', blank=True) # Field name made lowercase.
    shippingaddress = models.CharField(max_length=765, db_column='ShippingAddress', blank=True) # Field name made lowercase.
    shippingaddress2 = models.CharField(max_length=600, db_column='ShippingAddress2', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=765, db_column='City', blank=True) # Field name made lowercase.
    province = models.CharField(max_length=765, db_column='Province', blank=True) # Field name made lowercase.
    country = models.CharField(max_length=765, db_column='Country', blank=True) # Field name made lowercase.
    postalcode = models.CharField(max_length=765, db_column='PostalCode', blank=True) # Field name made lowercase.
    emailaddress = models.CharField(max_length=765, db_column='EmailAddress', blank=True) # Field name made lowercase.
    date = models.DateTimeField(null=True, db_column='Date', blank=True) # Field name made lowercase.
    amazonfulfilmentrequestid = models.CharField(max_length=765, db_column='AmazonFulfilmentRequestID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Orders'

class Outflowtypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    scope = models.CharField(max_length=210, db_column='Scope') # Field name made lowercase.
    name = models.CharField(unique=True, max_length=150, db_column='Name') # Field name made lowercase.
    nombre = models.CharField(max_length=765, db_column='Nombre', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    fromaccount = models.CharField(unique=True, max_length=255, db_column='FromAccount', blank=True) # Field name made lowercase.
    toaccount = models.CharField(unique=True, max_length=255, db_column='ToAccount', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'OutflowTypes'

class Productsubtypecategories(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name') # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ProductSubtypeCategories'

class Productsubtypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    subtypecategoryid = models.IntegerField(db_column='SubtypeCategoryID') # Field name made lowercase.
    consumerdescription = models.CharField(max_length=765, db_column='ConsumerDescription') # Field name made lowercase.
    consumerselectiondisplay = models.CharField(max_length=765, db_column='ConsumerSelectionDisplay', blank=True) # Field name made lowercase.
    coopdescription = models.CharField(max_length=765, db_column='CoopDescription', blank=True) # Field name made lowercase.
    displayorder = models.FloatField(null=True, db_column='DisplayOrder', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ProductSubtypes'

class Products(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    productid = models.CharField(max_length=150, db_column='ProductID') # Field name made lowercase.
    identifierusedbycoop = models.CharField(max_length=765, db_column='IDentifierUsedByCoop', blank=True) # Field name made lowercase.
    harmonizedtariffcode = models.CharField(max_length=45, db_column='HarmonizedTariffCode', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=600, db_column='Name', blank=True) # Field name made lowercase.
    productcategory = models.CharField(max_length=300, db_column='ProductCategory') # Field name made lowercase.
    sizesandcolors = models.CharField(max_length=600, db_column='SizesAndColors', blank=True) # Field name made lowercase.
    subtypecategoryid = models.IntegerField(null=True, db_column='SubtypeCategoryID', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    mainimage = models.CharField(max_length=600, db_column='MainImage', blank=True) # Field name made lowercase.
    price = models.CharField(max_length=765, db_column='Price', blank=True) # Field name made lowercase.
    currencyid = models.IntegerField(null=True, db_column='CurrencyID', blank=True) # Field name made lowercase.
    weight = models.FloatField(null=True, db_column='Weight', blank=True) # Field name made lowercase.
    length = models.FloatField(null=True, db_column='Length', blank=True) # Field name made lowercase.
    width = models.FloatField(null=True, db_column='Width', blank=True) # Field name made lowercase.
    height = models.FloatField(null=True, db_column='Height', blank=True) # Field name made lowercase.
    specialfundrate = models.FloatField(null=True, db_column='SpecialFundRate', blank=True) # Field name made lowercase.
    specialtaxrate = models.FloatField(null=True, db_column='SpecialTaxRate', blank=True) # Field name made lowercase.
    cooperativeid = models.IntegerField(null=True, db_column='CooperativeID', blank=True) # Field name made lowercase.
    dateavailable = models.DateTimeField(db_column='DateAvailable') # Field name made lowercase.
    datewithdrawn = models.DateTimeField(null=True, db_column='DateWithdrawn', blank=True) # Field name made lowercase.
    displaytype = models.CharField(max_length=300, db_column='DisplayType') # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder') # Field name made lowercase.
    amazonname = models.CharField(max_length=1500, db_column='AmazonName', blank=True) # Field name made lowercase.
    amazonbulletpoints = models.CharField(max_length=1515, db_column='AmazonBulletPoints', blank=True) # Field name made lowercase.
    amazonclothingtype = models.CharField(max_length=765, db_column='AmazonClothingType', blank=True) # Field name made lowercase.
    amazonmaterialfabric = models.CharField(max_length=765, db_column='AmazonMaterialFabric', blank=True) # Field name made lowercase.
    amazondepartment = models.CharField(max_length=1200, db_column='AmazonDepartment', blank=True) # Field name made lowercase.
    amazonstylekeyword = models.CharField(max_length=1200, db_column='AmazonStyleKeyword', blank=True) # Field name made lowercase.
    amazonoccasionlifestyle = models.CharField(max_length=1200, db_column='AmazonOccasionLifestyle', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Products'

class Productsordered(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    productsubtype = models.IntegerField(db_column='ProductSubtype') # Field name made lowercase.
    productid = models.CharField(max_length=765, db_column='ProductID', blank=True) # Field name made lowercase.
    orderid = models.IntegerField(null=True, db_column='OrderID', blank=True) # Field name made lowercase.
    shipmentid = models.IntegerField(null=True, db_column='ShipmentID', blank=True) # Field name made lowercase.
    price = models.FloatField(null=True, db_column='Price', blank=True) # Field name made lowercase.
    quantity = models.IntegerField(null=True, db_column='Quantity', blank=True) # Field name made lowercase.
    size = models.CharField(max_length=765, db_column='Size', blank=True) # Field name made lowercase.
    color = models.CharField(max_length=765, db_column='Color', blank=True) # Field name made lowercase.
    characteristics = models.CharField(max_length=765, db_column='Characteristics', blank=True) # Field name made lowercase.
    funddonation = models.FloatField(null=True, db_column='FundDonation', blank=True) # Field name made lowercase.
    taxes = models.FloatField(null=True, db_column='Taxes', blank=True) # Field name made lowercase.
    datecoopgivenorder = models.DateTimeField(null=True, db_column='DateCoopGivenOrder', blank=True) # Field name made lowercase.
    datecooppaid = models.DateTimeField(null=True, db_column='DateCoopPaid', blank=True) # Field name made lowercase.
    datetaxespaid = models.DateTimeField(null=True, db_column='DateTaxesPaid', blank=True) # Field name made lowercase.
    credittransactioncost = models.FloatField(null=True, db_column='CreditTransactionCost', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ProductsOrdered'

class Projectevents(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID') # Field name made lowercase.
    projectid = models.IntegerField(db_column='ProjectID') # Field name made lowercase.
    projecttable = models.CharField(max_length=765, db_column='ProjectTable') # Field name made lowercase.
    summary = models.CharField(max_length=765, db_column='Summary') # Field name made lowercase.
    details = models.TextField(db_column='Details', blank=True) # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    finalized = models.IntegerField(db_column='Finalized') # Field name made lowercase.
    completed = models.DateField(null=True, db_column='Completed', blank=True) # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate') # Field name made lowercase.
    type = models.CharField(max_length=105, db_column='Type') # Field name made lowercase.
    class Meta:
        db_table = u'ProjectEvents'

class Projectlogs(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID') # Field name made lowercase.
    projectid = models.IntegerField(db_column='ProjectID') # Field name made lowercase.
    projecttable = models.CharField(max_length=765, db_column='ProjectTable') # Field name made lowercase.
    pasoid = models.IntegerField(null=True, db_column='PasoID', blank=True) # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    progress = models.CharField(max_length=90, db_column='Progress') # Field name made lowercase.
    explanation = models.CharField(max_length=765, db_column='Explanation', blank=True) # Field name made lowercase.
    detailedexplanation = models.TextField(db_column='DetailedExplanation', blank=True) # Field name made lowercase.
    notasprivadas = models.TextField(db_column='NotasPrivadas', blank=True) # Field name made lowercase.
    additionalnotes = models.TextField(db_column='AdditionalNotes', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ProjectLogs'

class Repayments(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    loanid = models.IntegerField(db_column='LoanID') # Field name made lowercase.
    datedue = models.DateTimeField(db_column='DateDue') # Field name made lowercase.
    datepaid = models.DateTimeField(null=True, db_column='DatePaid', blank=True) # Field name made lowercase.
    amountdue = models.IntegerField(db_column='AmountDue') # Field name made lowercase.
    amountpaid = models.IntegerField(null=True, db_column='AmountPaid', blank=True) # Field name made lowercase.
    interestsincelastpayment = models.IntegerField(null=True, db_column='InterestSinceLastPayment', blank=True) # Field name made lowercase.
    daterefinanced = models.DateField(null=True, db_column='DateRefinanced', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Repayments'

class Shipments(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    orderid = models.IntegerField(unique=True, db_column='OrderID') # Field name made lowercase.
    trackingnumber = models.CharField(unique=True, max_length=255, db_column='TrackingNumber', blank=True) # Field name made lowercase.
    carrier = models.CharField(max_length=300, db_column='Carrier', blank=True) # Field name made lowercase.
    datetrackingnumberentered = models.DateTimeField(null=True, db_column='DateTrackingNumberEntered', blank=True) # Field name made lowercase.
    shipmentdate = models.DateField(null=True, db_column='ShipmentDate', blank=True) # Field name made lowercase.
    cost = models.FloatField(null=True, db_column='Cost', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Shipments'

class Shippingaddresses(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(null=True, db_column='UserID', blank=True) # Field name made lowercase.
    defaultaddress = models.IntegerField(null=True, db_column='DefaultAddress', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name', blank=True) # Field name made lowercase.
    street1 = models.CharField(max_length=765, db_column='Street1', blank=True) # Field name made lowercase.
    street2 = models.CharField(max_length=765, db_column='Street2', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=765, db_column='City', blank=True) # Field name made lowercase.
    province = models.CharField(max_length=765, db_column='Province', blank=True) # Field name made lowercase.
    country = models.CharField(max_length=765, db_column='Country', blank=True) # Field name made lowercase.
    postalcode = models.CharField(max_length=765, db_column='PostalCode', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ShippingAddresses'

class Storetransactions(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    response = models.CharField(max_length=765, db_column='Response', blank=True) # Field name made lowercase.
    errormessage = models.CharField(max_length=765, db_column='ErrorMessage', blank=True) # Field name made lowercase.
    userid = models.IntegerField(null=True, db_column='UserID', blank=True) # Field name made lowercase.
    accountnumber = models.CharField(max_length=765, db_column='AccountNumber', blank=True) # Field name made lowercase.
    expmonth = models.CharField(max_length=765, db_column='ExpMonth', blank=True) # Field name made lowercase.
    expyear = models.CharField(max_length=765, db_column='ExpYear', blank=True) # Field name made lowercase.
    cvv2 = models.CharField(max_length=15, db_column='CVV2', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name', blank=True) # Field name made lowercase.
    billingaddress = models.CharField(max_length=765, db_column='BillingAddress', blank=True) # Field name made lowercase.
    postalcode = models.CharField(max_length=765, db_column='PostalCode', blank=True) # Field name made lowercase.
    country = models.CharField(max_length=765, db_column='Country', blank=True) # Field name made lowercase.
    amount = models.FloatField(null=True, db_column='Amount', blank=True) # Field name made lowercase.
    date = models.DateTimeField(null=True, db_column='Date', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'StoreTransactions'

class Storeusercreditcards(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    userid = models.IntegerField(null=True, db_column='UserID', blank=True) # Field name made lowercase.
    defaultcard = models.IntegerField(null=True, db_column='DefaultCard', blank=True) # Field name made lowercase.
    firstname = models.CharField(max_length=765, db_column='FirstName', blank=True) # Field name made lowercase.
    lastname = models.CharField(max_length=765, db_column='LastName', blank=True) # Field name made lowercase.
    type = models.CharField(max_length=765, db_column='Type', blank=True) # Field name made lowercase.
    accountnumber = models.CharField(max_length=765, db_column='AccountNumber', blank=True) # Field name made lowercase.
    expmonth = models.CharField(max_length=765, db_column='ExpMonth', blank=True) # Field name made lowercase.
    expyear = models.CharField(max_length=765, db_column='ExpYear', blank=True) # Field name made lowercase.
    cvv2 = models.CharField(max_length=765, db_column='CVV2', blank=True) # Field name made lowercase.
    street1 = models.CharField(max_length=765, db_column='Street1', blank=True) # Field name made lowercase.
    street2 = models.CharField(max_length=765, db_column='Street2', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=765, db_column='City', blank=True) # Field name made lowercase.
    province = models.CharField(max_length=765, db_column='Province', blank=True) # Field name made lowercase.
    country = models.CharField(max_length=765, db_column='Country', blank=True) # Field name made lowercase.
    postalcode = models.CharField(max_length=765, db_column='PostalCode', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'StoreUserCreditCards'

class Storeuserlog(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    trackingid = models.CharField(max_length=60, db_column='TrackingID') # Field name made lowercase.
    useremail = models.CharField(max_length=150, db_column='UserEmail', blank=True) # Field name made lowercase.
    url = models.CharField(max_length=600, db_column='URL') # Field name made lowercase.
    query = models.CharField(max_length=765, db_column='Query') # Field name made lowercase.
    class Meta:
        db_table = u'StoreUserLog'

class Storeusers(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    email = models.CharField(unique=True, max_length=255, db_column='Email', blank=True) # Field name made lowercase.
    password = models.CharField(max_length=765, db_column='Password', blank=True) # Field name made lowercase.
    crypt = models.CharField(max_length=765, db_column='Crypt', blank=True) # Field name made lowercase.
    startdate = models.DateTimeField(null=True, db_column='StartDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'StoreUsers'

class Transactiontypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    scope = models.CharField(max_length=210, db_column='Scope') # Field name made lowercase.
    name = models.CharField(unique=True, max_length=150, db_column='Name') # Field name made lowercase.
    nombre = models.CharField(max_length=765, db_column='Nombre', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    fromaccount = models.CharField(unique=True, max_length=255, db_column='FromAccount', blank=True) # Field name made lowercase.
    toaccount = models.CharField(unique=True, max_length=255, db_column='ToAccount', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TransactionTypes'

class Transactions(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    grouptransactionid = models.IntegerField(null=True, db_column='GroupTransactionID', blank=True) # Field name made lowercase.
    account = models.IntegerField(db_column='Account') # Field name made lowercase.
    memberid = models.IntegerField(null=True, db_column='MemberID', blank=True) # Field name made lowercase.
    loan = models.IntegerField(null=True, db_column='Loan', blank=True) # Field name made lowercase.
    checkid = models.IntegerField(null=True, db_column='CheckID', blank=True) # Field name made lowercase.
    transactiontype = models.IntegerField(null=True, db_column='TransactionType', blank=True) # Field name made lowercase.
    inflowtype = models.IntegerField(null=True, db_column='InflowType', blank=True) # Field name made lowercase.
    outflowtype = models.IntegerField(null=True, db_column='OutflowType', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    tipodedocumento = models.CharField(max_length=765, db_column='TipoDeDocumento', blank=True) # Field name made lowercase.
    numerodedocumento = models.CharField(max_length=765, db_column='NumeroDeDocumento', blank=True) # Field name made lowercase.
    details = models.TextField(db_column='Details', blank=True) # Field name made lowercase.
    filtradoporsistemaeleo = models.IntegerField(db_column='FiltradoPorSistemaEleo') # Field name made lowercase.
    solamenteensistemaeleo = models.IntegerField(db_column='SolamenteEnSistemaEleo') # Field name made lowercase.
    dateaccrual = models.DateField(null=True, db_column='DateAccrual', blank=True) # Field name made lowercase.
    datecash = models.DateField(null=True, db_column='DateCash', blank=True) # Field name made lowercase.
    formula = models.CharField(max_length=765, db_column='Formula', blank=True) # Field name made lowercase.
    amount = models.FloatField(db_column='Amount') # Field name made lowercase.
    amountfixed = models.FloatField(null=True, db_column='AmountFixed', blank=True) # Field name made lowercase.
    credit = models.FloatField(null=True, db_column='Credit', blank=True) # Field name made lowercase.
    debit = models.FloatField(null=True, db_column='Debit', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Transactions'

class Transactionshold(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    account = models.IntegerField(db_column='Account') # Field name made lowercase.
    incometype = models.IntegerField(null=True, db_column='IncomeType', blank=True) # Field name made lowercase.
    expendituretype = models.IntegerField(null=True, db_column='ExpenditureType', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    date = models.DateField(null=True, db_column='Date', blank=True) # Field name made lowercase.
    formula = models.CharField(max_length=765, db_column='Formula', blank=True) # Field name made lowercase.
    amount = models.IntegerField(null=True, db_column='Amount', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TransactionsHold'

class Translations(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    language = models.IntegerField(db_column='Language') # Field name made lowercase.
    remoteid = models.IntegerField(db_column='RemoteID') # Field name made lowercase.
    remotetable = models.CharField(max_length=600, db_column='RemoteTable') # Field name made lowercase.
    remotecolumnname = models.CharField(max_length=600, db_column='RemoteColumnName') # Field name made lowercase.
    translatedcontent = models.TextField(db_column='TranslatedContent') # Field name made lowercase.
    class Meta:
        db_table = u'Translations'

class Vendororders(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    daterequested = models.DateTimeField(null=True, db_column='DateRequested', blank=True) # Field name made lowercase.
    datereceived = models.DateTimeField(null=True, db_column='DateReceived', blank=True) # Field name made lowercase.
    productid = models.CharField(max_length=300, db_column='ProductID') # Field name made lowercase.
    productsubtype = models.IntegerField(db_column='ProductSubtype') # Field name made lowercase.
    transactionid = models.IntegerField(null=True, db_column='TransactionID', blank=True) # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity') # Field name made lowercase.
    price = models.FloatField(db_column='Price') # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'VendorOrders'

class Workchangelog(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    worklogid = models.IntegerField(db_column='WorkLogID') # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID') # Field name made lowercase.
    starttime = models.DateTimeField(null=True, db_column='StartTime', blank=True) # Field name made lowercase.
    endtime = models.DateTimeField(null=True, db_column='EndTime', blank=True) # Field name made lowercase.
    client = models.CharField(max_length=765, db_column='Client', blank=True) # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime') # Field name made lowercase.
    class Meta:
        db_table = u'WorkChangeLog'

class Worklog(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID') # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime') # Field name made lowercase.
    endtime = models.DateTimeField(null=True, db_column='EndTime', blank=True) # Field name made lowercase.
    startclient = models.CharField(max_length=765, db_column='StartClient', blank=True) # Field name made lowercase.
    endclient = models.CharField(max_length=765, db_column='EndClient', blank=True) # Field name made lowercase.
    activitytype = models.CharField(max_length=300, db_column='ActivityType', blank=True) # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    pasoid = models.IntegerField(null=True, db_column='PasoID', blank=True) # Field name made lowercase.
    activitycategory = models.CharField(max_length=765, db_column='ActivityCategory', blank=True) # Field name made lowercase.
    activitydescription = models.TextField(db_column='ActivityDescription', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'WorkLog'

class Workervacation(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID') # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate') # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate') # Field name made lowercase.
    class Meta:
        db_table = u'WorkerVacation'

class Mailinglist(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=600)
    lastname = models.CharField(max_length=600)
    email = models.CharField(max_length=600)
    startdate = models.DateTimeField()
    class Meta:
        db_table = u'mailinglist'

class Test(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    test = models.CharField(max_length=765, db_column='Test') # Field name made lowercase.
    thedate = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'test'

class Todo(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority') # Field name made lowercase.
    status = models.CharField(max_length=90, db_column='STATUS') # Field name made lowercase.
    pointperson = models.IntegerField(null=True, db_column='PointPerson', blank=True) # Field name made lowercase.
    second = models.IntegerField(null=True, db_column='Second', blank=True) # Field name made lowercase.
    modified = models.DateField(db_column='Modified') # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    class Meta:
        db_table = u'todo'

