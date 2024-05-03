#!/usr/bin/pup
# file to install flask verion 2.1.0 using pip3
# 

package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  }
