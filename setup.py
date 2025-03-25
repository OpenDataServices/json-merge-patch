from setuptools import setup
setup(name='json-merge-patch',
      version='0.3.0',
      description='JSON Merge Patch library (https://tools.ietf.org/html/rfc7386)',
      author='Open Data Services',
      author_email='code@opendataservices.coop',
      scripts=['json-merge-patch'],
      license='BSD',
      packages=['json_merge_patch'],
      include_package_data=True,
      python_requires=">=3.9",
      url='https://github.com/open-contracting/json-merge-patch'
)
