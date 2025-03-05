import os
import pinocchio
import mujoco
from onshape_to_robot.message import bright, error, info

examples = [
    "2wheels_urdf", "2wheels_mujoco",
    "adjustable_height_arm_urdf", "adjustable_height_arm_mujoco",
    "rsk_urdf", "rsk_mujoco",
    "quadruped_urdf", "quadruped_mujoco",
    "dog_urdf", "dog_mujoco",
    "sigmaban2019_urdf", "sigmaban2019_mujoco",
    "orbita_mujoco",
    "field_urdf", "field_mujoco",
]

def process_example(example: str):
    print('')
    print(bright(f"========== Running {example} =========="))
    print("")
    
    result = os.system(f"python -m onshape_to_robot.export {example}")
    if result == 0:
        if "urdf" in example:
            print(info("Loading model in pinocchio"))
            output_filename = f"{example}/robot.urdf"
            model = pinocchio.buildModelFromUrdf(output_filename)
            pinocchio.buildGeomFromUrdf(model, output_filename, pinocchio.COLLISION, package_dirs=os.path.dirname(output_filename))
            pinocchio.buildGeomFromUrdf(model, output_filename, pinocchio.VISUAL, package_dirs=os.path.dirname(output_filename))
        elif "mujoco" in example:
            print(info("Loading model in mujoco"))
            output_filename = f"{example}/scene.xml"
            mujoco.MjModel.from_xml_path(output_filename)
    else:
        raise Exception(f"Failed to run example {example}")

for example in examples:
    try:
        process_example(example)
    except Exception as e:
        print("")
        print(error(f"Failed to run example {example}"))
        print(e)
        input()
    
