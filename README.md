# Onshape to robot examples

Here you will find several examples of robots that were design to be exported properly using the
[onshape-to-robot](https://github.com/Rhoban/onshape-to-robot) tool.

Have a look at the [design-time considerations](https://onshape-to-robot.readthedocs.io/en/latest/design.html)
to understand better the constraints to export your robot.

Before testing, in a nutshell, you need `onshape-to-robot`:

    pip install onshape-to-robot

This repository contains both `config.json` file and resulting export. You can use the following commands to visualize
the result:

    # Start PyBullet simulation
    onshape-to-robot-bullet directory
    # Start MuJoCo simulation
    onshape-to-robot-mujoco directory

## Robots

### 2 wheels

<a href=".imgs/robot-2wheels.png">
<img src=".imgs/robot-2wheels.png" width=256>
</a>

Description: Very simple design and minimalistic configuration

* Give it a try
    * `onshape-to-robot-bullet 2wheels_urdf`
    * `onshape-to-robot-mujoco 2wheels_mujoco`
* [Onshape design](https://cad.onshape.com/documents/862948a6ea6d38343e1d3272/w/98cee18311a3b8d7c10abc42/e/9332fc5299824befd8ebf702)
* `config.json`
    * [urdf](2wheels_urdf/config.json)
    * [mujoco](2wheels_mujoco/config.json)
* **Notes**:
    * The joint properties are set to use `continuous` with URDF format, and `velocity` controlled in MuJoCo
    * `wheel2` has the `_inv` suffix, which changes its direction making both wheels spin in same direction
  when same sign of order is given**

### Adjustable height arm

<a href=".imgs/robot-adjustable_height_arm.png">
<img src=".imgs/robot-adjustable_height_arm.png" width=256>
</a>

Description: Robot with 4 degrees of freedom, one prismatic (linear) joint and 3 rotations

* Give it a try
    * `onshape-to-robot-bullet -f adjustable_height_arm_urdf` (note: `-f` is passed to fix the base to the ground)
    * `onshape-to-robot-mujoco adjustable_height_arm_mujoco`
* [Onshape design](https://cad.onshape.com/documents/6a6e5b10ef079339c2ddde84/w/207da6d79692e0bbf50113f2/e/9f3edd12689fa0c486a7d0d7)
* `config.json`
    * [urdf](adjustable_height_arm_urdf/config.json)
    * [mujoco](adjustable_height_arm_mujoco/config.json)
* **Notes**:
    * The robot is fixed using a "fixed" Onshape feature
    * There is one frame (`frame_tip`) attached to the tip of the arm
    * Collisions mesh are ignored using `no_collision_meshes`

### Robot-soccer-kit omnidirectional

<a href=".imgs/robot-rsk.png">
<img src=".imgs/robot-rsk.png" width=256>
</a>

Description: an omnidirectional robot from the [robot-soccer-kit](https://robot-soccer-kit.github.io/) project.

* Give it a try
    * `onshape-to-robot-bullet rsk_urdf`
    * `onshape-to-robot-mujoco rsk_mujoco`
* [Onshape design](https://cad.onshape.com/documents/81e7adfaf4d8d74f2936fbd5/w/97141f458dee8c3b80cbf3d2/e/5e1ff591ff562de3da8ed2af)
* `config.json`
    * [urdf](rsk_urdf/config.json)
    * [mujoco](rsk_mujoco/config.json)
* **Notes**:
    * In MuJoCo, passive wheels are marked as unactuated.
    * In URDF, fixed links are added to the base, mostly to preserve colors in pyBullet.
    * Each small wheel is a degree of freedom. This approach is tedious and likely sub-optimal to simulate such robot.

### Quadruped

<a href=".imgs/robot-quadruped.png">
<img src=".imgs/robot-quadruped.png" width=256>
</a>

Description: 12 DOF quadruped robot, design similar to the [Metabot open-source project](https://github.com/rhoban/metabot) using
[XL-320](http://emanual.robotis.com/docs/en/dxl/x/xl320/) servos.

* Give it a try:
    * `onshape-to-robot-bullet quadruped_urdf`
    * `onshape-to-robot-mujoco quadruped_mujoco`
* [Onshape design](https://cad.onshape.com/documents/11a7f59e37f711d732274fca/w/7807518dc67487ad405722c8/e/5233c6445c575366a6cc0d50)
* `config.json`
    * [urdf](quadruped_urdf/config.json)
    * [mujoco](quadruped_mujoco/config.json)
* **Notes**:
    * Full pure shape approximation (OpenSCAD) for collisions
    * Frames in the trunk (`trunk_frame`) and in the tip of one leg (`tip_frame`)
    * A frame is attached to the tip of a leg (`leg_tip`)

### Dog

<a href=".imgs/robot-dog.png">
<img src=".imgs/robot-dog.png" width=256>
</a>

Description: 12 DOF dog robot, made for fun with [MX-64](http://emanual.robotis.com/docs/en/dxl/mx/mx-64-2/) servos (was actually built)

* Give it a try:
    * `onshape-to-robot-bullet dog`
    * `onshape-to-robot-mujoco dog`
* [Onshape design](https://cad.onshape.com/documents/adaeaba919da3242f78691a7/w/d80460ae3edd273c69c822a5/e/c8ebe3aba51c8ed2734fad87)
* [config.json](dog/config.json)
* No pure shape approximation (pure STLs)
* Dynamics is overridden for MX-64 and MX-106, since it is provided by constructor

### Sigmaban2019

<a href=".imgs/robot-sigmaban2019.png">
<img src=".imgs/robot-sigmaban2019.png" width=256>
</a>

Description: 20 DOF humanoid robot, snapshot of 2019 Sigmaban model from team [Rhoban](https://www.youtube.com/watch?v=tF0cr0PYjsk),
used at RoboCup kid size

* Give it a try:
    * `onshape-to-robot-bullet sigmaban2019_urdf`
    * `onshape-to-robot-mujoco sigmaban2019_mujoco`
* [Onshape design](https://cad.onshape.com/documents/41654e89e61a392d020b728c/w/d555ceec170d351622b789de/e/4c9a04a707c36ac7ad2ca0f8)
* `config.json`
    * [urdf](sigmaban2019_urdf/config.json)
    * [mujoco](sigmaban2019_mujoco/config.json)
* **Notes**:
    * Full pure shape approximation (OpenSCAD) for collisions
    * Frames in the trunk (`trunk_frame`), in feet (`right_foot_frame`, `left_foot_frame`), the camera
    (`camera_frame), the head base (`head_base_frame`) and some location to use Vive tracker for ground-truth
    (`vive_frame`).
    * In the URDF format, STLs are merged and simplified

### Orbita SPM

<a href=".imgs/robot-orbita.png">
<img src=".imgs/robot-orbita.png" width=256>
</a>

Description: Orbita is a type of spherical parallel manipulator with 3 DOFs.

* Give it a try:
    * `onshape-to-robot-mujoco field_mujoco`
* [Onshape design](https://cad.onshape.com/documents/38fc7348876da4041a20509c/w/bce45e5d7d8fe5e1a5ca0706/e/8fac25f2212dc9936ef3196b)
* `config.json`
    * [mujoco](orbita_mujoco/config.json)
* **Notes:**
    * The based is fixed using a fixed constraint
    * Two loop closures are used here in order to ensure the mechanism is fully constrained
    * Collisions are disabled in this example

### MoMo: An Open-Source Modular Mobile Robot Research Platform

<a href=".imgs/momo.png">
<img src=".imgs/momo.png" width=256>
</a>

Description: [MoMo](https://tuhh-itl.github.io/MoMo/) is a modular mobile robot research platform developed at the [Institut für Technische Logistik](https://www3.tuhh.de/itl/) - [TUHH](https://www.tuhh.de/tuhh/startseite).

* Give it a try:
    * `onshape-to-robot-bullet momo_urdf`
    * `onshape-to-robot-mujoco momo_mujoco`
* [Onshape design](https://cad.onshape.com/documents/0f7ba08d49760d832652e76c/w/f802382a554ac4e5d967eb06/e/176c79e9883e5c00c7190ba1)
* `config.json`
    * [urdf](momo_urdf/config.json)
    * [mujoco](momo_mujoco/config.json)
* **Notes:**
    * Each wheel has 12 rollers, each of them is a degree of freedom
    * Collisions are approximated using OpenScad manual approximation

### Field

<a href=".imgs/robot-field.png">
<img src=".imgs/robot-field.png" width=256>
</a>

Description: This is not actually a robot, but an environment that is designed in Onshape and can be converted into an URDF file

* Give it a try:
    * `onshape-to-robot-bullet field_urdf`
    * `onshape-to-robot-mujoco field_mujoco`
* [Onshape design](https://cad.onshape.com/documents/7c9b2b33f4117af700005b74/w/eec38b17995152d190f4b18a/e/82b08cac68e6478dadc7fda9)
* `config.json`
    * [urdf](field_urdf/config.json)
    * [mujoco](field_mujoco/config.json)
* **Notes:**
    * Since it is a static environment, `no_dynamics` is passed
    * There are multiple root nodes in this robot. Thus, `add_dummy_base_link` option is added in URDF to ensure there is only one root node.
    * This is a model of RoboCup humanoid soccer kid-size (2019) 6 x 9 m field
    * In URDF, the `use_fixed_links` option is set to `true` so that the colors of different sub-part are kept

## Re-running the imports yourself

### Instructions

Read the instructions from the [onshape-to-robot repository](https://github.com/Rhoban/onshape-to-robot), especially
be sure to have the API key registered and set as environment variable before running `onshape-to-robot`.

To get the same results, you might need `openscad` and `meshlab` installed.

    sudo apt-get install openscad meshlab

Else, pure shape approximation and meshes simplification might be disabled.

### Why do I get `ERROR (403) while using OnShape API` ?

If you want to export the robots yourself, you need to have the rights to access to the assembly. Thus, if you want to
re-run the import for the examples in this repository, you will have to make your own copy of the document. Fortunately,
this is quite simple because it is just about clicking on that button on top left:

![make a copy](.imgs/make-copy.png)

Then, update the `url` parameter in `config.json` of the robot to match the new document created where you own the robot
design.

### Why the colors are looking weird in pyBullet ?

Actually, pyBullet does only keep one color per link currently in the viewer. This is a known limitation that does not
affect your physical simulations.
(https://github.com/bulletphysics/bullet3/issues/2650)

For instance, the quadruped robot above will look like this:

![Quadruped](.imgs/pybullet-quadruped.png)
