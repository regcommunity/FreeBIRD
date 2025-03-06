from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_05_01_REF_FINREP_3_0_UnionItem:
	base = None #F_05_01_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.base.GRSS_CRRYNG_AMNT()
	@lineage(dependencies={"base.PRPS"})
	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.base.PRPS()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.base.INSTTTNL_SCTR()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.base.RPYMNT_RGHTS()
	@lineage(dependencies={"base.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.base.PRJCT_FNNC_LN()
	@lineage(dependencies={"base.CRRYNG_AMNT"})
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
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None # Reverse_repurchase_agreements
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
		for item in F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss:
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
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT

	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.ACCNTNG_CLSSFCTN
	
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.CRRYNG_AMNT
	PRTY = None # PRTY
	
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	FNNCL_ASST_INSTRMNT_DRVD_DT = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.FNNCL_ASST_INSTRMNT_DRVD_DT.GRSS_CRRYNG_AMNT
	FNNCL_ASST_INSTRMNT = None # FNNCL_ASST_INSTRMNT
	
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRPS"})
	def PRPS(self):
		return self.FNNCL_ASST_INSTRMNT.PRPS
	
	@lineage(dependencies={"FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN"})
	def PRJCT_FNNC_LN(self):
		return self.FNNCL_ASST_INSTRMNT.PRJCT_FNNC_LN
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	
	@lineage(dependencies={"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS.HLD_SL_INDCTR
	LN_EXCLDNG_RPRCHS_AGRMNT = None # LN_EXCLDNG_RPRCHS_AGRMNT
	
	@lineage(dependencies={"LN_EXCLDNG_RPRCHS_AGRMNT.LN_TYP"})
	def TYP_INSTRMNT(self):
		return self.LN_EXCLDNG_RPRCHS_AGRMNT.LN_TYP
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration '''
		return '2'

class Non_Negotiable_bonds(F_05_01_REF_FINREP_3_0_Base):
	pass
	LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT = None # LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_ACCNTNG_CLSSFCTN_FNNCL_ASSTS_ASSGNMNT.CRRYNG_AMNT

class Credit_card_debt(F_05_01_REF_FINREP_3_0_Base):
	pass

class Trade_receivables(F_05_01_REF_FINREP_3_0_Base):
	TRD_RCVBL = None # TRD_RCVBL
	@lineage(dependencies={"TRD_RCVBL.TRD_RCVBL_TYP"})
	def TYP_INSTRMNT(self):
		return self.TRD_RCVBL.TRD_RCVBL_TYP

class Finance_leases(F_05_01_REF_FINREP_3_0_Base):
	pass

class Reverse_repurchase_agreements(F_05_01_REF_FINREP_3_0_Base):
	RPRCHS_AGRMNT_INSTRMNT = None # RPRCHS_AGRMNT_INSTRMNT
	@lineage(dependencies={"RPRCHS_AGRMNT_INSTRMNT.RPRCHS_AGRMNT_INSTRMNT_TYP"})
	def TYP_INSTRMNT(self):
		return self.RPRCHS_AGRMNT_INSTRMNT.RPRCHS_AGRMNT_INSTRMNT_TYP

class Advances_that_are_not_loans(F_05_01_REF_FINREP_3_0_Base):
	ADVNC = None # ADVNC
	@lineage(dependencies={"ADVNC.ADVNC_TYP"})
	def TYP_INSTRMNT(self):
		return self.ADVNC.ADVNC_TYP

class F_05_01_REF_FINREP_3_0_Other_Loans_Table:
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT
	PRTY_Table = None # PRTY
	FNNCL_ASST_INSTRMNT_Table = None # FNNCL_ASST_INSTRMNT
	BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS_Table = None # BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS
	FNNCL_ASST_INSTRMNT_DRVD_DT_Table = None # FNNCL_ASST_INSTRMNT_DRVD_DT
	LN_EXCLDNG_RPRCHS_AGRMNT_Table = None # LN_EXCLDNG_RPRCHS_AGRMNT
	OTHR_LN_Table = None # OTHR_LN
	OTHR_LN_DBTR_ASSGNMNT_Table = None # OTHR_LN_DBTR_ASSGNMNT
	INSTRMNT_Table = None
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	Other_Loanss = []# Other_Loans[]

	@lineage(dependencies={"OTHR_LN_DBTR_ASSGNMNT.MN_DBTR_INDCTR",
		"OTHR_LN_DBTR_ASSGNMNT.Other_loan_has_Debtor_s_via_Other_loan_Loan_debtor_assignment",
		"OTHR_LN_DBTR_ASSGNMNT.Loan_debtor_is_obliged_to_pay_Other_loan_s_via_Other_loan_Debtor_assignment",
		"PRTY_RL.Party_acts_in_Party_role",
		"INSTRMNT.Instrument_type_by_product_delegate",
		"Instrument_type_by_product.Instrument_type_by_product_uniqueID",
		"OTHR_LN.Instrument_type_by_product_uniqueID",
		"BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.Balance_sheet_recognised_financial_asset_instrument_type_delegate",
		"Balance_sheet_recognised_financial_asset_instrument_type.blnc_sht_rcgnsd_fnncl_asst_instrmnt_ifrs",
		"FNNCL_ASST_INSTRMNT.Financial_asset_instrument_has_Financial_asset_instrument_derived_data",
		"FNNCL_ASST_INSTRMNT.Financial_asset_instrument_type_delegate",
		"FNNCL_ASST_INSTRMNT.Instrument_acts_in_Instrument_role_s"})
	def calc_Other_Loanss(self) :
		items = [] # Other_Loans[]
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations

		
		for loan in self.LN_EXCLDNG_RPRCHS_AGRMNT_Table:
			if loan.LN_TYP == '1022':
				other_loan = loan.Loan_type_delegate
				new_item = Other_Loans()
				new_item.LN_EXCLDNG_RPRCHS_AGRMNT = loan
				import pdb; pdb.set_trace()
				for debtor in  self.OTHR_LN_DBTR_ASSGNMNT_Table:
					if debtor.Other_loan_has_Debtor_s_via_Other_loan_Loan_debtor_assignment.Loan_type_uniqueID == other_loan.Loan_type_uniqueID and debtor.MN_DBTR_INDCTR == '1':
						new_item.PRTY = debtor.Loan_debtor_is_obliged_to_pay_Other_loan_s_via_Other_loan_Loan_debtor_assignment.Party_acts_in_Party_role
						
				the_instrument = None		
				for instrument in self.INSTRMNT_Table:
					if instrument.Instrument_type_by_product_delegate.Instrument_type_by_product_uniqueID == loan.Instrument_type_by_product_uniqueID:
						the_instrument = instrument
						break
				
				if the_instrument is not None:
					for instrument_rl in self.FNNCL_ASST_INSTRMNT_Table:
						if instrument_rl.Instrument_acts_in_Instrument_role_s == the_instrument:
							new_item.FNNCL_ASST_INSTRMNT = instrument_rl
							new_item.FNNCL_ASST_INSTRMNT_DRVD_DT = instrument_rl.Financial_asset_instrument_has_Financial_asset_instrument_derived_data
							Financial_asset_instrument_type_delegate = instrument_rl.Financial_asset_instrument_type_delegate
							
							if Financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt:
								new_item.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT = Financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt
								Balance_sheet_recognised_financial_asset_instrument_type_delegate = new_item.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT.Balance_sheet_recognised_financial_asset_instrument_type_delegate
								if Balance_sheet_recognised_financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt_ifrs:
									new_item.BLNC_SHT_RCGNSD_FNNCL_ASST_INSTRMNT_IFRS = Balance_sheet_recognised_financial_asset_instrument_type_delegate.blnc_sht_rcgnsd_fnncl_asst_instrmnt_ifrs
							break

							
				items.append(new_item)
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


class F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table:
	RPRCHS_AGRMNT_INSTRMNT_Table = None # RPRCHS_AGRMNT_INSTRMNT
	Reverse_repurchase_agreementss = []# Reverse_repurchase_agreements[]
	def calc_Reverse_repurchase_agreementss(self) :
		items = [] # Reverse_repurchase_agreements[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Reverse_repurchase_agreementss.extend(self.calc_Reverse_repurchase_agreementss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table:
	ADVNC_Table = None # ADVNC
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

