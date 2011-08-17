# Copyright 2010-2011, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

{
  'targets': [
    {
      'target_name': 'system_dictionary',
      'type': 'static_library',
      'sources': [
        'system_dictionary.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../file/dictionary_file.gyp:dictionary_file',
        '<(DEPTH)/third_party/rx/rx.gyp:rx',
      ],
    },
    {
      'target_name': 'system_dictionary_builder',
      'type': 'static_library',
      'sources': [
        'system_dictionary_builder.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../dictionary_base.gyp:text_dictionary_loader',
        '../file/dictionary_file.gyp:dictionary_file_builder',
        '<(DEPTH)/third_party/rx/rx.gyp:rx',
        'system_dictionary',
      ],
    },
    {
      'target_name': 'system_dictionary_test',
      'type': 'executable',
      'sources': [
        'system_dictionary_test.cc',
      ],
      'dependencies': [
        'system_dictionary',
        'system_dictionary_builder',
        '../../base/base.gyp:base',
        '../../testing/testing.gyp:gtest_main',
      ],
      'variables': {
        'test_size': 'small',
      },
    },
    {
      'target_name': 'system_dictionary_builder_test',
      'type': 'executable',
      'sources': [
        'system_dictionary_builder_test.cc',
      ],
      'dependencies': [
        'system_dictionary_builder',
        '../../base/base.gyp:base',
        '../../testing/testing.gyp:gtest_main',
      ],
      'variables': {
        'test_size': 'small',
      },
    },
  ],
}