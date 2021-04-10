#!/bin/bash

pause () {
 read -p -r "Press any key to continue . . ."
 echo ""
}

Start () {
  pause
  Start
}
Start
