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

from bson.json_util import loads
from mongows.validators.ValidationTest import ValidationTest, get_file_in_dir


class ValidationTestCase(ValidationTest):
    def run(self):
        path = get_file_in_dir(__file__, 'images_done.json')
        with open(path) as reference_file:
            reference = loads(reference_file.read())
            collections_equal = self.collection_equals('images', reference, True)
            return 'pass' if collections_equal else 'fail'
