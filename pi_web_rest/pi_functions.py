import sys
from datetime import datetime

import clr

from .serializers import PIValue, PIRecordedValues

sys.path.append(r'C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0')
clr.AddReference('OSIsoft.AFSDK')

from OSIsoft.AF import *
from OSIsoft.AF.PI import *
from OSIsoft.AF.Asset import *
from OSIsoft.AF.Data import *
from OSIsoft.AF.Time import *
from OSIsoft.AF.UnitsOfMeasure import *


def get_pi_point(tag):
    piServers = PIServers()
    pi_server = piServers.DefaultPIServer;
    try:
        pt = PIPoint.FindPIPoint(pi_server, tag)
    except PIPointInvalidException:
        return None
    return pt


def get_current_values(tags):
    current_values = []
    for tag in tags:
        pt = get_pi_point(tag)
        if pt != None:
                current_value = pt.CurrentValue()
                timestamp = datetime.strptime('{0}'.format(current_value.Timestamp.LocalTime), '%Y/%m/%d %H:%M:%S')
                pi_value = PIValue(tag, timestamp, current_value.Value)
                current_values.append(pi_value)
    return current_values

def get_recorded_values(tags, begin, end='*'):
    recorded_values = []
    timerange = AFTimeRange(begin, end)
    for tag in tags:
        pt = get_pi_point(tag)
        if pt != None:
            recorded = pt.RecordedValues(timerange, AFBoundaryType.Inside, "", False)
            timestamp_values = []
            for event in recorded:
                timestamp = datetime.strptime('{0}'.format(event.Timestamp.LocalTime), '%Y/%m/%d %H:%M:%S')
                timestamp_value = {'timestamp': timestamp, 'value': event.Value}
                timestamp_values.append(timestamp_value)
            pi_recorded = PIRecordedValues(tag, begin, end, timestamp_values)
        recorded_values.append(pi_recorded)
    return recorded_values





# timerange = AFTimeRange("*-3h", "*")
# recorded = pt.RecordedValues(timerange, AFBoundaryType.Inside, "", False)
# print('\nShowing PI Tag RecordedValues from {0}'.format(name))
# for event in recorded:
#     print('{0} value: {1}'.format(event.Timestamp.LocalTime, event.Value))
#
# #interpolatedvalues
# span = AFTimeSpan.Parse("1h")
# interpolated = pt.InterpolatedValues(timerange, span, "", False)
# print('\nShowing PI Tag InterpolatedValues from {0}'.format(name))
# for event in interpolated:
#     print('{0} value: {1}'.format(event.Timestamp.LocalTime, event.Value))
#
# #summariesvalues
# summaries = pt.Summaries(timerange, span, AFSummaryTypes.Average, AFCalculationBasis.TimeWeighted, AFTimestampCalculation.Auto)
# print('\nShowing PI Tag SummariesValues(Average) from {0}'.format(name))
# for summary in summaries:
#     for event in summary.Value:
#         print('{0} value: {1}'.format(event.Timestamp.LocalTime, event.Value))
