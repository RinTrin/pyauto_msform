# !/bin/sh

pip3 install selenium==4.1.0
if [ $1 == "start" ]; then
    python3 answer_start.py
else
    python3 answer_finish.py
fi