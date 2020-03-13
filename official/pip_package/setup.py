# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Sets up TensorFlow Official Models."""
import datetime
import sys

from setuptools import find_packages
from setuptools import setup

version = '2.1.0.dev2'

project_name = 'tf-models-official'

if '--project_name' in sys.argv:
  project_name_idx = sys.argv.index('--project_name')
  project_name = sys.argv[project_name_idx + 1]
  sys.argv.remove('--project_name')
  sys.argv.pop(project_name_idx)

if project_name == 'tf-models-nightly':
  version += '.' + datetime.datetime.now().strftime('%Y%m%d%H%M')

setup(
    name=project_name,
    version=version,
    description='TensorFlow Official Models',
    author='Google Inc.',
    author_email='no-reply@google.com',
    url='https://github.com/tensorflow/models',
    license='Apache 2.0',
    packages=find_packages(exclude=[
        'research*',
        'tutorials*',
        'samples*',
        'official.r1*',
        'official.pip_package*',
        'official.benchmark*',
    ]),
    exclude_package_data={
        '': ['*_test.py',],
    },
    install_requires=[
        'six',
    ],
    extras_require={
        'tensorflow': ['tensorflow>=2.0.0'],
        'tensorflow_gpu': ['tensorflow-gpu>=2.0.0'],
        'tensorflow-hub': ['tensorflow-hub>=0.6.0'],
    },
    python_requires='>=3.6',
)
