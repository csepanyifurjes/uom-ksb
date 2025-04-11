from su_control import ControlUnit
from su_explain import ExplainUnit
from su_report import ReportUnit
from su_teach import TeachUnit


class NullUnit(object):
    """ Object to follow the NULL pattern """

    def __init__(self):
        self.health = "Not implemented"

    def get_health(self):
        return self.health


KSB_UNITS = {
    'report': {
        'class': ReportUnit
    },
    'explain': {
        'class': ExplainUnit
    },
    'control': {
        'class': ControlUnit
    },
    'teach': {
        'class': TeachUnit
    },
    'future': {
        'class': NullUnit
    }
}
