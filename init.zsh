startup_timer_module_path="$0:a:h"

print_startup_time () {
  print -n "Startup time: "
  python "$startup_timer_module_path/startup_timer.py" 2>/dev/null
  (( $status )) && print -n '???  (Did you "pip install psutil"?)'
  print

  # Clean up.
  add-zsh-hook -d precmd print_startup_time
  unset startup_timer_module_path
}

autoload -Uz add-zsh-hook
add-zsh-hook precmd print_startup_time
