# SC3-GW
Smart controller 3 gateway. 

## Building SC3-GW
```
mkdir -p ~/ros_ws/src
cd ros_ws/src
git clone https://github.com/hakoroboken/SC3-GW
cd ~ros_ws
colcon build --symlink-install
```

## Launch
```
source ~/ros_ws/install/setup.sh
ros2 launch sc3_gw demo.py
```



