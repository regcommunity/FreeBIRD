from pybirdai.ldm_models import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime

class F_05_01_REF_FINREP_3_0_UnionItem:
	base = None #F_05_01_REF_FINREP_3_0_Base
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.base.GRSS_CRRYNG_AMNT()
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.base.PRPS()
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.base.INSTTTNL_SCTR()
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.base.RPYMNT_RGHTS()
	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.base.PRJCT_FNNC_LN()
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()

class F_05_01_REF_FINREP_3_0_Base:
	def GRSS_CRRYNG_AMNT() -> int:
		pass
	def PRPS() -> str:
		''' return string from PRPS enumeration '''
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def RPYMNT_RGHTS() -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		pass
	def PRJCT_FNNC_LN() -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		pass
	def CRRYNG_AMNT() -> int:
		pass

class F_05_01_REF_FINREP_3_0_UnionTable :
	F_05_01_REF_FINREP_3_0_UnionItems = [] # F_05_01_REF_FINREP_3_0_UnionItem []
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None # Non_Negotiable_bonds
	F_05_01_REF_FINREP_3_0_Loans_and_advances_Table = None # Loans_and_advances
	def calc_F_05_01_REF_FINREP_3_0_UnionItems(self) -> list[F_05_01_REF_FINREP_3_0_UnionItem] :
		items = [] # F_05_01_REF_FINREP_3_0_UnionItem []
		for item in F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in F_05_01_REF_FINREP_3_0_Loans_and_advances_Table.Loans_and_advancess:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0_UnionItems.extend(self.calc_F_05_01_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Non_Negotiable_bonds(F_05_01_REF_FINREP_3_0_Base):
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	def GRSS_CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.GRSS_CRRYNG_AMNT
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	def HLD_SL_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	PRTY = None # PRTY
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR

class Loans_and_advances(F_05_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_ORGN
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	def RPYMNT_RGHTS(self):
		return self.INSTRMNT.RPYMNT_RGHTS
	ABSTRCT_INSTRMNT_RL = None # ABSTRCT_INSTRMNT_RL
	def GRSS_CRRYNG_AMNT(self):
		return self.ABSTRCT_INSTRMNT_RL.GRSS_CRRYNG_AMNT
	def PRPS(self):
		return self.ABSTRCT_INSTRMNT_RL.PRPS
	def ACCNTNG_CLSSFCTN(self):
		return self.ABSTRCT_INSTRMNT_RL.ACCNTNG_CLSSFCTN
	def HLD_SL_INDCTR(self):
		return self.ABSTRCT_INSTRMNT_RL.HLD_SL_INDCTR
	def PRJCT_FNNC_LN(self):
		return self.ABSTRCT_INSTRMNT_RL.PRJCT_FNNC_LN
	def CRRYNG_AMNT(self):
		return self.ABSTRCT_INSTRMNT_RL.CRRYNG_AMNT
	PRTY = None # PRTY
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	CLLTRL = None # CLLTRL
	

class F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	PRTY_Table = None # PRTY
	Non_Negotiable_bondss = []# Non_Negotiable_bonds[]
	def calc_Non_Negotiable_bondss(self) :
		items = [] # Non_Negotiable_bonds[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Non_Negotiable_bondss.extend(self.calc_Non_Negotiable_bondss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Loans_and_advances_Table:
	INSTRMNT_Table = None # INSTRMNT
	ABSTRCT_INSTRMNT_RL_Table = None # ABSTRCT_INSTRMNT_RL
	PRTY_Table = None # PRTY
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	Loans_and_advancess = []# Loans_and_advances[]
	def calc_Loans_and_advancess(self) :
		items = [] # Loans_and_advances[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		from pybirdai.ldm_models import INSTRMNT
		for abstractInstrument in self.ABSTRCT_INSTRMNT_RL_Table:
			typeInst = abstractInstrument.theINSTRMNT.TYP_INSTRMNT
			#if (typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['140']) or \
			#		(typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['1022'] ) or \
			#	(typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['51'] ) or \
			#	(typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['80'] ) or \
			#	(typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['12'] ) or \
			#	(typeInst == INSTRMNT.TYP_INSTRMNT_INPT_domain['522'] ):
			if (typeInst == '140') or \
				(typeInst == '1022' ) or \
				(typeInst == '51' ) or \
				(typeInst == '80' ) or \
				(typeInst == '12' ) or \
				(typeInst == '522' ):
				
				newItem = Loans_and_advances()
				newItem.ABSTRCT_INSTRMNT_RL = abstractInstrument
				newItem.INSTRMNT = abstractInstrument.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.Loans_and_advancess.extend(self.calc_Loans_and_advancess())
		CSVConverter.persist_object_as_csv(self,True)
		return None