from pybirdai.ldm_models import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime

class F_18_00_a_REF_FINREP_3_0_UnionItem:
	base = None #F_18_00_a_REF_FINREP_3_0_Base
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.base.GRSS_CRRYNG_AMNT()
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.base.RPYMNT_RGHTS()
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.base.INSTTTNL_SCTR()
	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.base.ENTRPRS_SZ()
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.base.PRPS()
	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.IMPRMNT_STTS()
	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.PRFRMNG_STTS()
	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.base.DFLT_STTS()
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.base.SBJCT_IMPRMNT_INDCTR()

class F_18_00_a_REF_FINREP_3_0_Base:
	def GRSS_CRRYNG_AMNT() -> int:
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def RPYMNT_RGHTS() -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def ENTRPRS_SZ() -> str:
		''' return string from SZ enumeration '''
		pass
	def PRPS() -> str:
		''' return string from PRPS enumeration '''
		pass
	def IMPRMNT_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def PRFRMNG_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def DFLT_STTS() -> str:
		''' return string from CRDT_QLTY enumeration '''
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass

class F_18_00_a_REF_FINREP_3_0_UnionTable :
	F_18_00_a_REF_FINREP_3_0_UnionItems = [] # F_18_00_a_REF_FINREP_3_0_UnionItem []
	F_18_00_a_REF_FINREP_3_0_Debt_securities_Table = None # Debt_securities
	F_18_00_a_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None # Non_Negotiable_bonds
	F_18_00_a_REF_FINREP_3_0_Loans_and_advances_Table = None # Loans_and_advances
	def calc_F_18_00_a_REF_FINREP_3_0_UnionItems(self) -> list[F_18_00_a_REF_FINREP_3_0_UnionItem] :
		items = [] # F_18_00_a_REF_FINREP_3_0_UnionItem []
		for item in F_18_00_a_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess:
			newItem = F_18_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in F_18_00_a_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss:
			newItem = F_18_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in F_18_00_a_REF_FINREP_3_0_Loans_and_advances_Table.Loans_and_advancess:
			newItem = F_18_00_a_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_18_00_a_REF_FINREP_3_0_UnionItems.extend(self.calc_F_18_00_a_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Debt_securities(F_18_00_a_REF_FINREP_3_0_Base):
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	def GRSS_CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.GRSS_CRRYNG_AMNT
	def IMPRMNT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS
	def IMPRMNT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS
	def PRFRMNG_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS
	def PRFRMNG_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS
	def DFLT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS
	def DFLT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	def HLD_SL_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR

class Non_Negotiable_bonds(F_18_00_a_REF_FINREP_3_0_Base):
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	def GRSS_CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.GRSS_CRRYNG_AMNT
	def IMPRMNT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS
	def IMPRMNT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS
	def PRFRMNG_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS
	def PRFRMNG_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS
	def DFLT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.IMPRMNT_STTS
	def DFLT_STTS(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.INTL_IMPRMNT_STTS
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	def HLD_SL_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.HLD_SL_INDCTR
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	def ENTRPRS_SZ(self):
		return self.PRTY.ENTRPRS_SZ
	def IMPRMNT_STTS(self):
		return self.PRTY.DFLT_STTS
	def IMPRMNT_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	def PRFRMNG_STTS(self):
		return self.PRTY.DFLT_STTS
	def PRFRMNG_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	def DFLT_STTS(self):
		return self.PRTY.DFLT_STTS
	def DFLT_STTS(self):
		return self.PRTY.PRFRMNG_STTS

class Loans_and_advances(F_18_00_a_REF_FINREP_3_0_Base):
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
	def IMPRMNT_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.DFLT_STTS
	def IMPRMNT_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.DFLT_STTS_DRVD
	def IMPRMNT_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.IMPRMNT_STTS
	def IMPRMNT_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.INTL_IMPRMNT_STTS
	def IMPRMNT_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.PRFRMNG_STTS
	def PRFRMNG_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.DFLT_STTS
	def PRFRMNG_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.DFLT_STTS_DRVD
	def PRFRMNG_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.IMPRMNT_STTS
	def PRFRMNG_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.INTL_IMPRMNT_STTS
	def PRFRMNG_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.PRFRMNG_STTS
	def DFLT_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.DFLT_STTS
	def DFLT_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.DFLT_STTS_DRVD
	def DFLT_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.IMPRMNT_STTS
	def DFLT_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.INTL_IMPRMNT_STTS
	def DFLT_STTS(self):
		return self.ABSTRCT_INSTRMNT_RL.PRFRMNG_STTS
	def ACCNTNG_CLSSFCTN(self):
		return self.ABSTRCT_INSTRMNT_RL.ACCNTNG_CLSSFCTN
	def HLD_SL_INDCTR(self):
		return self.ABSTRCT_INSTRMNT_RL.HLD_SL_INDCTR
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.ABSTRCT_INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	PRTY = None # PRTY
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	def ENTRPRS_SZ(self):
		return self.PRTY.ENTRPRS_SZ
	def IMPRMNT_STTS(self):
		return self.PRTY.DFLT_STTS
	def IMPRMNT_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	def PRFRMNG_STTS(self):
		return self.PRTY.DFLT_STTS
	def PRFRMNG_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	def DFLT_STTS(self):
		return self.PRTY.DFLT_STTS
	def DFLT_STTS(self):
		return self.PRTY.PRFRMNG_STTS
	pass

class F_18_00_a_REF_FINREP_3_0_Debt_securities_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	Debt_securitiess = []# Debt_securities[]
	def calc_Debt_securitiess(self) :
		items = [] # Debt_securities[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Debt_securitiess.extend(self.calc_Debt_securitiess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_18_00_a_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
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


class F_18_00_a_REF_FINREP_3_0_Loans_and_advances_Table:
	INSTRMNT_Table = None # INSTRMNT
	ABSTRCT_INSTRMNT_RL_Table = None # ABSTRCT_INSTRMNT_RL
	PRTY_Table = None # PRTY
	Loans_and_advancess = []# Loans_and_advances[]
	def calc_Loans_and_advancess(self) :
		items = [] # Loans_and_advances[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Loans_and_advancess.extend(self.calc_Loans_and_advancess())
		CSVConverter.persist_object_as_csv(self,True)
		return None
