from setuptools import setup
setup(name='json-merge-patch',
      version='0.2',
      description='JSON Merge Patch library (https://tools.ietf.org/html/rfc7386)',
      author='David Raznick',
      author_email='mr.raznick@gmail.com',
      scripts=['json-merge-patch'],
      license='BSD',
      packages=['json_merge_patch'],
      include_package_data=True,
      url='https://github.com/open-contracting/json-merge-patch'
)
