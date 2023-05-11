if lsof -Pi :9001 -sTCP:LISTEN -t >/dev/null ; then
    echo "Port 9001 is already in use."
else
    nc -l 9001
fi
