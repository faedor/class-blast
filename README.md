installing chrome driver

mkdir -p $HOME/bin
chmod +x chromedriver
mv src/drivers/chromedriver $HOME/bin

additional:
echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_profile


OSX:
export PATH=$PATH:/{folder with driver}/



install PhantomJS

export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
sudo tar xvjf $PHANTOM_JS.tar.bz2
sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin