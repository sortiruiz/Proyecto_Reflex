#venv/Scripts/activate
#pip install -r requirements.txt
reflex init 
API_URL=https://sortiruiz-web.up.railway.app reflex export --frontend-only #me exporta la parte estatica 

#desde terminal ubuntu 
wsl rm -rf public #esto me borra la antigua carpeta public
wsl unzip  frontend.zip -d public #esto me lo unzipea a public 
wsl rm -f frontend.zip #me borra el zip

#rd frontend.zip