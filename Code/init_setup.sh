echo [$(date)] : "START"
echo [$(date)] : "Creating an Environment with Python 3.8 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)] : "Activating the Environment"
source activate ./env
echo [$(date)] : "Installing the dev requirements"
pip install -r requirements_dev.txt
echo [$(date)] : "END"