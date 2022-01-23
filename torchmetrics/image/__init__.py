# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from torchmetrics.image.psnr import PSNR, PeakSignalNoiseRatio  # noqa: F401
from torchmetrics.image.ssim import (  # noqa: F401
    SSIM,
    MultiScaleStructuralSimilarityIndexMeasure,
    StructuralSimilarityIndexMeasure,
)
from torchmetrics.utilities.imports import _LPIPS_AVAILABLE, _TORCH_FIDELITY_AVAILABLE
from torchmetrics.utilities.registry import register_compute_group

if _TORCH_FIDELITY_AVAILABLE:
    from torchmetrics.image.fid import FID, FrechetInceptionDistance  # noqa: F401
    from torchmetrics.image.inception import IS, InceptionScore  # noqa: F401
    from torchmetrics.image.kid import KID, KernelInceptionDistance  # noqa: F401
    
    register_compute_group(FrechetInceptionDistance, KernelInceptionDistance)  # todo: what 

if _LPIPS_AVAILABLE:
    from torchmetrics.image.lpip import LPIPS, LearnedPerceptualImagePatchSimilarity  # noqa: F401
