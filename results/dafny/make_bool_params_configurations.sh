#!/bin/sh

namespace=""

z3 -p |
    while read -r line
    do
        if [[ "$line" =~ ^\[module\]\ ([^\s,]+).*$ ]]
        then
            namespace="${BASH_REMATCH[1]}"
        elif [[ "$line" =~ ^\s*(.+)\ \(bool\)\ \(default:\ (true|false)\)\s*$ ]]
        then
            param_name="${BASH_REMATCH[1]}"
            default_value="${BASH_REMATCH[2]}"
            if [ "$default_value" = "true" ]
            then
                opposite_value="false"
            else
                opposite_value="true"
            fi
            if [[ "$namespace" = "" ]]
            then
                echo "      \"/proverOpt:O:$param_name=$opposite_value\","
            else
                echo "      \"/proverOpt:O:$namespace.$param_name=$opposite_value\","
            fi
        fi
    done
    
