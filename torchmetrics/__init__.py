r"""Root package info."""
import logging as __logging
import os

from torchmetrics.__about__ import *  # noqa: F403

_logger = __logging.getLogger("torchmetrics")
_logger.addHandler(__logging.StreamHandler())
_logger.setLevel(__logging.INFO)

_PACKAGE_ROOT = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.dirname(_PACKAGE_ROOT)

from torchmetrics import functional  # noqa: E402
from torchmetrics.aggregation import CatMetric, MaxMetric, MeanMetric, MinMetric, SumMetric  # noqa: E402
from torchmetrics.audio import (  # noqa: E402
    PIT,
    SDR,
    SI_SDR,
    SI_SNR,
    SNR,
    PermutationInvariantTraining,
    ScaleInvariantSignalDistortionRatio,
    ScaleInvariantSignalNoiseRatio,
    SignalDistortionRatio,
    SignalNoiseRatio,
)
from torchmetrics.classification import (  # noqa: E402
    AUC,
    AUROC,
    F1,
    ROC,
    Accuracy,
    AveragePrecision,
    BinnedAveragePrecision,
    BinnedPrecisionRecallCurve,
    BinnedRecallAtFixedPrecision,
    CalibrationError,
    CohenKappa,
    ConfusionMatrix,
    F1Score,
    FBeta,
    FBetaScore,
    HammingDistance,
    Hinge,
    HingeLoss,
    IoU,
    JaccardIndex,
    KLDivergence,
    MatthewsCorrcoef,
    MatthewsCorrCoef,
    Precision,
    PrecisionRecallCurve,
    Recall,
    Specificity,
    StatScores,
)
from torchmetrics.collections import MetricCollection  # noqa: E402
from torchmetrics.image import (  # noqa: E402
    PSNR,
    SSIM,
    MultiScaleStructuralSimilarityIndexMeasure,
    PeakSignalNoiseRatio,
    StructuralSimilarityIndexMeasure,
)
from torchmetrics.metric import Metric  # noqa: E402
from torchmetrics.regression import (  # noqa: E402
    CosineSimilarity,
    ExplainedVariance,
    MeanAbsoluteError,
    MeanAbsolutePercentageError,
    MeanSquaredError,
    MeanSquaredLogError,
    PearsonCorrcoef,
    PearsonCorrCoef,
    R2Score,
    SpearmanCorrcoef,
    SpearmanCorrCoef,
    SymmetricMeanAbsolutePercentageError,
    TweedieDevianceScore,
)
from torchmetrics.retrieval import (  # noqa: E402
    RetrievalFallOut,
    RetrievalHitRate,
    RetrievalMAP,
    RetrievalMRR,
    RetrievalNormalizedDCG,
    RetrievalPrecision,
    RetrievalRecall,
    RetrievalRPrecision,
)
from torchmetrics.text import (  # noqa: E402
    BLEUScore,
    CharErrorRate,
    CHRFScore,
    ExtendedEditDistance,
    MatchErrorRate,
    SacreBLEUScore,
    SQuAD,
    TranslationEditRate,
    WordErrorRate,
    WordInfoLost,
    WordInfoPreserved,
)
from torchmetrics.wrappers import BootStrapper, MetricTracker, MinMaxMetric, MultioutputWrapper  # noqa: E402

from torchmetrics.utilities.registry import register_compute_group

register_compute_group(F1, FBeta, Recall, Precision, Specificity, StatScores)
register_compute_group(AUROC, AveragePrecision, PrecisionRecallCurve, ROC)
register_compute_group(BinnedPrecisionRecallCurve, BinnedAveragePrecision)
register_compute_group(CohenKappa, ConfusionMatrix, IoU, MatthewsCorrcoef)
register_compute_group(CosineSimilarity, SpearmanCorrcoef)
register_compute_group(
    RetrievalMAP, RetrievalMRR, RetrievalFallOut, RetrievalNormalizedDCG, RetrievalPrecision, RetrievalRecall
)


__all__ = [
    "functional",
    "Accuracy",
    "AUC",
    "AUROC",
    "AveragePrecision",
    "BinnedAveragePrecision",
    "BinnedPrecisionRecallCurve",
    "BinnedRecallAtFixedPrecision",
    "BLEUScore",
    "BootStrapper",
    "CalibrationError",
    "CatMetric",
    "CHRFScore",
    "CohenKappa",
    "ConfusionMatrix",
    "CosineSimilarity",
    "TweedieDevianceScore",
    "ExplainedVariance",
    "ExtendedEditDistance",
    "F1",
    "F1Score",
    "FBeta",
    "FBetaScore",
    "HammingDistance",
    "Hinge",
    "HingeLoss",
    "JaccardIndex",
    "KLDivergence",
    "MatthewsCorrcoef",
    "MatthewsCorrCoef",
    "MaxMetric",
    "MeanAbsoluteError",
    "MeanAbsolutePercentageError",
    "MeanMetric",
    "MeanSquaredError",
    "MeanSquaredLogError",
    "Metric",
    "MetricCollection",
    "MetricTracker",
    "MinMaxMetric",
    "MinMetric",
    "MultioutputWrapper",
    "MultiScaleStructuralSimilarityIndexMeasure",
    "PearsonCorrcoef",
    "PearsonCorrCoef",
    "PermutationInvariantTraining",
    "PIT",
    "Precision",
    "PrecisionRecallCurve",
    "PSNR",
    "PeakSignalNoiseRatio",
    "R2Score",
    "Recall",
    "RetrievalFallOut",
    "RetrievalHitRate",
    "RetrievalMAP",
    "RetrievalMRR",
    "RetrievalNormalizedDCG",
    "RetrievalPrecision",
    "RetrievalRecall",
    "RetrievalRPrecision",
    "ROC",
    "SacreBLEUScore",
    "SDR",
    "SignalDistortionRatio",
    "ScaleInvariantSignalDistortionRatio",
    "SI_SDR",
    "SI_SNR",
    "ScaleInvariantSignalNoiseRatio",
    "SignalNoiseRatio",
    "SNR",
    "SpearmanCorrcoef",
    "SpearmanCorrCoef",
    "Specificity",
    "SQuAD",
    "SSIM",
    "StructuralSimilarityIndexMeasure",
    "StatScores",
    "SumMetric",
    "SymmetricMeanAbsolutePercentageError",
    "WER",
    "TranslationEditRate",
    "WordErrorRate",
    "CharErrorRate",
    "MatchErrorRate",
    "WordInfoLost",
    "WordInfoPreserved",
]
