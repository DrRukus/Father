#!/bin/bash
# Set values of vars
no='No'
yes='Yes'

echo 'Enter 1 to set ENVVAR to yes, 2 for no.'
read setting
re='^[0-9]+$'
if ! [[ $setting =~ $re ]] ; then
    echo 'Error: not a number!!' >&2 ; exit 1
    ENVVAR='Unknown'
else
    if [[ $setting -eq 2 ]] ; then
        echo "\$ENVVAR will be set to $no"
        ENVVAR=$no
    elif [[ $setting -eq 1 ]] ; then
        echo "\$ENVVAR will be set to $yes"
        ENVVAR=$yes
    else
        echo 'Invalid entry.  Must be either 1 or 2'
    fi
fi
export ENVVAR

