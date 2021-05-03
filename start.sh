#!/bin/bash

pause () {
 read -p -r "Press any key to continue . . ."
 echo ""
}

Start () {
  python3 main.py
  pause
  Start
}
Start
