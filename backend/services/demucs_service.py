from pathlib import Path
from demucs.api import Separator


def demucs_service(audio_path: Path, out_dir: Path) -> Path:
    separator = Separator()
    separator.separate_files([str(audio_path)], output_dir=out_dir)
    return out_dir / audio_path.stem
