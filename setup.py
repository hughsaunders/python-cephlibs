from setuptools import setup

setup(
    name='python-cephlibs',
    version='0.94.5-1',
    description='Python bindings for rados and rbd client libraries.',
    long_description=(
        'This package provides the rados and rbd python bindings for '
        'libraries used to connect to an existing ceph cluster. '
        'This package does not include the underlying C libraries which must '
        ' be installed separately. See http://ceph.com'),
    url='http://github.com/hughsaunders/python-cephlibs',
    author='Sage Weil & Team https://github.com/ceph/ceph/graphs/contributors',
    author_email='ceph-devel@vger.kernel.org',
    license='LGPL',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
    ],
    keywords='ceph storage',
    py_modules=['rados', 'rbd', 'cephfs', 'ceph_rest_api', 'ceph_argparse'],
    install_requires=[],

)
