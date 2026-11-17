"""Record beta-v2/hybrid snapshots explicitly; this never routes the main model."""
import argparse
from pathlib import Path
from beta_engine import make_snapshot, read, write_new


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, required=True)
    parser.add_argument('--inputs', type=Path, required=True)
    parser.add_argument('--selection', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--reconstruct', action='store_true')
    parser.add_argument('--no-mc', action='store_true')
    args = parser.parse_args()
    mode = 'retrospective_reconstruction' if args.reconstruct else 'forecast'
    selection = read(args.selection)
    snapshot = make_snapshot(read(args.package), read(args.inputs), selection['selected_policy'],
                             mode=mode, include_mc=not args.no_mc)
    write_new(args.output, snapshot)
    print(f"Saved {mode}: {snapshot['snapshot_id']} ({len(snapshot['rows'])} fixtures)")


if __name__ == '__main__':
    main()
