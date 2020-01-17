# Install R
sudo apt update
sudo apt install gdebi libxml2-dev libssl-dev libcurl4-openssl-dev libopenblas-dev r-base r-base-dev


# Install common packages
R --vanilla << EOF
install.packages(c("tidyverse","data.table","dtplyr","devtools","roxygen2","bit64","readr"), repos = "https://cran.rstudio.com/")
q()
EOF


# Install Python Pip
sudo apt install python3-pip
sudo -H pip3 install markdown rpy2==2.9.3 pelican==3.7.1 

# Install Cran

# Install Git
sudo apt install git

# Use pip to install pandas, numpy, ipython, jupyter, scikit-learn, flask, and SQLite3
pip install scikit-learn
pip install pandas
pip install numpy
pip install ipython
pip install jupyter
pip install Flask
pip install pysqlite

# Install Anaconda 3 v2019.10

# Using Anaconda install Keras, PyTorch and TensorFlow


