## to install
install newsbeuter

mv dot.newsbeuter to ~/.newsbeuter

append awesomebeuter script to the end of bashrc

## to use
you can set your own custom stuff by adding an alias to awesome beuters and creating a theme file in themes folder

alias (programname)='nb-term-search "(url identifier)" "(themefile)"'

#Example:
alias newsbeuter-youtube='nb-term-search "YouTube" "youtube.theme"'

http://rss.for.youtube/videos.rss "YouTube"
this url will be picked up by newsbeuter-youtube and displayed with youtube.theme



## Optional
download my urlhandler script to launch urls in your own programs

## Important
the cleanup cache config option set to no is mandatory for this to work
without it set newsbeuter will delete all the cache items when your urls change
