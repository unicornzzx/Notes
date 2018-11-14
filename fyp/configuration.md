#### 组件版本总览
---
1. Nvidia GPU drive: 最新版（390.87）
2. CUDA: 9.0.176 (4 patches)
3. cudnn: 7.05
4. g++/gcc: 6.4.0
5. tensorflow: 1.6
6. deeplab v3+

#### 安装显卡驱动
---
* 文件下载：官网最新驱动 .run 文件
* 禁用系统自带的开源驱动nouveau
    1. 创建文件：` /usr/lib/modprobe.d/blacklist-nouveau.conf`
    2. 在创建的conf文件中输入：
        ```
        blacklist nouveau
        blacklist lbm-nouveau
        options nouveau modeset=0
        alias nouveau off
        alias lbm-nouveau off
        ```
    3.修改blacklist conf:
        `sudo gedit /etc/modprobe.d/blacklist.conf`   
        在文件末尾添加：   
        
        ```
        blacklist vga16fb
        blacklist nouveau
        blacklist rivafb
        blacklistnvidiafb
        blacklist rivatv 
        ```
    3. 重新配置内核文件： `sudo update-initramfs -u` 或 `sudo dracut --force`
    4. reboot
* 安装`NVIDIA-Linux-x86_64-390.87.run`
    1. 停止可视化桌面：```$ sudo telinit 3 ``` 
    2. 进入tty：`crtl + alt + F3~F7
    3. 关闭gdm: `sudo service gdm stop`
    4. cd 到下载的.run文件的位置
    5. 更改文件读写权限：`sudo chmod +x NVIDIA-Linux-x86_64-390.77.run`
    6. 运行：`./NVIDIA-Linux-x86_64-390.87.run`
    7. 安装完毕后: `sudo service gdm restart`
    7. 查看驱动版本 `$ nvidia-smi`
    8. reboot

#### 安装CUDA
---
* 前期准备
    1. 文件下载：CUDA 9.0 的主安装文件和四个补丁 均为.run
    2. g++/gcc 降级   
    sudo add-apt-repository ppa:ubuntu-toolchain-r/rest   
    sudo apt-get update
        1.`sudo apt-get install gcc-6.4` & `sudo apt-get install g++-6.4`
        2. 版本切换(g++同理)
        
            ```
            #更新gcc6.4版本在多版本控制器的优先度
            sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6.4 50
            
            #查看配置情况
            sudo update-alternatives --config gcc
            ```
* 安装依赖   
`sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libgl1-mesa-glx libglu1-mesa libglu1-mesa-dev`
* 进入tty 安装所有.run 文件
* 配置CUDA环境
    `sudo gedit ~/.bashrc`
    末尾添加   

    ```
    export PATH=/usr/local/cuda-9.0/bin:$PATH
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-9.0/lib64
    export CUDA_HOME=/usr/local/cuda-9.0
    ```
    查看CUDA版本：`$ Nvcc -V`

#### 安装cudnn
---
1. 解压下载的.tgz文件 得到一个名为CUDA的文件夹
2. 复制那个文件夹里的文件去CUDA的安装目录

    ```
    sudo cp cuda/include/cudnn.h /usr/local/cuda/include 
    sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64 
    sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
    ```
#### 安装tensorflow
