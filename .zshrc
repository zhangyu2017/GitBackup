alias xterm='xterm -fn  -adobe-courier-medium-r-normal--14-140-75-75-m-90-iso8859-1  &'
alias bjoball='bjobs -u all'
path=(`echo $path | /bin/sed 's/ \.//'`)

stty sane
ignoreeof=2
#export ROOT_LEVEL=5.18.00
#    setenv ROOT_LEVEL 5.14.00
export CERN_LEVEL=2005
export MALLOC_CHECK_=0
export filec
export autolist
export nobeep
export MALLOC_CHECK_
export PBS_HOME=/opt/torque
path=($path /opt/torque/bin /opt/torque/sbin /opt/maui/sbin ~/.local/bin)
MANPATH="$HOME/.local/share/man:$MANPATH"

alias qsub="qsub -S /bin/tcsh "

#define software version
#if [ -z "$ROOT_LEVEL" ]; then
#   export ROOT_LEVEL=5.26.00
    export ROOT_LEVEL=v5-34-05
#fi
if [ -z "$CERN_LEVEL" ]; then
   export CERN_LEVEL=2005
fi

#define library path
if [ -z "$LD_LIBRARY_PATH" ]; then 
   export LD_LIBRARY_PATH=/lib64:/usr/lib64/:/usr/local/lib64
   if [ -d /lib64 ]; then
      export  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/lib64
   fi
   if [ -d /usr/lib64 ]; then
      export  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64
   fi
fi


#Setting for root
export ROOTSYS=/softwares/common/soft/root/x86_64_sl4/$ROOT_LEVEL
export PATH=$ROOTSYS/bin:$PATH
export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH

#Setting for cernlib
export CERN=/softwares/common/soft/cernlib/x86_64_sl4/
export CERN_ROOT=/softwares/common/soft/cernlib/x86_64_sl4/$CERN_LEVEL
export PATH=$CERN_ROOT/bin:$PATH
export LD_LIBRARY_PATH=$CERN_ROOT/lib:$LD_LIBRARY_PATH

#setting for sge
if [ -e /home/sge ]; then
   export SGE_ROOT=/home/sge
   export SGE_CELL=iopp
   source $SGE_ROOT/$SGE_CELL/common/settings.sh
   alias qstatall="qstat -u '*'"
fi

curdir=`pwd`
cd /softwares/common/soft/root/x86_64_sl4/v5-34-05
source bin/thisroot.sh
cd $curdir

#if tty -s
#then
#   echo "=========Environment variables==========="
#   echo "  ROOT_LEVEL = $ROOT_LEVEL"
#   echo "  CERN_LEVEL = $CERN_LEVEL"
#   echo "  ROOTSYSY   = $ROOTSYS"
#   echo "  CERN_ROOT  = $CERN_ROOT"
#   echo "========================================="
#fi
# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
export SHELL=/bin/zsh
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac
if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	color_prompt=yes
    else
	color_prompt=
    fi
fi

autoload -Uz colors && colors
if [ $UID -eq 0 ]; then
        PROMPT='%~ # '
else
        PROMPT='%{[01;36m%}∂ %{[01;34m%}%~%{[00m%} '
fi

DIRSTACKSIZE=10
setopt autocd
setopt AUTO_PUSHD
setopt PUSHD_IGNORE_DUPS
zstyle :compinstall filename '~/.zshrc'

autoload -Uz compinit
compinit


# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.

# User configuration

# export PATH="/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/dsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

#source /usr/share/autojump/autojump.zsh
autoload -U compinit && compinit -u
alias ls='ls --color'
alias l='ls -l --color'
alias ff='gfortran'
alias gvim='gvim -p --remote-tab'
alias gvi='vim -g'
alias rr='root.exe -q -l -b'
alias re='root.exe -l -b'
alias pyr='PYTHONSTARTUP=~/.devtools/pyre.py python'
alias py='python2'
alias python='/softwares/python_2.7.8/bin/python2'
alias .q='exit'
alias ..='cd ..'
alias wqstat='watch -n1 "qstat|tail -n 30"'
alias qless='qstat|less'
alias qaless="qstat -u '*' | less"

alias -s c='vim'
alias -s cxx='vim'
alias -s cc='vim'
alias -s cpp='vim'
alias -s h='vim'
alias -s f='vim'
alias -s txt='vim'

export sdir=/DATA/data01/u/star
export dhs=/DATA/data02/heshu
export d01=/DATA/data01
export d02=/DATA/data02
