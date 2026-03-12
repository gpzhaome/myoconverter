#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run the full OpenSim-to-MuJoCo conversion pipeline for the Gait2354Simbody example.

Created on Tue Jul 27 23:19:13 2021

@author: hwang
"""

from myoconverter.O2MPipeline import O2MPipeline


# Define pipeline configuration.
kwargs = {}
kwargs["convert_steps"] = [1, 2, 3]          # Run all three conversion steps.
kwargs["muscle_list"] = None                 # Optimize all muscles.
kwargs["osim_data_overwrite"] = True         # Regenerate cached OpenSim state data.
kwargs["conversion"] = True                  # Run the conversion steps.
kwargs["validation"] = True                  # Run the validation steps.
kwargs["speedy"] = False                     # Keep the full optimization settings.
kwargs["generate_pdf"] = True                # Generate the validation PDF report.
kwargs["add_ground_geom"] = True             # Add a ground geometry to the converted model.
kwargs["treat_as_normal_path_point"] = False # Keep moving and conditional path points dynamic.


# Gait2354Simbody example
osim_file = "./models/osim/Gait2354Simbody/gait2354.osim"
geometry_folder = "./models/osim/Gait2354Simbody/Geometry"
output_folder = "./models/mjc/Gait2354Simbody"


if __name__ == "__main__":
    O2MPipeline(osim_file, geometry_folder, output_folder, **kwargs)
