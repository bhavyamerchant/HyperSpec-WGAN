# Copyright 2021 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.

"""Pipeline structure for data visualization tasks."""

from kedro.pipeline.node import node
from kedro.pipeline.pipeline import Pipeline

from .nodes import plot_pca, plot_tsne


def data_visualization_pipeline() -> Pipeline:
    """Create the data visualization pipeline."""
    return Pipeline(
        nodes=[
            node(
                func=plot_pca,
                inputs={
                    "x": "model_output_pca_x",
                    "y": "primary_classified_y",
                    "variance": "model_output_pca_variance",
                    "metadata": "params:metadata",
                    "kwargs": "params:plot_pca",
                },
                outputs="reporting_pca",
                name="plot-pca",
                tags="pca",
            ),
            node(
                func=plot_tsne,
                inputs={
                    "x": "model_output_tsne_x",
                    "y": "primary_classified_y",
                    "metadata": "params:metadata",
                    "kwargs": "params:plot_tsne",
                },
                outputs="reporting_tsne",
                name="plot-tsne",
                tags="tsne",
            ),
        ]
    )
