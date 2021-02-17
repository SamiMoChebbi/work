class mymodule::myklass {
  file {
    'my_bash_script':
      ensure => 'file',
      source => 'puppet:///modules/mymodule/my_bash_script.sh',
      path => '/usr/local/bin/my_bash_script.sh',
      owner => 'root'
      group => 'root'
      mode  => '0744', # Use 0700 if it is sensitive
      notify => Exec['run_my_script'],
  }
  exec {
    'run_my_script':
     command => '/usr/local/bin/my_bash_script.sh',
     refreshonly => true,
  }
}
