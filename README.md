# pibot
Robot doing robot things with a Raspberry Pi

**Current hardware:**
- [Raspberry Pi 3 - Model B+](https://www.adafruit.com/product/3775)
- [uSDHC Card - 32GB](https://www.amazon.com/gp/product/B010Q57T02/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)
- [Raspberry Pi Camera Board v2 - 8MP](https://www.adafruit.com/product/3099)
- [Adafruit 9-DOF IMU Breakout - BNO055](https://www.adafruit.com/product/2472)

**Current software:**
- [Raspbian GNU/Linux 9 - stretch](https://www.raspberrypi.org/downloads/raspbian/) (booting from SD-card)
- [GCC](https://gcc.gnu.org/) [`sudo apt install build-essential`]
- [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/) [`sudo apt install pkg-config`]
- [CMake](https://cmake.org/) [`sudo apt install cmake`]
- C++
  - [BLAS](http://www.netlib.org/blas/) [`sudo apt install libblas-dev`]
  - [LAPACK](http://www.netlib.org/lapack/) [`sudo apt install liblapack-dev`]
  - [ATLAS](http://math-atlas.sourceforge.net/) [`sudo apt install libatlas-dev`]
  - [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page) [`sudo apt install libeigen3-dev`] (or from [this git mirror](https://github.com/eigenteam/eigen-git-mirror))
  - [This guide](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/) for installing [OpenCV](https://opencv.org/) from [here](https://github.com/opencv/opencv)
- Python
  - [NumPy](http://www.numpy.org/) [`sudo apt install python-numpy`] (I think it was also necessary to upgrade with PIP)
  - [SciPy](https://www.scipy.org/) [`sudo apt install python-scipy`]
  - [matplotlib](https://matplotlib.org/) [`sudo apt install python-matplotlib`]
  - [BNO055 Driver](https://github.com/adafruit/Adafruit_Python_BNO055) (git clone and run setup.py)
- [Firefox](https://www.mozilla.org/en-US/) [`sudo apt install firefox-esr`]
- Free up some space by uninstalling Libre Office [`sudo apt remove --purge libreoffice*`]

**To-Do:**
- [visual-inertial odometry](https://en.wikipedia.org/wiki/Visual_odometry)
- fly or walk, drive or something I dunno it can be a whatever kind of robot
