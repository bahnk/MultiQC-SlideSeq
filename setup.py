
from setuptools import setup, find_packages

setup(
    name = "multiqc_slideseq",
    version = "0.1",
    author = "Nourdine Bah",
    author_email = "nourdinebah@gmail.com",
    description = "MultiQC plugin for Slide-seq metrics",
    packages = find_packages(),
    include_package_data = True,
    install_requires = ["multiqc>=1.14"],
    entry_points = {
        "multiqc.modules.v1": [
            "slideseq = multiqc_slideseq.modules.slideseq.slideseq:MultiqcModule"
        ]
	}
)
