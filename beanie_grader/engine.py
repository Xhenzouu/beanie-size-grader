import pandas as pd

def build_graded_table(config, base_overrides=None):
    """
    Generic grading engine.

    Args:
        config (dict): Product configuration.
        base_overrides (dict, optional): Override base values per measurement.

    Returns:
        pandas.DataFrame
    """
    sizes = config["sizes"]
    measurements = config["measurements"]
    base_overrides = base_overrides or {}

    df = pd.DataFrame({"Size": sizes})

    for name, spec in measurements.items():
        base_value = base_overrides.get(name, spec["base"])
        offsets = spec["offsets"]

        df[name] = [
            round(base_value + offset, 1)
            for offset in offsets
        ]

    return df

print("DEBUG: engine.build_graded_table loaded")
