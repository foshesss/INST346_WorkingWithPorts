if lsof -Pi :9001 -sTCP:LISTEN -t >/dev/null ; then
    lsof -i :9001
else
    echo "Port 9001 is not currently in use."
fi