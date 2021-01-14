# CONSTANTS - FILENAMES
EXECUTEONCE=".executeonce"


[[ -f "$EXECUTEONCE" ]] && {
  python3 -m pip install virtualenv;
  python3 -m virtualenv venv;
  source venv/bin/activate;
  if [ -f 'requirements.txt' ]; then
    python3 -m pip install -r requirements.txt
  else
    echo "Cannot find requirements.txt"
    return 1
  fi
  sudo chmod u+x ./main.py || return 1;
  rm $EXECUTEONCE;  # remove to skip this on next execute
  echo "Setup complete.";
} || {
  # if already setup just execute
  # ./main.py || {
  touch "$EXECUTEONCE";  # on error, reset for next execute;
  echo "$EXECUTEONCE" reinitialized;
  exit 1
}
