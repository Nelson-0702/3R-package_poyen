import csv
from collections import defaultdict

import click


def mean_per_device(input_file):
    counts = defaultdict(list)

    with open(input_file, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            device = row["device"]
            daily_count = float(row["daily_count"])
            counts[device].append(daily_count)

    return {
        device: sum(values) 
        for device, values in counts.items()
    }


@click.command()
@click.option("--input", "input_file", required=True,
              type=click.Path(exists=True))
def device_analysis_cli(input_file):
    results = mean_per_device(input_file)

    for device, mean in sorted(results.items()):
        click.echo(f"{device}  {mean:.2f}")
