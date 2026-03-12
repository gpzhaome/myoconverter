import argparse

from myoconverter.O2MPipeline import O2MPipeline


def add_bool_flag(parser, name, default, help_text):
    flag_name = name.replace("_", "-")
    parser.add_argument(
        f"--{flag_name}",
        dest=name,
        action="store_true",
        help=help_text,
    )
    parser.add_argument(
        f"--no-{flag_name}",
        dest=name,
        action="store_false",
        help=f"Disable: {help_text.lower()}",
    )
    parser.set_defaults(**{name: default})


parser = argparse.ArgumentParser(
    description="Run the OpenSim-to-MuJoCo conversion pipeline from the command line.",
    prog="O2M",
)
parser.add_argument("--osim-file", dest="osim_file", required=True, help="Path to the OpenSim model file.")
parser.add_argument("--geometry-folder", dest="geometry_folder", required=True, help="Path to the geometry folder.")
parser.add_argument("--output-folder", dest="output_folder", required=True, help="Path to the output folder.")
parser.add_argument(
    "--convert-steps",
    dest="convert_steps",
    type=int,
    nargs="+",
    choices=[1, 2, 3],
    default=[1, 2, 3],
    help="Conversion steps to run, for example: --convert-steps 1 2 3",
)
parser.add_argument(
    "--muscle-list",
    dest="muscle_list",
    nargs="+",
    default=None,
    help="Optional muscle names to process, for example: --muscle-list muscle1 muscle2",
)

add_bool_flag(parser, "osim_data_overwrite", True, "Regenerate cached OpenSim state data")
add_bool_flag(parser, "conversion", True, 'Run the "Cvt#" conversion steps')
add_bool_flag(parser, "validation", True, 'Run the "Vlt#" validation steps')
add_bool_flag(parser, "speedy", False, "Use reduced optimization settings for faster runs")
add_bool_flag(parser, "generate_pdf", True, "Generate the validation PDF report")
add_bool_flag(parser, "add_ground_geom", True, "Add a ground geometry to the converted model")
add_bool_flag(
    parser,
    "treat_as_normal_path_point",
    False,
    "Treat moving and conditional path points as normal path points",
)


if __name__ == "__main__":
    args = parser.parse_args()
    O2MPipeline(**vars(args))
