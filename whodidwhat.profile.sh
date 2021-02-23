export LOGDINUSER=`klist | grep "Default principal" | awk '{print $3}' | sed 's/@CERN.CH//'`
export HISTTIMEFORMAT="@ %m/%d/%Y %H:%M "
export HISTFILE=~/.bash_history_$LOGDINUSER
