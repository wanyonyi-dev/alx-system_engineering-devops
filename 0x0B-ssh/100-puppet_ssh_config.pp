#!/usr/bin/env puppet

# Script to update the ssh_config file to allow signing in without using a password
# and using ~/ssh/school as the private key

file { 'config_file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => ' IdentityFile ~/ssh/school',
}

file { 'password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '   asswordAuthentication no',
}
