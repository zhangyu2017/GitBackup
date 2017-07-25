map <F4> :call TitleDet2() <cr>'s
function AddTitle2()
	call append(0,"/*******************************************************************************")
	call append(1,"    Author        : Yu Zhang")
	call append(2,"    Email         : zhang_yu@mails.ccnu.edu.cn")
	call append(3,"    Last modified : ".strftime("%Y-%m-%d %H:%M"))
	call append(4,"    Filename      : ".expand("%:t"))
	call append(5,"    Description   : Don't be so hard")
	call append(6,"******************************************************************************/")
	echohl WarningMsg | echo "Successful in adding the copyrght ." | echohl None
endfunction

function UpdateTitle2()
	normal m'
	execute '/# *Last modified:/s@\=strftime(":\t%Y-%m-%d %H:%M")@'
	normal ''
	execute mk
	execute '/# *Filename:/s@:.*$@\=":\t\t".expand("%:t")@'
	normal 'k
	echohl WarningMsg | echo "Successful in updating the copyright ." | echohl None
endfunction
function TitleDet2()
	let n=1
	while n<7
		let line=getline(n)
		if line=~'\#\s*\S*Last\smodified:\s*.*$'
			call UpdateTitle2()
			return
		endif
		let n=n+1
	endwhile
	call AddTitle2()
endfunction


set nu
syntax on
set autoindent
set cindent
set shiftwidth=4
set softtabstop=5
set tabstop=4
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Raimondi/delimitMate'
call vundle#end()
let delimitMate_expand_cr = 1
filetype plugin indent on
set backspace=indent,eol,start
set ls=2
set hls
set nocompatible
set cursorline
hi CursorLine cterm=NONE ctermbg=green  ctermfg=black  guibg=white
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
if has("autocmd")
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif
hi CursorColumn cterm=NONE ctermbg=green  ctermfg=black guibg=white
