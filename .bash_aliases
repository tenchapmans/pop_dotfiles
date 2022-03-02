## aliases for ls to lsd
alias ls='lsd'
alias l='ls -lh'
alias la='ls -ah'
alias ll='ls -lah'
alias lt='ls --tree'

## aliases for common config files that I edit. 
alias ealias='lvim ~/.bash_aliases'
alias ebash='lvim ~/.bashrc'
alias estarship='lvim ~/.config/starship.toml'
alias sbash='source ~/.bashrc'

## aliases for git
alias gcl='git clone --recurse '
alias gcm='git commit -m ""'

## system stuff
alias upd='sudo apt update && sudp apt upgrade'


## Misc aliases
alias man='tldr'
alias cat='bat'

alias bsrc='source ~/.bashrc'
alias aghome='sshfs acchapm1@agave.asu.edu:/home/acchapm1 /home/acchapm1/sshfs/agave/home && cd /home/acchapm1/sshfs/agave/home'
alias agscratch='sshfs acchapm1@agave.asu.edu:/scratch/acchapm1 /home/acchapm1/sshfs/agave/scratch && cd /home/acchapm1/sshfs/agave/scratch'
alias py='python3'
alias condaa='conda activate '
alias condad='conda deactivate'

alias splinter='ssh acchapm1@splinter.asu.edu -p 396'
alias agave='ssh acchapm1@agave.asu.edu'
alias py='python3'

alias kt='py ~/.config/kitty/kittytheme.py'
alias ktt='py ~/.config/kitty/kittytheme.py -t -L'
