MAC OS SETUP
Install Apple Xcode and accept license. You may need to update if you have an older version.

TERMINAL
xcode-select --install


Install Homebrew
TERMINAL
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


Install updated Python which includes pip.
TERMINAL
brew install python@2


TERMINAL
sudo pip install selenium
pip install pytest==3.2.1


USAGE (defaults to chrome browser)
pytest -m api
pytest -m ui
pytest -m ui --browser=chrome
pytest -m ui --browser=firefox
