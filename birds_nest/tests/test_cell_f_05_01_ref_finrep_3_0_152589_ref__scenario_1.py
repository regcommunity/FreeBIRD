import os
import logging
os.environ['DJANGO_SETTINGS_MODULE'] = 'birds_nest.settings'
from django.conf import settings
import pytest
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from pybirdai.entry_points.execute_datapoint import RunExecuteDataPoint
from pybirdai.process_steps.pybird.execute_datapoint import ExecuteDataPoint
from pybirdai.process_steps.filter_code.report_cells import Cell_F_05_01_REF_FINREP_3_0_152589_REF

def test_execute_datapoint(value: int=83491250):
    data_point_id = 'F_05_01_REF_FINREP_3_0_152589_REF'
    result = RunExecuteDataPoint.run_execute_data_point(data_point_id)
    ExecuteDataPoint.delete_lineage_data()
    assert result == str(value)

def test_delete_lineage():
    ExecuteDataPoint.delete_lineage_data()
    base_dir = settings.BASE_DIR
    lineage_dir = os.path.join(base_dir, 'results', 'lineage')
    assert len(os.listdir(lineage_dir)) == 1

def test_cell_metric():
    cell = Cell_F_05_01_REF_FINREP_3_0_152589_REF()
    cell.init()
    result = cell.metric_value()
    ExecuteDataPoint.delete_lineage_data()
    assert isinstance(result, (int, float))

def test_cell_filter():
    cell = Cell_F_05_01_REF_FINREP_3_0_152589_REF()
    cell.init()
    ExecuteDataPoint.delete_lineage_data()
    assert isinstance(cell.F_05_01_REF_FINREP_3_0s, list)