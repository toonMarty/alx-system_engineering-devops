file_line {'Identity_file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'Identity_file ~/.ssh/school',
}
file_line {'disable password login':
  path => '/etc/ssh/ssh_config',
  line => ' PasswordAuthentication no'
}
