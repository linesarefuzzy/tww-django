from django_evolution.mutations import ChangeField


MUTATIONS = [
    ChangeField('UserAccount', 'modified', initial=0, null=False),
    ChangeField('UserAccount', 'created', initial=0, null=False)
]
