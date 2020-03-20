### Setting up user groups for celery workers

The celery-worker group is added in users/fixtures/user_groups.json. The workers need to 
be added to this group to obtain the necessary permissions.

```
python3 manage.py loaddata user_groups
```

New workers can be added as shown in the fixture. 
The password has to be generated as a hash. To generate
a password hash use the build in function and paste it into the fixture.

```
python3 manage.py shell
>>> from django.contrib.auth.hashers import make_password
>>> make_password('test')
'pbkdf2_sha256$10000$vkRy7QauoLLj$ry+3xm3YX+YrSXbri8s3EcXDIrx5ceM+xQjtpLdw2oE='
```

Password 'X6IxEcfpXrTjCjD6HtFswNC43unfqNAudWTNDvNLTSY='
Hash:'pbkdf2_sha256$180000$W989vEV5QzFx$r0zdLN7PagfdnGV0X6y/Ou89o39pOkqqb0c2a69AXLc=' 
```
PIPENV_VENV_IN_PROJECT=1 pipenv run python3 manage.py shell
>>> from django.contrib.auth.models import Group, User
>>> user = User.objects.get(usernamee="krupke")
>>> group = Group.objects.get(name="celery-workers")
>>> user.groups.add(group)
```