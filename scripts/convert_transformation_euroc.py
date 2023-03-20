import numpy as np
import yaml

# Load the EuroC stereo configuration file
config_file = '/home/liangchuan/Development/VINS-Fusion-gpu/config/euroc/euroc_stereo_config.yaml'
with open(config_file, 'r') as f:
    config = yaml.safe_load(f)
    # Get the transformation matrices from the camera frames to the body frame
    body_T_cam0 = config['body_T_cam0']
    body_T_cam1 = config['body_T_cam1']

print("body_T_cam0: {}".format(body_T_cam0))
print("body_T_cam1: {}".format(body_T_cam1))

# Get the transformation matrices from the camera frames to the body frame
cam0_T_body = np.linalg.inv(np.array(body_T_cam0['data']).reshape((4, 4)))
cam1_T_body = np.linalg.inv(np.array(body_T_cam1['data']).reshape((4, 4)))

# Compute the transformation matrix from the left camera to the right camera
T_cam0_cam1 = np.matmul(cam1_T_body, np.array(body_T_cam0['data']).reshape((4, 4)))


print("T_cam0_cam1: {}".format(T_cam0_cam1))