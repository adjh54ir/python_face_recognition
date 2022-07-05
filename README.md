# python_face_recognition

> `Python의 face_recognition 오픈소스를 기반으로 얼굴 탐지 기능` 

<br>

# 1) cmake 설치 가이드 

> CMake란 여러 환경(window , linux 등)에 맞는 build process를 작성한 것으로, 
CMakeLists.txt에 기술된 내용을 바탕으로 각 확경에 맞는 Makefile을 생성해 주는 빌드 프로그램이다. 
CMake를 통해 Makefile을 만들게 되면, 추가적인 파일이 추가되지 않는 한 Makefile을 수정하지 않고, 자동으로 생성해준다는 장점이 있지만,
단순히 Makefile을 생성해 주는 것이기 때문에 Make를 추가로 해야한다.


    # default pip install 
    $ pip install --upgrade pip

    # install cmake 
    $ brew install cmake

    # cmake version 3.23.2
    $ cmake --version 

    $ pip install cmake


# 2) dlib 설치 가이드
> C++로 실제 기계 학습 및 데이터 분석 애플리케이션을 만들기 위한 툴킷

    # git clone
    $ git clone <https://github.com/davisking/dlib.git>

    $ cd dlib

    $ mkdir build

    $ cd build

    # 해당 부분에서 에러 발생 하단 참고!
    $ cmake ..

    $ cmake --build .

    $ cd ..

    $ sudo python3 setup.py install

 
<br>
    
> cmake .. 에 대한 에러 발생

    CMake Error at /usr/local/Cellar/cmake/3.23.2/share/cmake/Modules/CMakeTestCCompiler.cmake:69 (message):
    The C compiler

    "/usr/bin/cc"

    is not able to compile a simple test program.

    It fails with the following output:

    Change Dir: /Users/lee/Desktop/workspace/WHATNEED/dlib/build/CMakeFiles/CMakeTmp

    Run Build Command(s):/usr/bin/make -f Makefile cmTC_e7b91/fast && xcrun: error: active developer path ("/Applications/Xcode.app/Contents/Developer") does not exist
    Use `sudo xcode-select --switch path/to/Xcode.app` to specify the Xcode that you wish to use for command line developer tools, or use `xcode-select --install` to install the standalone command line developer tools.
    See `man xcode-select` for more details.

    CMake will not be able to correctly generate this project.
    Call Stack (most recent call first):
    CMakeLists.txt:3 (project)

<br> 

> 해결책
<br>


    # xcode-select version 2395.
    $ xcode-select --version

    $ sudo xcode-select --reset

# 3) face_recognition 라이브러리 설치

    $ pip install face_recognition

    # Reference 
    $ pip install -r requirements.txt
    $ pip install -r requirements_dev.txt

# 4) 기타 라이브러리 설치

    $ pip install opencv-python


 