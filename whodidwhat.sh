#!/usr/bin/bash


tail -n +1 ~/.bash_history_* | awk '
/==>/{
    split($2,a,"_")
    user=a[length(a)]
    next
}

/#[0-9]+/{
    printf "%s", strftime("%Y-%m-%d %H:%M:%S", substr($1, 2, length($1)))
}

!/#[0-9]+/{
    print " "user," ", $0
}
' | sort
