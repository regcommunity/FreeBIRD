from pybirdai.bird_data_model import *
from .output_tables import *
from pybirdai.process_steps.pybird.orchestration import Orchestration

class Cell_F_05_01_REF_FINREP_3_0_152589_REF:
	F_05_01_REF_FINREP_3_0_Table = None
	F_05_01_REF_FINREP_3_0s = []

	def metric_value(self):
		total = 0
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total

	def calc_referenced_items(self):
		items = self.F_05_01_REF_FINREP_3_0_Table.F_05_01_REF_FINREP_3_0s
		for item in items:
			filter_passed = True
			if 				(item.PRPS() == '7')  or \
				(item.PRPS() == '9')  or \
				(item.PRPS() == '6')  or \
				(item.PRPS() == '8')  or \
				(item.PRPS() == '4')  or \
				(item.PRPS() == '12')  or \
				(item.PRPS() == '13')  or \
				(item.PRPS() == '1')  or \
				(item.PRPS() == '19')  or \
				False:
				print("item.PRPS() failed: " + item.PRPS())
			else:
				filter_passed = False
			if 				(item.ACCNTNG_CLSSFCTN() == '6')  or \
				(item.ACCNTNG_CLSSFCTN() == '14')  or \
				(item.ACCNTNG_CLSSFCTN() == '45')  or \
				(item.ACCNTNG_CLSSFCTN() == '9')  or \
				(item.ACCNTNG_CLSSFCTN() == '7')  or \
				(item.ACCNTNG_CLSSFCTN() == '8')  or \
				(item.ACCNTNG_CLSSFCTN() == '41')  or \
				(item.ACCNTNG_CLSSFCTN() == '4')  or \
				(item.ACCNTNG_CLSSFCTN() == '47')  or \
				(item.ACCNTNG_CLSSFCTN() == '77')  or \
				(item.ACCNTNG_CLSSFCTN() == '76')  or \
				(item.ACCNTNG_CLSSFCTN() == '74')  or \
				(item.ACCNTNG_CLSSFCTN() == '73')  or \
				False:
				print("item.ACCNTNG_CLSSFCTN() failed: " + item.ACCNTNG_CLSSFCTN())
			else:
				filter_passed = False
			if 				(item.HLD_SL_INDCTR() == '2')  or \
				False:
				print("item.HLD_SL_INDCTR() failed: " + item.HLD_SL_INDCTR())
			else:
				filter_passed = False
			if 				(item.INSTTTNL_SCTR() == 'S128')  or \
				(item.INSTTTNL_SCTR() == 'S129')  or \
				(item.INSTTTNL_SCTR() == 'S121')  or \
				(item.INSTTTNL_SCTR() == 'S123')  or \
				(item.INSTTTNL_SCTR() == 'S122_B2')  or \
				(item.INSTTTNL_SCTR() == 'S122_B1')  or \
				(item.INSTTTNL_SCTR() == 'S122_A_1')  or \
				(item.INSTTTNL_SCTR() == 'S122_A_2')  or \
				(item.INSTTTNL_SCTR() == 'S124')  or \
				(item.INSTTTNL_SCTR() == 'S126')  or \
				(item.INSTTTNL_SCTR() == 'S125_I')  or \
				(item.INSTTTNL_SCTR() == 'S125_C')  or \
				(item.INSTTTNL_SCTR() == 'S125_B')  or \
				(item.INSTTTNL_SCTR() == 'S125_D')  or \
				(item.INSTTTNL_SCTR() == 'S125_E')  or \
				(item.INSTTTNL_SCTR() == 'S125_A')  or \
				(item.INSTTTNL_SCTR() == 'S127')  or \
				(item.INSTTTNL_SCTR() == 'S1312')  or \
				(item.INSTTTNL_SCTR() == 'S1313')  or \
				(item.INSTTTNL_SCTR() == 'S1311')  or \
				(item.INSTTTNL_SCTR() == 'S1314')  or \
				(item.INSTTTNL_SCTR() == 'S15')  or \
				(item.INSTTTNL_SCTR() == 'S11')  or \
				(item.INSTTTNL_SCTR() == 'S14_B')  or \
				(item.INSTTTNL_SCTR() == 'S14_A')  or \
				False:
				print("item.INSTTTNL_SCTR() failed: " + item.INSTTTNL_SCTR())
			else:
				filter_passed = False
			if 				(item.RPYMNT_RGHTS() == '2')  or \
				False:
				print("item.RPYMNT_RGHTS() failed: " + item.RPYMNT_RGHTS())
			else:
				filter_passed = False
			if 				(item.PRJCT_FNNC_LN() == '1')  or \
				(item.PRJCT_FNNC_LN() == '2')  or \
				False:
				print("item.PRJCT_FNNC_LN() failed: " + item.PRJCT_FNNC_LN())
			else:
				filter_passed = False
			if filter_passed:
				print("self.F_05_01_REF_FINREP_3_0s.append(item)")
				self.F_05_01_REF_FINREP_3_0s.append(item)
	def init(self):
		Orchestration().init(self)
		self.calc_referenced_items()
		return None
