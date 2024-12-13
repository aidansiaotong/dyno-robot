# dyno-robot
**Dyno robot control source code.**

Controller Interface Installation (for a mechanical engineer who barely knows how computers work):

1. Flash Raspberry Pi 5 with Raspbian.
2. Install to Python virtual environment: ds4drv, msgpack, numpy, PS4Joystick, pyserial, UDPComms
3. Put joystick.service and dyno.service in the desktop.
4. Change the file locations in the service files in ExecStart= to match the
   locations of joystick.py and run-dyno.py
5. In terminal:
```shell
$ sudo mv ~/Desktop/joystick.service /etc/systemd/system/
$ sudo mv ~/Desktop/dyno.service /etc/systemd/system/
```
```shell
$ sudo systemctl daemon-reload
$ sudo systemctl enable joystick.service
$ sudo systemctl enable dyno.service
```
6. Put 50-ds4drv.rules in the desktop.
7. In terminal:
```shell
  $ sudo mv ~/Desktop/50-ds4drv.rules /etc/udev/rules.d/
  $ sudo udevadm control --reload-rules
  $ sudo udevadm trigger
```
9. Check if uinput is configured:
```shell
  $ lsmod | grep uinput
```
11. If nothing is returned in the terminal, put uinput.conf in the desktop.
12. In terminal:
```shell
  $ sudo mv ~/Desktop/uinput.conf /etc/modules-load.d/uinput.conf
  $ sudo modprobe uinput
```
13. Connect to wi-fi and reboot the Raspberry Pi. Upon startup, you should be able to pair the Raspberry Pi with a DualShock 4 controller.
14. Press R1 to activate Dyno.

**CONTROLS**
- R1: Activate/Deactivate
- x: Walk (single stride)
- circle: sit
- triangle: stand
- square: step up
