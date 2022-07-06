from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
  # The fields to be used in displaying the User model.
  # These override the definitions on the base UserModelAdmin
  # that reference specific fields on auth.User.
  list_display = ('id', 'email','phone', 'name', 'DOB','Gender','RegdNo','YearOfAdmission','medicalCouncil','photo','signature','regdCertificate', 'is_admin')
  list_filter = ('is_admin',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('phone','name', 'DOB','Gender','RegdNo','YearOfAdmission','medicalCouncil','photo','signature','regdCertificate',)}),
      ('Permissions', {'fields': ('is_admin',)}),
  )
  # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email','phone', 'name', 'DOB','Gender','RegdNo','YearOfAdmission','medicalCouncil','photo','signature','regdCertificate', 'password1', 'password2'),
      }),
  )
  search_fields = ('phone',)
  ordering = ('email', 'id')
  filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)