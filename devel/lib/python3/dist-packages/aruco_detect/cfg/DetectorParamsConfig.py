## *********************************************************
##
## File autogenerated for the aruco_detect package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'adaptiveThreshConstant', 'type': 'double', 'default': 7.0, 'level': 0, 'description': 'Constant for adaptive thresholding before finding contours', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'adaptiveThreshWinSizeMin', 'type': 'int', 'default': 3, 'level': 0, 'description': 'Minimum window size for adaptive thresholding before finding contours', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'adaptiveThreshWinSizeMax', 'type': 'int', 'default': 53, 'level': 0, 'description': 'Maximum window size for adaptive thresholding before finding contours', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'adaptiveThreshWinSizeStep', 'type': 'int', 'default': 4, 'level': 0, 'description': 'Increments from adaptiveThreshWinSizeMin to adaptiveThreshWinSizeMax during the thresholding', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'cornerRefinementMaxIterations', 'type': 'int', 'default': 30, 'level': 0, 'description': 'Maximum number of iterations for stop criteria of the corner refinement process', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'cornerRefinementMinAccuracy', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'Minimum error for the stop criteria of the corner refinement process', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'cornerRefinementWinSize', 'type': 'int', 'default': 5, 'level': 0, 'description': 'Window size for the corner refinement process (in pixels)', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'doCornerRefinement', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Whether to do subpixel corner refinement', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'cornerRefinementSubpix', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Whether to do subpixel corner refinement (true) or contour (false)', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'errorCorrectionRate', 'type': 'double', 'default': 0.6, 'level': 0, 'description': 'Error correction rate respect to the maximum error correction capability for each dictionary', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'minCornerDistanceRate', 'type': 'double', 'default': 0.05, 'level': 0, 'description': 'Minimum distance between corners for detected markers relative to its perimeter', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'markerBorderBits', 'type': 'int', 'default': 1, 'level': 0, 'description': 'Number of bits of the marker border, i.e. marker border width', 'min': 0, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'maxErroneousBitsInBorderRate', 'type': 'double', 'default': 0.04, 'level': 0, 'description': 'Maximum number of accepted erroneous bits in the border (i.e. number of allowed white bits in the border)', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'minDistanceToBorder', 'type': 'int', 'default': 3, 'level': 0, 'description': 'Minimum distance of any corner to the image border for detected markers (in pixels)', 'min': 0, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'minMarkerDistanceRate', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'minimum mean distance beetween two marker corners to be considered similar, so that the smaller one is removed. The rate is relative to the smaller perimeter of the two markers', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'minMarkerPerimeterRate', 'type': 'double', 'default': 0.03, 'level': 0, 'description': 'Determine minumum perimeter for marker contour to be detected. This is defined as a rate respect to the maximum dimension of the input image', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'maxMarkerPerimeterRate', 'type': 'double', 'default': 4.0, 'level': 0, 'description': 'Determine maximum perimeter for marker contour to be detected. This is defined as a rate respect to the maximum dimension of the input image', 'min': 0.0, 'max': 4.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'minOtsuStdDev', 'type': 'double', 'default': 5.0, 'level': 0, 'description': 'Minimun standard deviation in pixels values during the decodification step to apply Otsu thresholding (otherwise, all the bits are set to 0 or 1 depending on mean higher than 128 or not)', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'perspectiveRemoveIgnoredMarginPerCell', 'type': 'double', 'default': 0.13, 'level': 0, 'description': 'Width of the margin of pixels on each cell not considered for the determination of the cell bit. Represents the rate respect to the total size of the cell, i.e. perpectiveRemovePixelPerCell', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'perspectiveRemovePixelPerCell', 'type': 'int', 'default': 8, 'level': 0, 'description': 'Number of bits (per dimension) for each cell of the marker when removing the perspective', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'polygonalApproxAccuracyRate', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'Minimum accuracy during the polygonal approximation process to determine which contours are squares', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']
