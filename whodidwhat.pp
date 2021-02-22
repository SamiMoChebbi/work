class hg_box::monitor{
  

  #whodidwhat Scripts
  file {'cernbox/ops':
      ensure => 'file',
      owner => 'root',
      mode  => '755', 
      recurse => true,
      source => 'puppet:///modules/hg_box/monitor/whodidwhat',
