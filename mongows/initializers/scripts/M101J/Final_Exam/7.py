#    Copyright 2013 10gen Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from mongows.initializers.util import load_data_from_mongodump
from mongows.validators.ValidationTest import get_file_in_dir


def run(res_id):
    path = get_file_in_dir(__file__, 'albums.bson')
    load_data_from_mongodump(res_id, path, 'albums',)

    path = get_file_in_dir(__file__, 'images_init.bson')
    load_data_from_mongodump(res_id, path, 'images',)
