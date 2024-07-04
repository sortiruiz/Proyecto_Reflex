cd link_bio
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init 
API_URL=https://sortiruiz-web.up.railway.app reflex export --frontend-only #me exporta la parte estatica 

#desde terminal ubuntu 
rm -rf public #esto me borra la antigua carpeta public
unzip  frontend.zip -d public #esto me lo unzipea a public 
rm -f frontend.zip #me borra el zip

deactivate
#rd frontend.zip
