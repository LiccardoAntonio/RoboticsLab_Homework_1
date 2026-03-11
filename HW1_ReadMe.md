Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML``   # HW1 - Armando  ## Overview  This project contains the complete implementation of Homework 1 for the Robotics Lab course.  The project is organized into three ROS 2 packages:  - `armando_description`  - `armando_gazebo`  - `armando_controller`  The final result includes:  - visualization of the robot in **RViz**  - simulation in **Ignition / Gazebo**  - integration with **ign_ros2_control**  - loading of ROS 2 controllers  - simulated camera with image bridge through **ros_ign_bridge**  - C++ controller node for:    - **position control**    - **trajectory control**  The implementation follows the workflow requested in the homework:  1. robot visualization in RViz  2. simulation in Gazebo with controllers  3. camera integration  4. custom C++ controller node  ---  ## Workspace Structure  ```bash  ~/ros2_ws/src/HW1/  ├── armando_description  │   ├── launch/  │   │   └── armando_display.launch.py  │   ├── urdf/  │   │   ├── arm.urdf.xacro  │   │   └── armando_hardware_interface.xacro  │   ├── config/  │   │   ├── armando_controllers.yaml  │   │   └── rviz/  │   │       └── config.rviz  │   ├── meshes/  │   ├── CMakeLists.txt  │   └── package.xml  │  ├── armando_gazebo  │   ├── launch/  │   │   ├── armando_world.launch.py  │   │   └── armando_gazebo.launch.py  │   ├── urdf/  │   │   └── armando_camera.xacro  │   ├── CMakeLists.txt  │   └── package.xml  │  └── armando_controller      ├── src/      │   └── arm_controller_node.cpp      ├── launch/      ├── CMakeLists.txt      └── package.xml   ``

Main Features
-------------

### 1\. RViz Visualization

The robot is loaded from arm.urdf.xacro and visualized in RViz through:

*   robot\_state\_publisher
    
*   joint\_state\_publisher / joint\_state\_publisher\_gui
    
*   rviz2
    

The robot description is published on:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   /robot_description   `

Collision geometry is approximated with simple **box primitives**, while the visual geometry uses the original mesh files.

### 2\. Gazebo / Ignition Simulation

The robot is spawned in Gazebo using:

*   ros\_gz\_sim
    
*   robot\_state\_publisher
    
*   ign\_ros2\_control
    

The simulation loads the robot from /robot\_description and spawns it inside an empty world.

Controllers are loaded automatically after spawn using RegisterEventHandler.

### 3\. Controllers

The following controllers are defined:

*   joint\_state\_broadcaster
    
*   position\_controller
    
*   joint\_trajectory\_controller
    

They are configured in:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   armando_description/config/armando_controllers.yaml   `

Two control modes are supported:

*   controller\_type:=0 → position\_controller
    
*   controller\_type:=1 → joint\_trajectory\_controller
    

### 4\. Camera Integration

A camera sensor is attached to the robot and bridged to ROS 2 using:

*   ros\_ign\_bridge
    

The image topic is remapped to:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   /videocamera   `

This can be visualized with:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 run rqt_image_view rqt_image_view   `

### 5\. Custom C++ Control Node

The package armando\_controller contains a custom C++ node that:

*   subscribes to /joint\_states
    
*   prints the current joint values
    
*   publishes commands to:
    
    *   position\_controller/commands
        
    *   joint\_trajectory\_controller/joint\_trajectory
        

The node supports:

*   position-based motion
    
*   trajectory-based motion
    

The mode is selected through the parameter:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   controller_type   `

Dependencies
------------

Make sure the following packages are installed.

### ROS 2 basic tools

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   sudo apt update  sudo apt install \    ros-humble-joint-state-publisher \    ros-humble-joint-state-publisher-gui \    ros-humble-robot-state-publisher \    ros-humble-rviz2 \    ros-humble-xacro \    ros-humble-rqt-image-view   `

### Control and Gazebo / Ignition tools

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   sudo apt install \    ros-humble-controller-manager \    ros-humble-joint-state-broadcaster \    ros-humble-position-controllers \    ros-humble-joint-trajectory-controller \    ros-humble-ros-gz-sim \    ros-humble-ros-ign-bridge \    ros-humble-ign-ros2-control   `

Build
-----

From the workspace root:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd ~/ros2_ws  source /opt/ros/humble/setup.bash  colcon build --symlink-install  source install/setup.bash   `

If needed, force a clean rebuild:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd ~/ros2_ws  rm -rf build install log  source /opt/ros/humble/setup.bash  colcon build --symlink-install  source install/setup.bash   `

Run Instructions
----------------

1\. RViz Visualization
----------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 launch armando_description armando_display.launch.py   `

In RViz:

*   set Fixed Frame to base\_link
    
*   add RobotModel
    
*   use Description Topic = /robot\_description
    

2\. Gazebo Simulation - Position Controller Mode
------------------------------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 launch armando_gazebo armando_world.launch.py controller_type:=0   `

This launches:

*   Gazebo / Ignition
    
*   robot\_state\_publisher
    
*   robot spawning from /robot\_description
    
*   joint\_state\_broadcaster
    
*   position\_controller
    

To verify:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 control list_controllers   `

Expected active controllers:

*   joint\_state\_broadcaster
    
*   position\_controller
    

3\. Gazebo Simulation - Trajectory Controller Mode
--------------------------------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 launch armando_gazebo armando_world.launch.py controller_type:=1   `

Expected active controllers:

*   joint\_state\_broadcaster
    
*   joint\_trajectory\_controller
    

4\. Camera Bridge
-----------------

Run in a second terminal:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   source /opt/ros/humble/setup.bash  source ~/ros2_ws/install/setup.bash  ros2 launch armando_gazebo armando_gazebo.launch.py   `

Check image topics:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 topic list | grep -E "camera|videocamera"   `

Expected topic:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   /videocamera   `

5\. Visualize Camera Image
--------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 run rqt_image_view rqt_image_view   `

Then select:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   /videocamera   `

6\. Run C++ Controller Node - Position Mode
-------------------------------------------

Open a new terminal:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   source /opt/ros/humble/setup.bash  source ~/ros2_ws/install/setup.bash  ros2 run armando_controller arm_controller_node --ros-args -p controller_type:=0   `

This mode publishes commands on:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   position_controller/commands   `

7\. Run C++ Controller Node - Trajectory Mode
---------------------------------------------

Open a new terminal:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   source /opt/ros/humble/setup.bash  source ~/ros2_ws/install/setup.bash  ros2 run armando_controller arm_controller_node --ros-args -p controller_type:=1   `

This mode publishes commands on:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   joint_trajectory_controller/joint_trajectory   `

Useful Checks
-------------

### List controllers

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 control list_controllers   `

### Show joint states

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 topic echo /joint_states   `

### List topics

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 topic list   `

### Check robot description

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ros2 param get /robot_state_publisher robot_description   `

Important Notes
---------------

*   The robot meshes are used in the visual blocks.
    
*   The collision blocks are simplified using box primitives.
    
*   The project uses:
    
    *   ign\_ros2\_control
        
    *   ros\_ign\_bridge
        
*   The simulation is controlled through the parameter:
    
    *   controller\_type:=0 for position control
        
    *   controller\_type:=1 for trajectory control
        

Example Full Workflow
---------------------

### Position control workflow

Terminal 1:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd ~/ros2_ws  source /opt/ros/humble/setup.bash  source install/setup.bash  ros2 launch armando_gazebo armando_world.launch.py controller_type:=0   `

Terminal 2:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd ~/ros2_ws  source /opt/ros/humble/setup.bash  source install/setup.bash  ros2 launch armando_gazebo armando_gazebo.launch.py   `

Terminal 3:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd ~/ros2_ws  source /opt/ros/humble/setup.bash  source install/setup.bash  ros2 run armando_controller arm_controller_node --ros-args -p controller_type:=0   `

Terminal 4:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd ~/ros2_ws  source /opt/ros/humble/setup.bash  source install/setup.bash  ros2 run rqt_image_view rqt_image_view   `

### Trajectory control workflow

Terminal 1:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd ~/ros2_ws  source /opt/ros/humble/setup.bash  source install/setup.bash  ros2 launch armando_gazebo armando_world.launch.py controller_type:=1   `

Terminal 2:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd ~/ros2_ws  source /opt/ros/humble/setup.bash  source install/setup.bash  ros2 run armando_controller arm_controller_node --ros-args -p controller_type:=1   `

Final Result
------------

At the end of the project, the following functionalities are available:

*   robot visible in RViz
    
*   robot spawned in Gazebo / Ignition
    
*   controllers loaded correctly
    
*   robot movable through position or trajectory commands
    
*   camera image bridged to ROS 2
    
*   camera stream visualized in rqt\_image\_view
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML
