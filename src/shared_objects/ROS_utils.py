SHOW = False

class Topics:
    def __init__(self) -> None:
        self.topic_names = {
            "speed": "ECU/speed",
            "throttle": "ECU/throttle",
            "rpm": "ECU/rpm",
            "steering": "commands/KalmanAngle",
            "requested_speed": "commands/speed",
            "stop": "commands/stop",
            "model_enable": "status/model_enable",
            "engine_enable": "status/engine_enable",
            "stop_enable": "status/stop_enable",
            "RGB_image": "/zed/zed_node/rgb/image_rect_color",  # Updated to ZED rectified RGB image
            "segmented_image": "/zed/zed_node/rgb/image_rect_color",  # Replace this if a ZED segmentation topic exists
            "goal": "/move_base_simple/goal",
            "costmap": "/planner/move_base/local_costmap/costmap",
        }
