# Executing kill command in Puppet using pkill
exec {'killmenow':
  path    => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
  command => 'pkill -SIGTERM -f ./killmenow'
}
