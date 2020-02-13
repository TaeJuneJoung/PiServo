# 파이썬 라즈베리파이 서보 모터 모듈 제어

라즈베리파이와 서보 모터를 파이썬을 이용하여 제어하는 라이브러리



## 필요 조건

- Python3.x

- pip install RPi.GPIO
- OS : Unix 계열


## 사용 방법

본 소스는 라즈베리파이와 파이썬에 익숙하지 않은 사람들을 위해 교육용으로 제작되었습니다.
파이썬으로 서보 모터를 다룰 수 있으며, 사용 예시는 `test_servo.py`를 통해 테스트 해보실 수 있습니다.

서버 모터 핀은 GPIO PWM 핀에 꽂는 것을 권장드립니다.
서버 모터의 각도는 0~180도를 지원하고 있는 SG90 모듈을 사용하였기에 0~180도를 지원하고 있습니다.


### 1. Interface
Class Servo를 이용합니다.
`test_servo.py`가 Interface를 사용한 예시입니다.


### 2. Argv
Flask, Pi Camera와 연동하여 실시간 비디오 웹 스트리밍을 위해 맞춤형 소스입니다.
```python
import os

os.system('python piservo.py 32 135')
```
32번 핀에 서버 모터 GPIO핀이 꽂혀있으며, 135도를 돌리라는 방법입니다.

