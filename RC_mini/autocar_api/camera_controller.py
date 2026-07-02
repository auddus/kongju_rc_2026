class CameraController:
    def __init__(self):
        self.pan = 90
        self.tilt = 90

    def set_pan_tilt(self, pan, tilt):
        # 범위 제한 (0~180도)
        self.pan = max(0, min(180, pan))
        self.tilt = max(0, min(180, tilt))
        print(f"[MOCK CAMERA] Pan: {self.pan}도, Tilt: {self.tilt}도 설정")
        return self.pan, self.tilt
    