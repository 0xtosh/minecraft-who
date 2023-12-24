#!/bin/bash

while true; do
    # Listen on port 5000
    {
        echo -ne "HTTP/1.1 200 OK\r\n";
        echo -ne "Content-Type: application/json\r\n";
        echo -ne "Access-Control-Allow-Origin: *\r\n";
        echo -ne "Content-Length: $(echo -n '{ "players": ["sethbling", "shalz", "DanTDM"] }' | wc -c)\r\n";
        echo -ne "\r\n";
        echo -ne '{ "players": ["sethbling", "shalz", "DanTDM"] }\r\n';
    } | nc -l -p 5000 -q 1;
done

