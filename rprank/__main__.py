from os import path as os_path

from brs_utils import (
    init as init_logger,
    build_args_parser,
)
from rplibs import rpPathway

from .Args import add_arguments
from .rprank import rank
from ._version import __version__


def entry_point():

    parser = build_args_parser(
        prog="rprank",
        version=__version__,
        description="Rank pathways",
        m_add_args=add_arguments,
    )
    args = parser.parse_args()

    logger = init_logger(parser, args, __version__)

    # Build the list of pathways to rank (with their filename)
    pathways = {}
    for pathway_fname in args.pathways:
        pathway = rpPathway(infile=pathway_fname, logger=logger)
        pathway_name = pathway.get_id().replace(" ", "_")
        pathways[pathway_name] = {"pathway": pathway, "filename": pathway_fname}

    # Rank pathways
    sorted_pathways = rank(pathways)

    # Rename pathway ids to their filenames
    pathway_names = {
        pathway_name: os_path.basename(pathway["filename"])
        for pathway_name, pathway in pathways.items()
    }
    sorted_renamed_pathways = {
        pathway_names[pathway_name]: score
        for pathway_name, score in sorted_pathways.items()
    }

    # Transform the set of pathways into
    # a string with one pathway per line
    sorted_pathways_str = "\n".join(
        args.delimiter.join(item) for item in sorted_renamed_pathways.items()
    )

    # Printout the result
    print(f"#Name{args.delimiter}Score")
    print(sorted_pathways_str)


if __name__ == "__main__":
    entry_point()
