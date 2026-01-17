import argparse
from beanie_grader.beanie_config import PRODUCT_CONFIG
from beanie_grader.config import load_config
from beanie_grader.commands import run_command, validate_command, list_command

def parse_args():
    parser = argparse.ArgumentParser(
        description="Config-driven product sizing and grading automation"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # RUN command
    run_parser = subparsers.add_parser(
        "run",
        help="Run grading pipeline using a product config"
    )

    run_parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to product config YAML"
    )

    run_parser.add_argument(
        "--output",
        type=str,
        default="graded_output.xlsx",
        help="Output Excel file"
    )

    # VALIDATE command
    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate a product config YAML"
    )

    validate_parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to product config YAML"
    )

    # LIST command
    list_parser = subparsers.add_parser(
        "list",
        help="List available config files"
    )

    # Parse known args first to get --config for run/validate, then load config for run
    args, remaining = parser.parse_known_args()
    if args.command == "run":
        config = load_config(args.config)
        # Dynamically add --base_* arguments based on loaded config's measurements
        for name, spec in config["measurements"].items():
            arg_name = name.lower().replace(" ", "_").replace("/", "").replace("(", "").replace(")", "")
            run_parser.add_argument(
                f"--base_{arg_name}",
                type=float,
                default=spec["base"],
                help=f"Override base value for {name}"
            )

    # Re-parse all args now that dynamic ones are added (for run)
    return parser.parse_args()

def main():
    args = parse_args()

    if args.command == "run":
        run_command(args)
    elif args.command == "validate":
        validate_command(args)
    elif args.command == "list":
        list_command(args)

if __name__ == "__main__":
    main()