MAC OS SETUP
Install Apple Xcode and accept license. You may need to update if you have an older version.

TERMINAL
xcode-select --install


Install Homebrew
TERMINAL
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


Install updated Python which includes pip.
TERMINAL
brew install python@3


TERMINAL
sudo pip install selenium
pip install pytest==3.2.1


USAGE (defaults to chrome browser)
pytest -m api
pytest -m ui
pytest -m ui --browser=chrome

*Verify:
-classpath is correct due to upgraded python version on mac osx with a native python 2.x version
-test ".py" runs without error on both sublime and terminal
-install all import requested libraries
-
