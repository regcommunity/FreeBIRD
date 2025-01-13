from pybirdai.bird_data_model import *
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
	F_05_01_REF_FINREP_3_0_Other_Loans_Table = None # Other_Loans
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None # Non_Negotiable_bonds
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None # Credit_card_debt
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None # Trade_receivables
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None # Finance_leases
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None # Advances_that_are_not_loans
	def calc_F_05_01_REF_FINREP_3_0_UnionItems(self) -> list[F_05_01_REF_FINREP_3_0_UnionItem] :
		items = [] # F_05_01_REF_FINREP_3_0_UnionItem []
		for item in F_05_01_REF_FINREP_3_0_Other_Loans_Table.Other_Loanss:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss:
			newItem = F_05_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0_UnionItems.extend(self.calc_F_05_01_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Other_Loans(F_05_01_REF_FINREP_3_0_Base):
	pass
	BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT = None # BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT
	def ACCNTNG_CLSSFCTN(self):
		return self.BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN
	def CRRYNG_AMNT(self):
		return self.BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT.CRRYNG_AMNT
	PRTY = None # PRTY
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR

class Non_Negotiable_bonds(F_05_01_REF_FINREP_3_0_Base):
	pass
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT

class Credit_card_debt(F_05_01_REF_FINREP_3_0_Base):
	pass

class Trade_receivables(F_05_01_REF_FINREP_3_0_Base):
	TRD_RCVBL = None # TRD_RCVBL
	def TYP_INSTRMNT(self):
		return self.TRD_RCVBL.TRD_RCVBL_TYP
	def TYP_INSTRMNT(self):
		return self.TRD_RCVBL.TRD_RCVBL_TYP
	def TYP_INSTRMNT(self):
		return self.TRD_RCVBL.TRD_RCVBL_TYP
	BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT = None # BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT
	def ACCNTNG_CLSSFCTN(self):
		return self.BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN
	def CRRYNG_AMNT(self):
		return self.BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT.CRRYNG_AMNT

class Finance_leases(F_05_01_REF_FINREP_3_0_Base):
	pass

class Advances_that_are_not_loans(F_05_01_REF_FINREP_3_0_Base):
	ADVNC = None # ADVNC
	def TYP_INSTRMNT(self):
		return self.ADVNC.ADVNC_TYP
	def TYP_INSTRMNT(self):
		return self.ADVNC.ADVNC_TYP
	def TYP_INSTRMNT(self):
		return self.ADVNC.ADVNC_TYP
	def TYP_INSTRMNT(self):
		return self.ADVNC.ADVNC_TYP
	BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT = None # BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT
	def ACCNTNG_CLSSFCTN(self):
		return self.BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN
	def CRRYNG_AMNT(self):
		return self.BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT.CRRYNG_AMNT

class F_05_01_REF_FINREP_3_0_Other_Loans_Table:
	BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT_Table = None # BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT
	PRTY_Table = None # PRTY
	Other_Loanss = []# Other_Loans[]
	def calc_Other_Loanss(self) :
		items = [] # Other_Loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Other_Loanss.extend(self.calc_Other_Loanss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT_Table = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
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


class F_05_01_REF_FINREP_3_0_Credit_card_debt_Table:
	Credit_card_debts = []# Credit_card_debt[]
	def calc_Credit_card_debts(self) :
		items = [] # Credit_card_debt[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Credit_card_debts.extend(self.calc_Credit_card_debts())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Trade_receivables_Table:
	TRD_RCVBL_Table = None # TRD_RCVBL
	BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT_Table = None # BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT
	Trade_receivabless = []# Trade_receivables[]
	def calc_Trade_receivabless(self) :
		items = [] # Trade_receivables[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Trade_receivabless.extend(self.calc_Trade_receivabless())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Finance_leases_Table:
	Finance_leasess = []# Finance_leases[]
	def calc_Finance_leasess(self) :
		items = [] # Finance_leases[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Finance_leasess.extend(self.calc_Finance_leasess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table:
	ADVNC_Table = None # ADVNC
	BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT_Table = None # BLNC_SHT_RCGNSD_FNNCNL_ASST_INSTRMNT
	Advances_that_are_not_loanss = []# Advances_that_are_not_loans[]
	def calc_Advances_that_are_not_loanss(self) :
		items = [] # Advances_that_are_not_loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Advances_that_are_not_loanss.extend(self.calc_Advances_that_are_not_loanss())
		CSVConverter.persist_object_as_csv(self,True)
		return None

