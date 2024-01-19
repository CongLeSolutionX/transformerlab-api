# This plugin exports a model to MLX format so you can interact and train on a MBP with Apple Silicon
import os
import subprocess
import sqlite3
import argparse
import sys

from mlx_lm import convert

# TODO: Connect to the LLM Lab database (to update job status)
# llmlab_root_dir = os.getenv('LLM_LAB_ROOT_PATH')
# db = sqlite3.connect(llmlab_root_dir + "/workspace/llmlab.sqlite3")

# Get all arguments provided to this script using argparse
# NOTE: This takes an adaptor name but doesn't do anything with the adaptor at this time
parser = argparse.ArgumentParser(description='Convert a model to MLX format.')
parser.add_argument('--model_name', default='gpt-j-6b', type=str, help='Name of model to export.')
parser.add_argument('--model_architecture', default='hf-causal', type=str, help='Type of model to export.')
parser.add_argument('--experiment_name', default='', type=str, help='Name of experiment.')
parser.add_argument('--model_adaptor', default='', type=str, help='Name of model adaptor.')
args, unknown = parser.parse_known_args()

# TODO: Verify that the model uses a supported format
# According to MLX docs (as of Jan 16/24) supported formats are:
# Mistral, Llama, Phi-2
model_architecture = args.model_architecture

# Directory to run conversion subprocess
root_dir = os.environ.get("LLM_LAB_ROOT_PATH")
plugin_dir = f"{root_dir}/workspace/experiments/{args.experiment_name}/plugins/mlx_exporter"

# Directory to output quantized model
output_path = f"{root_dir}/workspace/models"

# Call MLX Convert function
print("Exporting", args.model_name, "to MLX format in", output_dir)
subprocess.Popen(
    ["python", '-m',  'mlx_lm.convert', 
        '--hf-path', args.model_name, '--mlx-path', output_path, '-q'],
    cwd=plugin_dir,
)
