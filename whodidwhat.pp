class hg_box::monitor{
  

  #whodidwhat Scripts
  file {'/usr/local/sbin/whodidwhat':
      ensure  => 'present'
      owner   => 'root',
      mode    => '755', 
      source  => 'puppet:///modules/hg_box/monitor/cbox-op-scripts/whodidwhat.sh',

  }

  file {'/etc/profilze.d/whodidwhat_profile.sh':
      ensure  => 'present'
      owner   => 'root',
      mode    => '755', 
      source  => 'puppet:///modules/hg_box/monitor/cbox-op-scripts/whodidwhat.profile.sh',

  }
