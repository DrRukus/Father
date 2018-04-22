#!/bin/bash

for file in ~/.{path,bash_prompt,aliases}; do
    [ -r "$file" ] && [ -f "$file" ] && source "$file";
done
unset file;

# added by Anaconda2 5.0.0 installer
export PATH="/Users/dschmidt2/anaconda2/bin:$PATH"
export PATH=$PATH:"/usr/local/bin"

export PATH="$HOME/.cargo/bin:$PATH"
