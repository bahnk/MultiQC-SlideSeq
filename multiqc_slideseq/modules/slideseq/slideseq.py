
import logging

from multiqc.modules.base_module import BaseMultiqcModule
from multiqc.plots import bargraph

# Initialise the logger
log = logging.getLogger(__name__)


class MultiqcModule(BaseMultiqcModule):
    def __init__(self):
        # Initialise the parent object
        super(MultiqcModule, self).__init__(
            name="Slide-seq",
            anchor="slideseq",
            href="https://www.nature.com/articles/s41587-020-0739-1",
            info="is a spatial transcriptomics technology,"
            " created by Sam Rodriques at the Broad Institute in Cambridge.",
        )

        self.add_section(
            name="Read 1 length",
            anchor="slideseq_read1_length",
            description="Check that read 1 is long enought to contain barcode and UMI",
            helptext="""
            The first step is to throw away the read pairs whose read 1 is too shortself.
            For example, if you have the following read structure 8C18U6C9M, then you need at least 41 bp.
            """,
            plot=bargraph.plot({"sample1": {"x": 45, "y":55, "z": 70}, "sample2": {"x": 30, "y": 70, "z": 60}}),
        )
