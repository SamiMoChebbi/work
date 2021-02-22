#!/usr/bin/awk -f

/#[0-9]+/{
    printf "%s", strftime("%Y-%m-%d %H:%M:%S", substr($1, 2, length($1)))
}

!/#[0-9]+/{
    print " ", $1
}
