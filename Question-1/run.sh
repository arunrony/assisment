if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Running App.py File"
        source .venv/bin/activate
        export MAIL_SERVER="cloud.cloudparas.in"
        export MAIL_PORT=465
        export MAIL_USERNAME="me@arunbamniya.com"
        export MAIL_PASSWORD="sanzWFMENGCE3vi"
        export MAIL_USE_TLS=false
        export MAIL_USE_SSL=true
        python ./app.py
        curl http://127.0.0.1:5000/

elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
        echo "windows emulation"
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
elif [[ "$OSTYPE" == "win32" ]]; then
         echo "windows"
        # I'm not sure this can happen.
fi