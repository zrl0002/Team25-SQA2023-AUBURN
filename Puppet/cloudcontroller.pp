class { 'openstack::controller':
  public_address       => $::ipaddress_eth0,
  mysql_root_password  => 'password',
  allowed_hosts        => ['127.0.0.%', '192.168.1.%'],
  rabbit_password      => 'password',
  keystone_db_password => 'password',
  keystone_admin_token => '12345',
  admin_email          => 'root@localhost',
  admin_password       => 'password',
  nova_db_password     => 'password',
  nova_user_password   => 'password',
  glance_db_password   => 'password',
  glance_user_password => 'password',
  secret_key           => '12345',
}
