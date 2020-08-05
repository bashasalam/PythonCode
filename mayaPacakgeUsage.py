print("Assalaamu alaikkum to all")
import maya

now = maya.now()
print(now)
tomorrow = maya.when('tomorrow')
print(tomorrow)

print(tomorrow.slang_date())
print()
print(tomorrow.slang_time())
print()
print(tomorrow.rfc3339())
print()
print(tomorrow.rfc2822())
print()
print(tomorrow.iso8601())
print()
print(tomorrow.datetime())