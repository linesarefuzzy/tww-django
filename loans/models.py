# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#	  * Rearrange models' order
#	  * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from django.contrib.auth.models import User

class Currency(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	name = models.CharField(max_length=150, db_column='Name')
	symbol = models.CharField(max_length=60, db_column='Symbol')
	description = models.TextField(db_column='Description')
	default_currency = models.IntegerField(db_column='DefaultCurrency')
	country = models.CharField(max_length=765, db_column='Country')
	exchange_rate = models.FloatField(db_column='ExchangeRate')
	class Meta:
		db_table = u'Currencies'
		verbose_name_plural = 'currencies'
	def __unicode__(self):
		return self.symbol

class Division(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	name = models.CharField(max_length=765, db_column='Name')
	external_name = models.CharField(max_length=765, db_column='ExternalName', blank=True)
	account_division = models.IntegerField(db_column='AccountDivision')
	super_division = models.IntegerField(null=True, db_column='SuperDivision', blank=True)
	country = models.CharField(max_length=360, db_column='Country')
	description = models.TextField(db_column='Description')
	class Meta:
		db_table = u'Divisions'
	def __unicode__(self):
		return self.name

class Member(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	first_name = models.CharField(max_length=450, db_column='FirstName')
	last_name = models.CharField(max_length=450, db_column='LastName', blank=True)
	username = models.CharField(max_length=300, db_column='Username', blank=True)
	password = models.CharField(max_length=300, db_column='Password', blank=True)
	passcode = models.CharField(max_length=300, db_column='Passcode', blank=True)
	access_status = models.IntegerField(null=True, db_column='AccessStatus', blank=True)
	national_id = models.CharField(max_length=105, db_column='NationalID', blank=True)
	address = models.TextField(db_column='Address', blank=True)
	city = models.CharField(max_length=600, db_column='City', blank=True)
	country = models.CharField(max_length=600, db_column='Country', blank=True)
	phone = models.CharField(max_length=150, db_column='Phone', blank=True)
	mobile = models.CharField(max_length=180, blank=True)
	cooperative_id = models.IntegerField(null=True, db_column='CooperativeID', blank=True)
	birth_date = models.DateTimeField(null=True, db_column='BirthDate', blank=True)
	payroll = models.IntegerField(db_column='Payroll')
	class Meta:
		db_table = u'Members'
	def __unicode__(self):
		return unicode(self.first_name) + u' ' + unicode(self.last_name)

class AccountClass(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	class_id = models.CharField(max_length=765, db_column='ClassID')
	super_class_id = models.CharField(max_length=765, db_column='SuperClassID', blank=True)
	name = models.CharField(max_length=765, db_column='Name')
	nombre = models.CharField(max_length=765, db_column='Nombre')
	description = models.TextField(db_column='Description', blank=True)
	class Meta:
		db_table = u'AccountClasses'
		verbose_name_plural = "account classes"
	def __unicode__(self):
		return self.name

class AccountType(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	name = models.CharField(max_length=150, db_column='Name')
	description = models.TextField(db_column='Description')
	class Meta:
		db_table = u'AccountTypes'
	def __unicode__(self):
		return self.name

class Account(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	external_accounting_id = models.CharField(unique=True, max_length=45, db_column='ExternalAccountingID', blank=True)
	name = models.CharField(unique=True, max_length=255, db_column='Name')
	nombre = models.CharField(max_length=765, db_column='Nombre')
	external_accounting_name = models.CharField(max_length=765, db_column='ExternalAccountingName', blank=True)
	division = models.ForeignKey(Division, db_column='DivisionID')
	currency = models.ForeignKey(Currency, db_column='Currency')
	description = models.TextField(db_column='Description')
	type = models.IntegerField(db_column='Type')
	external_party = models.IntegerField(null=True, db_column='ExternalParty', blank=True)
	class Meta:
		db_table = u'Accounts'
	def __unicode__(self):
		return self.name

class BasicProject(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	type = models.CharField(max_length=90, db_column='Type')
	length = models.FloatField(db_column='Length')
	nivel = models.CharField(max_length=600, db_column='Nivel')
	coordinator = models.IntegerField(null=True, db_column='Coordinator', blank=True)
	assistant = models.IntegerField(null=True, db_column='Assistant', blank=True)
	goal = models.IntegerField(null=True, db_column='Goal', blank=True)
	start_date = models.DateTimeField(null=True, db_column='StartDate', blank=True)
	name = models.CharField(max_length=765, db_column='Name')
	short_description = models.TextField(db_column='ShortDescription')
	description = models.TextField(db_column='Description', blank=True)
	class Meta:
		db_table = u'BasicProjects'

class Blog(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	title = models.CharField(max_length=765, db_column='Title')
	text = models.TextField(db_column='Text')
	type = models.CharField(max_length=765, db_column='Type')
	date = models.DateTimeField(db_column='Date')
	class Meta:
		db_table = u'Blog'

class Check(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	banco = models.CharField(max_length=600, db_column='Banco')
	numero_de_cheque = models.CharField(max_length=150, db_column='NumeroDeCheque')
	account_holder = models.CharField(max_length=765, db_column='AccountHolder')
	amount = models.FloatField(db_column='Amount')
	loan_id = models.IntegerField(db_column='LoanID')
	date_entered = models.DateField(db_column='DateEntered')
	date_due = models.DateField(db_column='DateDue')
	date_removed = models.DateField(null=True, db_column='DateRemoved', blank=True)
	date_bounced = models.DateField(null=True, db_column='DateBounced', blank=True)
	exidente = models.FloatField(null=True, db_column='Exidente', blank=True)
	gastos_financieros = models.FloatField(null=True, db_column='GastosFinancieros', blank=True)
	impuesto = models.FloatField(null=True, db_column='Impuesto', blank=True)
	bounced = models.IntegerField(null=True, db_column='Bounced', blank=True)
	notes = models.TextField(db_column='Notes', blank=True)
	class Meta:
		db_table = u'Checks'

class Cooperative(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	la_base_fund_account_id = models.IntegerField(null=True, db_column='LaBaseFundAccountID', blank=True)
	red_tekufen_fund_account_id = models.IntegerField(null=True, db_column='RedTekufenFundAccountID', blank=True)
	name = models.CharField(max_length=750, db_column='Name')
	alias = models.CharField(max_length=600, db_column='Alias', blank=True)
	address = models.TextField(db_column='Address', blank=True)
	city = models.CharField(max_length=600, db_column='City')
	country = models.CharField(max_length=600, db_column='Country')
	web = models.CharField(max_length=765)
	contact = models.TextField(db_column='Contact', blank=True)
	ownership = models.CharField(max_length=750, db_column='Ownership', blank=True)
	ownership_change_date = models.DateTimeField(null=True, db_column='OwnershipChangeDate', blank=True)
	recuperada = models.IntegerField(db_column='Recuperada')
	sector = models.CharField(max_length=600, db_column='Sector', blank=True)
	industry = models.CharField(max_length=600, db_column='Industry', blank=True)
	source = models.CharField(max_length=750, db_column='Source', blank=True)
	# thumb_path = MediaManager()
	class Meta:
		db_table = u'Cooperatives'
	def __unicode__(self):
		return self.name

	def picture_path(self):
		return get_picture_path('Cooperatives', self.id)
	picture_path = property(picture_path)

	def thumb_path(self):
		return get_thumb_path('Cooperatives', self.id)
	thumb_path = property(thumb_path)

class ExchangeRate(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	currency_id = models.IntegerField(db_column='CurrencyID')
	exchange_rate = models.FloatField(db_column='ExchangeRate')
	date_start = models.DateField(db_column='DateStart')
	date_end = models.DateField(db_column='DateEnd')
	class Meta:
		db_table = u'ExchangeRates'

class Goal(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	name = models.CharField(max_length=150, db_column='Name')
	description = models.TextField(db_column='Description')
	date_activated = models.DateField(db_column='DateActivated')
	date_disactivated = models.DateField(null=True, db_column='DateDisactivated', blank=True)
	super_goal = models.IntegerField(null=True, db_column='SuperGoal', blank=True)
	class Meta:
		db_table = u'Goals'

class GroupTransactionID(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	starter_transaction = models.IntegerField(null=True, db_column='StarterTransaction', blank=True)
	date_created = models.DateTimeField(db_column='DateCreated')
	class Meta:
		db_table = u'GroupTransactionIDs'

class InflowType(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	name = models.CharField(max_length=150, db_column='Name')
	nombre = models.CharField(max_length=765, db_column='Nombre', blank=True)
	description = models.TextField(db_column='Description')
	scope = models.CharField(max_length=210, db_column='Scope')
	from_account = models.CharField(max_length=765, db_column='FromAccount', blank=True)
	to_account = models.CharField(max_length=765, db_column='ToAccount', blank=True)
	class Meta:
		db_table = u'InflowTypes'

class Inventory(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	product_id = models.CharField(max_length=150, db_column='ProductID')
	product_subtype = models.IntegerField(null=True, db_column='ProductSubtype', blank=True)
	location = models.CharField(max_length=300, db_column='Location')
	quantity = models.IntegerField(db_column='Quantity')
	current = models.IntegerField(db_column='Current')
	date_modified = models.DateTimeField(db_column='DateModified')
	class Meta:
		db_table = u'Inventory'

class Language(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	code = models.CharField(max_length=6, db_column='Code')
	name = models.CharField(max_length=600, db_column='Name')
	priority = models.IntegerField(db_column='Priority')
	class Meta:
		db_table = u'Languages'
	def __unicode__(self):
		return unicode(self.name)

class Translation(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	language = models.ForeignKey(Language, db_column='Language')
	remote_id = models.IntegerField(db_column='RemoteID')
	remote_table = models.CharField(max_length=600, db_column='RemoteTable')
	remote_column_name = models.CharField(max_length=600, db_column='RemoteColumnName')
	translated_content = models.TextField(db_column='TranslatedContent')
	class Meta:
		db_table = u'Translations'
	def __unicode__(self):
		return unicode(self.id)

class LoanAgentTransaction(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	account = models.IntegerField(db_column='Account')
	member_id = models.IntegerField(null=True, db_column='MemberID', blank=True)
	loan = models.IntegerField(null=True, db_column='Loan', blank=True)
	inflow_type = models.IntegerField(null=True, db_column='InflowType', blank=True)
	outflow_type = models.IntegerField(null=True, db_column='OutflowType', blank=True)
	description = models.TextField(db_column='Description')
	details = models.TextField(db_column='Details', blank=True)
	date_cash = models.DateField(null=True, db_column='DateCash', blank=True)
	formula = models.CharField(max_length=765, db_column='Formula', blank=True)
	amount = models.FloatField(null=True, db_column='Amount', blank=True)
	linked_transaction = models.IntegerField(null=True, db_column='LinkedTransaction', blank=True)
	class Meta:
		db_table = u'LoanAgentTransactions'

class LoanInstallment(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	loan_id = models.IntegerField(db_column='LoanID')
	date_due = models.DateField(db_column='DateDue')
	capital_cuota = models.IntegerField(db_column='CapitalCuota')
	interest_cuota = models.IntegerField(null=True, db_column='InterestCuota', blank=True)
	date_refinanced = models.DateField(null=True, db_column='DateRefinanced', blank=True)
	class Meta:
		db_table = u'LoanInstallments'

class LoanQuestion(models.Model):
	id = models.AutoField(primary_key=True)
	orden = models.IntegerField(db_column='Orden')
	question = models.TextField()
	grupo = models.IntegerField(null=True, db_column='Grupo', blank=True)
	type = models.CharField(max_length=60, db_column='Type')
	active = models.IntegerField(db_column='Active')
	date_created = models.DateTimeField(db_column='dateCreated')
	class Meta:
		db_table = u'LoanQuestions'

class LoanRequest(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	name = models.CharField(max_length=300, db_column='Name')
	contact = models.CharField(max_length=600, db_column='Contact')
	location = models.CharField(max_length=600, db_column='Location')
	members = models.CharField(max_length=765, db_column='Members', blank=True)
	unit = models.CharField(max_length=150, db_column='Unit')
	description = models.TextField(db_column='Description')
	date_requested = models.DateTimeField(db_column='DateRequested')
	answered = models.IntegerField(db_column='Answered')
	class Meta:
		db_table = u'LoanRequests'

class LoanResponseSet(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	response_set_id = models.IntegerField(unique=True, db_column='ResponseSetID')
	loan_id = models.IntegerField(unique=True, db_column='LoanID')
	class Meta:
		db_table = u'LoanResponseSets'

class LoanResponse(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	question_id = models.IntegerField(db_column='QuestionID')
	response_set_id = models.IntegerField(db_column='ResponseSetID')
	answer = models.TextField(db_column='Answer')
	rating = models.IntegerField(null=True, db_column='Rating', blank=True)
	saved = models.IntegerField(db_column='Saved')
	created = models.DateTimeField(null=True, db_column='Created', blank=True)
	class Meta:
		db_table = u'LoanResponses'

class LoanType(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	english_name = models.CharField(max_length=765, db_column='EnglishName')
	spanish_name = models.CharField(max_length=765, db_column='SpanishName')
	english_description = models.TextField(db_column='EnglishDescription')
	spanish_description = models.TextField(db_column='SpanishDescription', blank=True)
	class Meta:
		db_table = u'LoanTypes'
	def __unicode__(self):
		return self.english_name

class Loan(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	amount = models.IntegerField(null=True, db_column='Amount', blank=True)
	rate = models.FloatField(null=True, db_column='Rate', blank=True)
	length = models.IntegerField(null=True, db_column='Length', blank=True)
	loan_type = models.ForeignKey(LoanType, db_column='LoanType')
	source_division = models.ForeignKey(Division, db_column='SourceDivision')
	nivel = models.CharField(max_length=600, db_column='Nivel')
	cooperative = models.ForeignKey(Cooperative, db_column='CooperativeID')
	cooperative_members = models.IntegerField(null=True, db_column='CooperativeMembers', blank=True)
	point_person = models.ForeignKey(Member, db_column='PointPerson')
	second = models.ForeignKey(Member, related_name='loan_second', null=True, db_column='Second', blank=True)
	representative_id = models.IntegerField(null=True, db_column='RepresentativeID', blank=True)
	signing_date = models.DateField(null=True, db_column='SigningDate', blank=True)
	first_interest_payment = models.DateField(null=True, db_column='FirstInterestPayment', blank=True)
	first_payment_date = models.DateField(null=True, db_column='FirstPaymentDate', blank=True)
	fecha_de_finalizacion = models.DateTimeField(null=True, db_column='FechaDeFinalizacion', blank=True)
	contrato_electronico = models.CharField(max_length=765, db_column='ContratoElectronico', blank=True)
	prospective = models.IntegerField(null=True, db_column='Prospective', blank=True)
	projected_return = models.FloatField(null=True, db_column='ProjectedReturn', blank=True)
	short_description = models.TextField(db_column='ShortDescription')
	description = models.TextField(db_column='Description', blank=True)
	short_description_english = models.TextField(db_column='ShortDescriptionEnglish', blank=True)
	description_english = models.TextField(db_column='DescriptionEnglish', blank=True)
	nivel_publico = models.CharField(max_length=300, db_column='NivelPublico', blank=True)
	class Meta:
		db_table = u'Loans'

	def __unicode__(self):
		try:
			return 'Loan with ' + unicode(self.cooperative) + ((' ('+unicode(self.signing_date)+')') if self.signing_date else '')
		except Cooperative.DoesNotExist:
			return 'Loan ' + unicode(self.id)

	def picture_path(self):
		paths = get_picture_paths('Loans', self.id) or get_picture_paths('Cooperatives', self.cooperative.id)
		return paths['picture']
	picture_path = property(picture_path)

	def thumb_path(self):
		paths = get_picture_paths('Loans', self.id) or get_picture_paths('Cooperatives', self.cooperative.id)
		return paths['thumb']
	thumb_path = property(thumb_path)

	def get_description(self, language_code='EN'):
		return get_translation('Loans', 'Description', self.id, language_code)

	def get_short_description(self, language_code='EN'):
		return get_translation('Loans', 'ShortDescription', self.id, language_code)

class Media(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	date = models.DateTimeField(db_column='Date')
	priority = models.IntegerField(null=True, db_column='Priority', blank=True)
	media_path = models.CharField(max_length=600, db_column='MediaPath')
	context_table = models.CharField(max_length=765, db_column='ContextTable')
	context_id = models.IntegerField(db_column='ContextID')
	member_id = models.IntegerField(db_column='MemberID')
	old_caption = models.TextField(db_column='OldCaption', blank=True)
	description = models.TextField(db_column='Description', blank=True)
	class Meta:
		db_table = u'Media'
	def __unicode__(self):
		return unicode(self.media_path)

class NotaDeAsamblea(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	member_id = models.IntegerField(db_column='MemberID')
	date = models.DateTimeField(db_column='Date')
	note = models.TextField(db_column='Note')
	class Meta:
		db_table = u'NotasDeAsambleas'

class Note(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	member_id = models.IntegerField(db_column='MemberID')
	noted_id = models.IntegerField(db_column='NotedID')
	noted_table = models.CharField(max_length=600, db_column='NotedTable')
	date = models.DateTimeField(db_column='Date')
	note = models.TextField(db_column='Note')
	class Meta:
		db_table = u'Notes'

class Order(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	user_id = models.IntegerField(null=True, db_column='UserID', blank=True)
	transaction_id = models.IntegerField(null=True, db_column='TransactionID', blank=True)
	donation = models.FloatField(null=True, db_column='Donation', blank=True)
	shipping = models.FloatField(null=True, db_column='Shipping', blank=True)
	name = models.CharField(max_length=765, db_column='Name', blank=True)
	shipping_address = models.CharField(max_length=765, db_column='ShippingAddress', blank=True)
	shipping_address2 = models.CharField(max_length=600, db_column='ShippingAddress2', blank=True)
	city = models.CharField(max_length=765, db_column='City', blank=True)
	province = models.CharField(max_length=765, db_column='Province', blank=True)
	country = models.CharField(max_length=765, db_column='Country', blank=True)
	postal_code = models.CharField(max_length=765, db_column='PostalCode', blank=True)
	email_address = models.CharField(max_length=765, db_column='EmailAddress', blank=True)
	date = models.DateTimeField(null=True, db_column='Date', blank=True)
	amazon_fulfilment_request_id = models.CharField(max_length=765, db_column='AmazonFulfilmentRequestID', blank=True)
	class Meta:
		db_table = u'Orders'

class OutflowType(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	scope = models.CharField(max_length=210, db_column='Scope')
	name = models.CharField(unique=True, max_length=150, db_column='Name')
	nombre = models.CharField(max_length=765, db_column='Nombre', blank=True)
	description = models.TextField(db_column='Description')
	from_account = models.CharField(unique=True, max_length=255, db_column='FromAccount', blank=True)
	to_account = models.CharField(unique=True, max_length=255, db_column='ToAccount', blank=True)
	class Meta:
		db_table = u'OutflowTypes'

class ProductSubtypeCategory(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	name = models.CharField(max_length=765, db_column='Name')
	description = models.TextField(db_column='Description', blank=True)
	class Meta:
		db_table = u'ProductSubtypeCategories'

class ProductSubtype(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	subtype_category_id = models.IntegerField(db_column='SubtypeCategoryID')
	consumer_description = models.CharField(max_length=765, db_column='ConsumerDescription')
	consumer_selection_display = models.CharField(max_length=765, db_column='ConsumerSelectionDisplay', blank=True)
	coop_description = models.CharField(max_length=765, db_column='CoopDescription', blank=True)
	display_order = models.FloatField(null=True, db_column='DisplayOrder', blank=True)
	class Meta:
		db_table = u'ProductSubtypes'

class Product(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	product_id = models.CharField(max_length=150, db_column='ProductID')
	identifier_used_by_coop = models.CharField(max_length=765, db_column='IDentifierUsedByCoop', blank=True)
	harmonized_tariff_code = models.CharField(max_length=45, db_column='HarmonizedTariffCode', blank=True)
	name = models.CharField(max_length=600, db_column='Name', blank=True)
	product_category = models.CharField(max_length=300, db_column='ProductCategory')
	sizes_and_colors = models.CharField(max_length=600, db_column='SizesAndColors', blank=True)
	subtype_category_id = models.IntegerField(null=True, db_column='SubtypeCategoryID', blank=True)
	description = models.TextField(db_column='Description', blank=True)
	main_image = models.CharField(max_length=600, db_column='MainImage', blank=True)
	price = models.CharField(max_length=765, db_column='Price', blank=True)
	currency_id = models.IntegerField(null=True, db_column='CurrencyID', blank=True)
	weight = models.FloatField(null=True, db_column='Weight', blank=True)
	length = models.FloatField(null=True, db_column='Length', blank=True)
	width = models.FloatField(null=True, db_column='Width', blank=True)
	height = models.FloatField(null=True, db_column='Height', blank=True)
	special_fund_rate = models.FloatField(null=True, db_column='SpecialFundRate', blank=True)
	special_tax_rate = models.FloatField(null=True, db_column='SpecialTaxRate', blank=True)
	cooperative_id = models.IntegerField(null=True, db_column='CooperativeID', blank=True)
	date_available = models.DateTimeField(db_column='DateAvailable')
	date_withdrawn = models.DateTimeField(null=True, db_column='DateWithdrawn', blank=True)
	display_type = models.CharField(max_length=300, db_column='DisplayType')
	display_order = models.IntegerField(db_column='DisplayOrder')
	amazon_name = models.CharField(max_length=1500, db_column='AmazonName', blank=True)
	amazon_bullet_points = models.CharField(max_length=1515, db_column='AmazonBulletPoints', blank=True)
	amazon_clothing_type = models.CharField(max_length=765, db_column='AmazonClothingType', blank=True)
	amazon_material_fabric = models.CharField(max_length=765, db_column='AmazonMaterialFabric', blank=True)
	amazon_department = models.CharField(max_length=1200, db_column='AmazonDepartment', blank=True)
	amazon_style_keyword = models.CharField(max_length=1200, db_column='AmazonStyleKeyword', blank=True)
	amazon_occasion_lifestyle = models.CharField(max_length=1200, db_column='AmazonOccasionLifestyle', blank=True)
	class Meta:
		db_table = u'Products'

class ProductOrdered(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	product_subtype = models.IntegerField(db_column='ProductSubtype')
	product_id = models.CharField(max_length=765, db_column='ProductID', blank=True)
	order_id = models.IntegerField(null=True, db_column='OrderID', blank=True)
	shipment_id = models.IntegerField(null=True, db_column='ShipmentID', blank=True)
	price = models.FloatField(null=True, db_column='Price', blank=True)
	quantity = models.IntegerField(null=True, db_column='Quantity', blank=True)
	size = models.CharField(max_length=765, db_column='Size', blank=True)
	color = models.CharField(max_length=765, db_column='Color', blank=True)
	characteristics = models.CharField(max_length=765, db_column='Characteristics', blank=True)
	fund_donation = models.FloatField(null=True, db_column='FundDonation', blank=True)
	taxes = models.FloatField(null=True, db_column='Taxes', blank=True)
	date_coop_given_order = models.DateTimeField(null=True, db_column='DateCoopGivenOrder', blank=True)
	date_coop_paid = models.DateTimeField(null=True, db_column='DateCoopPaid', blank=True)
	date_taxes_paid = models.DateTimeField(null=True, db_column='DateTaxesPaid', blank=True)
	credit_transaction_cost = models.FloatField(null=True, db_column='CreditTransactionCost', blank=True)
	class Meta:
		db_table = u'ProductsOrdered'

class ProjectEvent(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	member_id = models.IntegerField(db_column='MemberID')
	project_id = models.IntegerField(db_column='ProjectID')
	project_table = models.CharField(max_length=765, db_column='ProjectTable')
	summary = models.CharField(max_length=765, db_column='Summary')
	details = models.TextField(db_column='Details', blank=True)
	date = models.DateTimeField(db_column='Date')
	finalized = models.IntegerField(db_column='Finalized')
	completed = models.DateField(null=True, db_column='Completed', blank=True)
	modified_date = models.DateTimeField(db_column='ModifiedDate')
	type = models.CharField(max_length=105, db_column='Type')
	class Meta:
		db_table = u'ProjectEvents'

class ProjectLog(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	member_id = models.IntegerField(db_column='MemberID')
	project_id = models.IntegerField(db_column='ProjectID')
	project_table = models.CharField(max_length=765, db_column='ProjectTable')
	paso_id = models.IntegerField(null=True, db_column='PasoID', blank=True)
	date = models.DateTimeField(db_column='Date')
	progress = models.CharField(max_length=90, db_column='Progress')
	explanation = models.CharField(max_length=765, db_column='Explanation', blank=True)
	detailed_explanation = models.TextField(db_column='DetailedExplanation', blank=True)
	notas_privadas = models.TextField(db_column='NotasPrivadas', blank=True)
	additional_notes = models.TextField(db_column='AdditionalNotes', blank=True)
	class Meta:
		db_table = u'ProjectLogs'

class Repayment(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	loan_id = models.IntegerField(db_column='LoanID')
	date_due = models.DateTimeField(db_column='DateDue')
	date_paid = models.DateTimeField(null=True, db_column='DatePaid', blank=True)
	amount_due = models.IntegerField(db_column='AmountDue')
	amount_paid = models.IntegerField(null=True, db_column='AmountPaid', blank=True)
	interest_since_last_payment = models.IntegerField(null=True, db_column='InterestSinceLastPayment', blank=True)
	date_refinanced = models.DateField(null=True, db_column='DateRefinanced', blank=True)
	class Meta:
		db_table = u'Repayments'

class Shipment(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	order_id = models.IntegerField(unique=True, db_column='OrderID')
	tracking_number = models.CharField(unique=True, max_length=255, db_column='TrackingNumber', blank=True)
	carrier = models.CharField(max_length=300, db_column='Carrier', blank=True)
	date_tracking_number_entered = models.DateTimeField(null=True, db_column='DateTrackingNumberEntered', blank=True)
	shipment_date = models.DateField(null=True, db_column='ShipmentDate', blank=True)
	cost = models.FloatField(null=True, db_column='Cost', blank=True)
	notes = models.TextField(db_column='Notes', blank=True)
	class Meta:
		db_table = u'Shipments'

class ShippingAddress(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	user_id = models.IntegerField(null=True, db_column='UserID', blank=True)
	default_address = models.IntegerField(null=True, db_column='DefaultAddress', blank=True)
	name = models.CharField(max_length=765, db_column='Name', blank=True)
	street1 = models.CharField(max_length=765, db_column='Street1', blank=True)
	street2 = models.CharField(max_length=765, db_column='Street2', blank=True)
	city = models.CharField(max_length=765, db_column='City', blank=True)
	province = models.CharField(max_length=765, db_column='Province', blank=True)
	country = models.CharField(max_length=765, db_column='Country', blank=True)
	postal_code = models.CharField(max_length=765, db_column='PostalCode', blank=True)
	class Meta:
		db_table = u'ShippingAddresses'

class StoreTransaction(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	response = models.CharField(max_length=765, db_column='Response', blank=True)
	error_message = models.CharField(max_length=765, db_column='ErrorMessage', blank=True)
	user_id = models.IntegerField(null=True, db_column='UserID', blank=True)
	account_number = models.CharField(max_length=765, db_column='AccountNumber', blank=True)
	exp_month = models.CharField(max_length=765, db_column='ExpMonth', blank=True)
	exp_year = models.CharField(max_length=765, db_column='ExpYear', blank=True)
	cvv2 = models.CharField(max_length=15, db_column='CVV2', blank=True)
	name = models.CharField(max_length=765, db_column='Name', blank=True)
	billing_address = models.CharField(max_length=765, db_column='BillingAddress', blank=True)
	postal_code = models.CharField(max_length=765, db_column='PostalCode', blank=True)
	country = models.CharField(max_length=765, db_column='Country', blank=True)
	amount = models.FloatField(null=True, db_column='Amount', blank=True)
	date = models.DateTimeField(null=True, db_column='Date', blank=True)
	class Meta:
		db_table = u'StoreTransactions'

class StoreUserCreditCard(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	user_id = models.IntegerField(null=True, db_column='UserID', blank=True)
	default_card = models.IntegerField(null=True, db_column='DefaultCard', blank=True)
	first_name = models.CharField(max_length=765, db_column='FirstName', blank=True)
	last_name = models.CharField(max_length=765, db_column='LastName', blank=True)
	type = models.CharField(max_length=765, db_column='Type', blank=True)
	account_number = models.CharField(max_length=765, db_column='AccountNumber', blank=True)
	exp_month = models.CharField(max_length=765, db_column='ExpMonth', blank=True)
	exp_year = models.CharField(max_length=765, db_column='ExpYear', blank=True)
	cvv2 = models.CharField(max_length=765, db_column='CVV2', blank=True)
	street1 = models.CharField(max_length=765, db_column='Street1', blank=True)
	street2 = models.CharField(max_length=765, db_column='Street2', blank=True)
	city = models.CharField(max_length=765, db_column='City', blank=True)
	province = models.CharField(max_length=765, db_column='Province', blank=True)
	country = models.CharField(max_length=765, db_column='Country', blank=True)
	postal_code = models.CharField(max_length=765, db_column='PostalCode', blank=True)
	class Meta:
		db_table = u'StoreUserCreditCards'

class StoreUserLog(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	date = models.DateTimeField(db_column='Date')
	tracking_id = models.CharField(max_length=60, db_column='TrackingID')
	user_email = models.CharField(max_length=150, db_column='UserEmail', blank=True)
	url = models.CharField(max_length=600, db_column='URL')
	query = models.CharField(max_length=765, db_column='Query')
	class Meta:
		db_table = u'StoreUserLog'

class StoreUser(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	email = models.CharField(unique=True, max_length=255, db_column='Email', blank=True)
	password = models.CharField(max_length=765, db_column='Password', blank=True)
	crypt = models.CharField(max_length=765, db_column='Crypt', blank=True)
	start_date = models.DateTimeField(null=True, db_column='StartDate', blank=True)
	class Meta:
		db_table = u'StoreUsers'

class TransactionType(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	scope = models.CharField(max_length=210, db_column='Scope')
	name = models.CharField(unique=True, max_length=150, db_column='Name')
	nombre = models.CharField(max_length=765, db_column='Nombre', blank=True)
	description = models.TextField(db_column='Description')
	from_account = models.CharField(unique=True, max_length=255, db_column='FromAccount', blank=True)
	to_account = models.CharField(unique=True, max_length=255, db_column='ToAccount', blank=True)
	class Meta:
		db_table = u'TransactionTypes'

class Transaction(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	group_transaction_id = models.IntegerField(null=True, db_column='GroupTransactionID', blank=True)
	account = models.IntegerField(db_column='Account')
	member_id = models.IntegerField(null=True, db_column='MemberID', blank=True)
	loan = models.IntegerField(null=True, db_column='Loan', blank=True)
	check_id = models.IntegerField(null=True, db_column='CheckID', blank=True)
	transaction_type = models.IntegerField(null=True, db_column='TransactionType', blank=True)
	inflow_type = models.IntegerField(null=True, db_column='InflowType', blank=True)
	outflow_type = models.IntegerField(null=True, db_column='OutflowType', blank=True)
	description = models.TextField(db_column='Description')
	tipo_de_documento = models.CharField(max_length=765, db_column='TipoDeDocumento', blank=True)
	numero_de_documento = models.CharField(max_length=765, db_column='NumeroDeDocumento', blank=True)
	details = models.TextField(db_column='Details', blank=True)
	filtrado_por_sistema_eleo = models.IntegerField(db_column='FiltradoPorSistemaEleo')
	solamente_en_sistema_eleo = models.IntegerField(db_column='SolamenteEnSistemaEleo')
	date_accrual = models.DateField(null=True, db_column='DateAccrual', blank=True)
	date_cash = models.DateField(null=True, db_column='DateCash', blank=True)
	formula = models.CharField(max_length=765, db_column='Formula', blank=True)
	amount = models.FloatField(db_column='Amount')
	amount_fixed = models.FloatField(null=True, db_column='AmountFixed', blank=True)
	credit = models.FloatField(null=True, db_column='Credit', blank=True)
	debit = models.FloatField(null=True, db_column='Debit', blank=True)
	class Meta:
		db_table = u'Transactions'

class TransactionHold(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	account = models.IntegerField(db_column='Account')
	income_type = models.IntegerField(null=True, db_column='IncomeType', blank=True)
	expenditure_type = models.IntegerField(null=True, db_column='ExpenditureType', blank=True)
	description = models.TextField(db_column='Description')
	date = models.DateField(null=True, db_column='Date', blank=True)
	formula = models.CharField(max_length=765, db_column='Formula', blank=True)
	amount = models.IntegerField(null=True, db_column='Amount', blank=True)
	class Meta:
		db_table = u'TransactionsHold'

class VendorOrder(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	date_requested = models.DateTimeField(null=True, db_column='DateRequested', blank=True)
	date_received = models.DateTimeField(null=True, db_column='DateReceived', blank=True)
	product_id = models.CharField(max_length=300, db_column='ProductID')
	product_subtype = models.IntegerField(db_column='ProductSubtype')
	transaction_id = models.IntegerField(null=True, db_column='TransactionID', blank=True)
	quantity = models.IntegerField(db_column='Quantity')
	price = models.FloatField(db_column='Price')
	notes = models.TextField(db_column='Notes', blank=True)
	class Meta:
		db_table = u'VendorOrders'

class WorkChangeLog(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	work_log_id = models.IntegerField(db_column='WorkLogID')
	member_id = models.IntegerField(db_column='MemberID')
	start_time = models.DateTimeField(null=True, db_column='StartTime', blank=True)
	end_time = models.DateTimeField(null=True, db_column='EndTime', blank=True)
	client = models.CharField(max_length=765, db_column='Client', blank=True)
	modified_time = models.DateTimeField(db_column='ModifiedTime')
	class Meta:
		db_table = u'WorkChangeLog'

class WorkLog(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	member_id = models.IntegerField(db_column='MemberID')
	start_time = models.DateTimeField(db_column='StartTime')
	end_time = models.DateTimeField(null=True, db_column='EndTime', blank=True)
	start_client = models.CharField(max_length=765, db_column='StartClient', blank=True)
	end_client = models.CharField(max_length=765, db_column='EndClient', blank=True)
	activity_type = models.CharField(max_length=300, db_column='ActivityType', blank=True)
	project_id = models.IntegerField(null=True, db_column='ProjectID', blank=True)
	paso_id = models.IntegerField(null=True, db_column='PasoID', blank=True)
	activity_category = models.CharField(max_length=765, db_column='ActivityCategory', blank=True)
	activity_description = models.TextField(db_column='ActivityDescription', blank=True)
	class Meta:
		db_table = u'WorkLog'

class WorkerVacation(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	member_id = models.IntegerField(db_column='MemberID')
	start_date = models.DateField(db_column='StartDate')
	end_date = models.DateField(db_column='EndDate')
	class Meta:
		db_table = u'WorkerVacation'

class Mailinglist(models.Model):
	id = models.AutoField(primary_key=True)
	firstname = models.CharField(max_length=600)
	lastname = models.CharField(max_length=600)
	email = models.CharField(max_length=600)
	startdate = models.DateTimeField()
	class Meta:
		db_table = u'mailinglist'

class Test(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	test = models.CharField(max_length=765, db_column='Test')
	thedate = models.DateTimeField(null=True, blank=True)
	class Meta:
		db_table = u'test'

class Todo(models.Model):
	id = models.AutoField(primary_key=True, db_column='ID')
	priority = models.IntegerField(db_column='Priority')
	status = models.CharField(max_length=90, db_column='STATUS')
	point_person = models.ForeignKey(Member, null=True, db_column='PointPerson', blank=True)
	second = models.ForeignKey(Member, related_name='todo_second', null=True, db_column='Second', blank=True)
	modified = models.DateField(db_column='Modified')
	description = models.TextField(db_column='Description')
	class Meta:
		db_table = u'todo'
	def __unicode__(self):
		return unicode(self.description)


class UserAccount(models.Model):
	user = models.OneToOneField(User)
	balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
	loans = models.ManyToManyField(Loan, through='UserLoanContribution')

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return unicode(self.user.username)

class UserLoanContribution(models.Model):
	user = models.ForeignKey(UserAccount)
	loan = models.ForeignKey(Loan)
	amount = models.DecimalField(max_digits=12, decimal_places=2)
	balance = models.DecimalField(max_digits=12, decimal_places=2)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

# class UserLoanPayment(models.Model):
# 	contribution = models.ForeignKey(UserLoanContribution)
# 	amount = models.DecimalField(max_digits=12, decimal_places=2)
# 	timestamp = models.DateTimeField(auto_now_add=True)


## Functions ##

import re

def get_picture_paths(table_name, id):
	try:
		image = Media.objects.filter(context_table=table_name, context_id=id).order_by('priority','media_path')[0]
	except IndexError:
		return
	# insert ".thumb" into image path
	thumb_path = re.sub(r'(\.[^.]+)$', r'.thumb\1', image.media_path)
	return {'picture':image.media_path, 'thumb':thumb_path}

# def get_thumb_path(table_name, id):
# 	images = Media.objects.filter(context_table=table_name, context_id=id).order_by('-priority','media_path')
# 	if images:
# 		# insert ".thumb" into image path
# 		thumb_path = re.sub(r'(\.[^.]+)$', r'.thumb\1', images[0].media_path)
# 		return thumb_path

def get_translation(table_name, column_name, id, language_code='EN'):
	translations = Translation.objects.filter(remote_table=table_name, remote_id=id, remote_column_name=column_name)
	try:
		content = translations.get(language__code=language_code).translated_content
	except Translation.DoesNotExist:
		content = translations.order_by('language__priority')[0].translated_content
	return content

def first_or_none(some_list):
	try:
		some_list[0]
	except IndexError:
		pass
