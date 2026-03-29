from enum import Enum


class RollConv(Enum):
    FOLLOWING = "FOLL"
    MODIFIED_FOLLOWING = "MODF"
    PRECEDING = "PREC"
    MODIFIED_PRECEDING = "MODP"
    UNADJUSTED = "NONE"
    