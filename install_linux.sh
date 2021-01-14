EXECUTEONCE="executeonce.txt"
if [ -f "$EXECUTEONCE" ]; then
  echo "Attempting to install virtualenv"
  python3 -m pip install virtualenv && echo "virtualenv installed"

  if [ ! -d 'venv' ]; then
    python3 -m virtualenv venv && echo "Initialized a virtual environment"
  fi
  source venv/bin/activate && echo "Sourced into venv"

  if [ -f 'requirements.txt' ]; then
    python3 -m pip install -r requirements.txt
  else
    echo "Cannot find requirements.txt"
    return 1
  fi
  echo "Attempting to execute 'sudo chmod u+x ./main.py' -- need password..."
  sudo chmod u+x ./script.py || return 1
  rm $EXECUTEONCE  # remove to skip this on next execute
  echo "Setup complete."

else

  # if already setup just execute
  ./script.py || {
    touch "$EXECUTEONCE";  # on error, reset for next execute;
    echo "$EXECUTEONCE" reinitialized;
    exit 1
  }
fi