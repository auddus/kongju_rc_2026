class CarController:
    def __init__(self):
        self.speed = 0
        self.steering = 0

    def set_motor(self, speed):
        if speed < -100: speed = -100
        elif speed > 100: speed = 100
        self.speed = speed
        # [실제 하드웨어 코드로 교체해야 하는 위치]
        print(f"[MOCK MOTOR] 속도 설정: {self.speed}")
        return self.speed

    def set_steering(self, angle):
        if angle < -45: angle = -45
        elif angle > 45: angle = 45
        self.steering = angle
        # [실제 하드웨어 코드로 교체해야 하는 위치]
        print(f"[MOCK STEERING] 조향각 설정: {self.steering}")
        return self.steering

    def stop(self):
        self.speed = 0
        self.steering = 0
        print("[MOCK EMERGENCY STOP] 긴급 정지! 속도 0, 조향 0")