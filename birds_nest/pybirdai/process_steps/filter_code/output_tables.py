from pybirdai.process_steps.pybird.orchestration import Orchestration
from datetime import datetime
from .F_01_01_REF_FINREP_3_0_logic import *

class F_01_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_01_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()


class F_01_01_REF_FINREP_3_0_Table :
	F_01_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_01_01_REF_FINREP_3_0s = [] #F_01_01_REF_FINREP_3_0[]
	def  calc_F_01_01_REF_FINREP_3_0s(self) -> list[F_01_01_REF_FINREP_3_0] :
		items = [] # F_01_01_REF_FINREP_3_0[]
		for item in self.F_01_01_REF_FINREP_3_0_UnionTable.F_01_01_REF_FINREP_3_0_UnionItems:
			newItem = F_01_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_01_01_REF_FINREP_3_0s.extend(self.calc_F_01_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_01_02_REF_FINREP_3_0_logic import *

class F_01_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_01_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()


class F_01_02_REF_FINREP_3_0_Table :
	F_01_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_01_02_REF_FINREP_3_0s = [] #F_01_02_REF_FINREP_3_0[]
	def  calc_F_01_02_REF_FINREP_3_0s(self) -> list[F_01_02_REF_FINREP_3_0] :
		items = [] # F_01_02_REF_FINREP_3_0[]
		for item in self.F_01_02_REF_FINREP_3_0_UnionTable.F_01_02_REF_FINREP_3_0_UnionItems:
			newItem = F_01_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_01_02_REF_FINREP_3_0s.extend(self.calc_F_01_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_01_REF_FINREP_3_0_logic import *

class F_04_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_04_01_REF_FINREP_3_0_Table :
	F_04_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_01_REF_FINREP_3_0s = [] #F_04_01_REF_FINREP_3_0[]
	def  calc_F_04_01_REF_FINREP_3_0s(self) -> list[F_04_01_REF_FINREP_3_0] :
		items = [] # F_04_01_REF_FINREP_3_0[]
		for item in self.F_04_01_REF_FINREP_3_0_UnionTable.F_04_01_REF_FINREP_3_0_UnionItems:
			newItem = F_04_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s.extend(self.calc_F_04_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_02_1_REF_FINREP_3_0_logic import *

class F_04_02_1_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_02_1_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_04_02_1_REF_FINREP_3_0_Table :
	F_04_02_1_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_02_1_REF_FINREP_3_0s = [] #F_04_02_1_REF_FINREP_3_0[]
	def  calc_F_04_02_1_REF_FINREP_3_0s(self) -> list[F_04_02_1_REF_FINREP_3_0] :
		items = [] # F_04_02_1_REF_FINREP_3_0[]
		for item in self.F_04_02_1_REF_FINREP_3_0_UnionTable.F_04_02_1_REF_FINREP_3_0_UnionItems:
			newItem = F_04_02_1_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_02_1_REF_FINREP_3_0s.extend(self.calc_F_04_02_1_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_02_2_REF_FINREP_3_0_logic import *

class F_04_02_2_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_02_2_REF_FINREP_3_0_UnionItem  unionOfLayers
	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_04_02_2_REF_FINREP_3_0_Table :
	F_04_02_2_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_02_2_REF_FINREP_3_0s = [] #F_04_02_2_REF_FINREP_3_0[]
	def  calc_F_04_02_2_REF_FINREP_3_0s(self) -> list[F_04_02_2_REF_FINREP_3_0] :
		items = [] # F_04_02_2_REF_FINREP_3_0[]
		for item in self.F_04_02_2_REF_FINREP_3_0_UnionTable.F_04_02_2_REF_FINREP_3_0_UnionItems:
			newItem = F_04_02_2_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_02_2_REF_FINREP_3_0s.extend(self.calc_F_04_02_2_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_03_1_REF_FINREP_3_0_logic import *

class F_04_03_1_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_03_1_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCMLTD_TTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_TTL_WRTFFS()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def ACCMLTD_PRTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_PRTL_WRTFFS()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	def LW_CRDT_RSK_INDCTR(self) -> str:
		''' return string from LW_CRDT_RSK_INDCTR enumeration '''
		return self.unionOfLayers.LW_CRDT_RSK_INDCTR()


class F_04_03_1_REF_FINREP_3_0_Table :
	F_04_03_1_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_03_1_REF_FINREP_3_0s = [] #F_04_03_1_REF_FINREP_3_0[]
	def  calc_F_04_03_1_REF_FINREP_3_0s(self) -> list[F_04_03_1_REF_FINREP_3_0] :
		items = [] # F_04_03_1_REF_FINREP_3_0[]
		for item in self.F_04_03_1_REF_FINREP_3_0_UnionTable.F_04_03_1_REF_FINREP_3_0_UnionItems:
			newItem = F_04_03_1_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_03_1_REF_FINREP_3_0s.extend(self.calc_F_04_03_1_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_04_1_REF_FINREP_3_0_logic import *

class F_04_04_1_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_04_1_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCMLTD_PRTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_PRTL_WRTFFS()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCMLTD_TTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_TTL_WRTFFS()

	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	def LW_CRDT_RSK_INDCTR(self) -> str:
		''' return string from LW_CRDT_RSK_INDCTR enumeration '''
		return self.unionOfLayers.LW_CRDT_RSK_INDCTR()


class F_04_04_1_REF_FINREP_3_0_Table :
	F_04_04_1_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_04_1_REF_FINREP_3_0s = [] #F_04_04_1_REF_FINREP_3_0[]
	def  calc_F_04_04_1_REF_FINREP_3_0s(self) -> list[F_04_04_1_REF_FINREP_3_0] :
		items = [] # F_04_04_1_REF_FINREP_3_0[]
		for item in self.F_04_04_1_REF_FINREP_3_0_UnionTable.F_04_04_1_REF_FINREP_3_0_UnionItems:
			newItem = F_04_04_1_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_04_1_REF_FINREP_3_0s.extend(self.calc_F_04_04_1_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_05_REF_FINREP_3_0_logic import *

class F_04_05_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_05_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def SBRDNTD_DBT(self) -> str:
		''' return string from SBRDNTD_DBT enumeration '''
		return self.unionOfLayers.SBRDNTD_DBT()


class F_04_05_REF_FINREP_3_0_Table :
	F_04_05_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_05_REF_FINREP_3_0s = [] #F_04_05_REF_FINREP_3_0[]
	def  calc_F_04_05_REF_FINREP_3_0s(self) -> list[F_04_05_REF_FINREP_3_0] :
		items = [] # F_04_05_REF_FINREP_3_0[]
		for item in self.F_04_05_REF_FINREP_3_0_UnionTable.F_04_05_REF_FINREP_3_0_UnionItems:
			newItem = F_04_05_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_05_REF_FINREP_3_0s.extend(self.calc_F_04_05_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_06_REF_FINREP_3_0_logic import *

class F_04_06_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_06_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_04_06_REF_FINREP_3_0_Table :
	F_04_06_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_06_REF_FINREP_3_0s = [] #F_04_06_REF_FINREP_3_0[]
	def  calc_F_04_06_REF_FINREP_3_0s(self) -> list[F_04_06_REF_FINREP_3_0] :
		items = [] # F_04_06_REF_FINREP_3_0[]
		for item in self.F_04_06_REF_FINREP_3_0_UnionTable.F_04_06_REF_FINREP_3_0_UnionItems:
			newItem = F_04_06_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_06_REF_FINREP_3_0s.extend(self.calc_F_04_06_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_07_REF_FINREP_3_0_logic import *

class F_04_07_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_07_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()


class F_04_07_REF_FINREP_3_0_Table :
	F_04_07_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_07_REF_FINREP_3_0s = [] #F_04_07_REF_FINREP_3_0[]
	def  calc_F_04_07_REF_FINREP_3_0s(self) -> list[F_04_07_REF_FINREP_3_0] :
		items = [] # F_04_07_REF_FINREP_3_0[]
		for item in self.F_04_07_REF_FINREP_3_0_UnionTable.F_04_07_REF_FINREP_3_0_UnionItems:
			newItem = F_04_07_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_07_REF_FINREP_3_0s.extend(self.calc_F_04_07_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_08_REF_FINREP_3_0_logic import *

class F_04_08_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_08_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	def ACCMLTD_TTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_TTL_WRTFFS()

	def ACCMLTD_PRTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_PRTL_WRTFFS()

	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()


class F_04_08_REF_FINREP_3_0_Table :
	F_04_08_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_08_REF_FINREP_3_0s = [] #F_04_08_REF_FINREP_3_0[]
	def  calc_F_04_08_REF_FINREP_3_0s(self) -> list[F_04_08_REF_FINREP_3_0] :
		items = [] # F_04_08_REF_FINREP_3_0[]
		for item in self.F_04_08_REF_FINREP_3_0_UnionTable.F_04_08_REF_FINREP_3_0_UnionItems:
			newItem = F_04_08_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_08_REF_FINREP_3_0s.extend(self.calc_F_04_08_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_09_REF_FINREP_3_0_logic import *

class F_04_09_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_09_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	def ACCMLTD_NGTV_VL_ADJSTMNT_MR(self) -> int:
		return self.unionOfLayers.ACCMLTD_NGTV_VL_ADJSTMNT_MR()

	def ACCMLTD_PRTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_PRTL_WRTFFS()

	def ACCMLTD_TTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_TTL_WRTFFS()

	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()


class F_04_09_REF_FINREP_3_0_Table :
	F_04_09_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_09_REF_FINREP_3_0s = [] #F_04_09_REF_FINREP_3_0[]
	def  calc_F_04_09_REF_FINREP_3_0s(self) -> list[F_04_09_REF_FINREP_3_0] :
		items = [] # F_04_09_REF_FINREP_3_0[]
		for item in self.F_04_09_REF_FINREP_3_0_UnionTable.F_04_09_REF_FINREP_3_0_UnionItems:
			newItem = F_04_09_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_09_REF_FINREP_3_0s.extend(self.calc_F_04_09_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_04_10_REF_FINREP_3_0_logic import *

class F_04_10_REF_FINREP_3_0:
	unionOfLayers = None #  F_04_10_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCMLTD_PRTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_PRTL_WRTFFS()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCMLTD_NGTV_VL_ADJSTMNT_MR(self) -> int:
		return self.unionOfLayers.ACCMLTD_NGTV_VL_ADJSTMNT_MR()

	def ACCMLTD_TTL_WRTFFS(self) -> int:
		return self.unionOfLayers.ACCMLTD_TTL_WRTFFS()

	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()


class F_04_10_REF_FINREP_3_0_Table :
	F_04_10_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_04_10_REF_FINREP_3_0s = [] #F_04_10_REF_FINREP_3_0[]
	def  calc_F_04_10_REF_FINREP_3_0s(self) -> list[F_04_10_REF_FINREP_3_0] :
		items = [] # F_04_10_REF_FINREP_3_0[]
		for item in self.F_04_10_REF_FINREP_3_0_UnionTable.F_04_10_REF_FINREP_3_0_UnionItems:
			newItem = F_04_10_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_04_10_REF_FINREP_3_0s.extend(self.calc_F_04_10_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_05_01_REF_FINREP_3_0_logic import *

class F_05_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_05_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.unionOfLayers.PRJCT_FNNC_LN()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_05_01_REF_FINREP_3_0_Table :
	F_05_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_05_01_REF_FINREP_3_0s = [] #F_05_01_REF_FINREP_3_0[]
	def  calc_F_05_01_REF_FINREP_3_0s(self) -> list[F_05_01_REF_FINREP_3_0] :
		items = [] # F_05_01_REF_FINREP_3_0[]
		for item in self.F_05_01_REF_FINREP_3_0_UnionTable.F_05_01_REF_FINREP_3_0_UnionItems:
			newItem = F_05_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s.extend(self.calc_F_05_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_06_01_REF_FINREP_3_0_logic import *

class F_06_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_06_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def ECNMC_ACTVTY(self) -> str:
		''' return string from ECNMC_ACTVTY enumeration '''
		return self.unionOfLayers.ECNMC_ACTVTY()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()


class F_06_01_REF_FINREP_3_0_Table :
	F_06_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_06_01_REF_FINREP_3_0s = [] #F_06_01_REF_FINREP_3_0[]
	def  calc_F_06_01_REF_FINREP_3_0s(self) -> list[F_06_01_REF_FINREP_3_0] :
		items = [] # F_06_01_REF_FINREP_3_0[]
		for item in self.F_06_01_REF_FINREP_3_0_UnionTable.F_06_01_REF_FINREP_3_0_UnionItems:
			newItem = F_06_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_06_01_REF_FINREP_3_0s.extend(self.calc_F_06_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_07_01_REF_FINREP_3_0_logic import *

class F_07_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_07_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.unionOfLayers.PRJCT_FNNC_LN()

	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()


class F_07_01_REF_FINREP_3_0_Table :
	F_07_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_07_01_REF_FINREP_3_0s = [] #F_07_01_REF_FINREP_3_0[]
	def  calc_F_07_01_REF_FINREP_3_0s(self) -> list[F_07_01_REF_FINREP_3_0] :
		items = [] # F_07_01_REF_FINREP_3_0[]
		for item in self.F_07_01_REF_FINREP_3_0_UnionTable.F_07_01_REF_FINREP_3_0_UnionItems:
			newItem = F_07_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_07_01_REF_FINREP_3_0s.extend(self.calc_F_07_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_07_02_REF_FINREP_3_0_logic import *

class F_07_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_07_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def PRJCT_FNNC_LN(self) -> str:
		''' return string from PRJCT_FNNC_LN enumeration '''
		return self.unionOfLayers.PRJCT_FNNC_LN()

	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()


class F_07_02_REF_FINREP_3_0_Table :
	F_07_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_07_02_REF_FINREP_3_0s = [] #F_07_02_REF_FINREP_3_0[]
	def  calc_F_07_02_REF_FINREP_3_0s(self) -> list[F_07_02_REF_FINREP_3_0] :
		items = [] # F_07_02_REF_FINREP_3_0[]
		for item in self.F_07_02_REF_FINREP_3_0_UnionTable.F_07_02_REF_FINREP_3_0_UnionItems:
			newItem = F_07_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_07_02_REF_FINREP_3_0s.extend(self.calc_F_07_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_08_01_a_REF_FINREP_3_0_logic import *

class F_08_01_a_REF_FINREP_3_0:
	unionOfLayers = None #  F_08_01_a_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCMLTD_CHNGS_FV_CR(self) -> int:
		return self.unionOfLayers.ACCMLTD_CHNGS_FV_CR()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_08_01_a_REF_FINREP_3_0_Table :
	F_08_01_a_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_08_01_a_REF_FINREP_3_0s = [] #F_08_01_a_REF_FINREP_3_0[]
	def  calc_F_08_01_a_REF_FINREP_3_0s(self) -> list[F_08_01_a_REF_FINREP_3_0] :
		items = [] # F_08_01_a_REF_FINREP_3_0[]
		for item in self.F_08_01_a_REF_FINREP_3_0_UnionTable.F_08_01_a_REF_FINREP_3_0_UnionItems:
			newItem = F_08_01_a_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_08_01_a_REF_FINREP_3_0s.extend(self.calc_F_08_01_a_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_08_02_REF_FINREP_3_0_logic import *

class F_08_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_08_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def SBRDNTD_DBT(self) -> str:
		''' return string from SBRDNTD_DBT enumeration '''
		return self.unionOfLayers.SBRDNTD_DBT()


class F_08_02_REF_FINREP_3_0_Table :
	F_08_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_08_02_REF_FINREP_3_0s = [] #F_08_02_REF_FINREP_3_0[]
	def  calc_F_08_02_REF_FINREP_3_0s(self) -> list[F_08_02_REF_FINREP_3_0] :
		items = [] # F_08_02_REF_FINREP_3_0[]
		for item in self.F_08_02_REF_FINREP_3_0_UnionTable.F_08_02_REF_FINREP_3_0_UnionItems:
			newItem = F_08_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_08_02_REF_FINREP_3_0s.extend(self.calc_F_08_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_13_01_REF_FINREP_3_0_logic import *

class F_13_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_13_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()


class F_13_01_REF_FINREP_3_0_Table :
	F_13_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_13_01_REF_FINREP_3_0s = [] #F_13_01_REF_FINREP_3_0[]
	def  calc_F_13_01_REF_FINREP_3_0s(self) -> list[F_13_01_REF_FINREP_3_0] :
		items = [] # F_13_01_REF_FINREP_3_0[]
		for item in self.F_13_01_REF_FINREP_3_0_UnionTable.F_13_01_REF_FINREP_3_0_UnionItems:
			newItem = F_13_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_13_01_REF_FINREP_3_0s.extend(self.calc_F_13_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_14_00_REF_FINREP_3_0_logic import *

class F_14_00_REF_FINREP_3_0:
	unionOfLayers = None #  F_14_00_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCMLTD_CHNGS_FV(self) -> int:
		return self.unionOfLayers.ACCMLTD_CHNGS_FV()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def FV_HRRCHY(self) -> str:
		''' return string from FV_HRRCHY enumeration '''
		return self.unionOfLayers.FV_HRRCHY()

	def FV(self) -> int:
		return self.unionOfLayers.FV()

	def FV_CHNG(self) -> int:
		return self.unionOfLayers.FV_CHNG()


class F_14_00_REF_FINREP_3_0_Table :
	F_14_00_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_14_00_REF_FINREP_3_0s = [] #F_14_00_REF_FINREP_3_0[]
	def  calc_F_14_00_REF_FINREP_3_0s(self) -> list[F_14_00_REF_FINREP_3_0] :
		items = [] # F_14_00_REF_FINREP_3_0[]
		for item in self.F_14_00_REF_FINREP_3_0_UnionTable.F_14_00_REF_FINREP_3_0_UnionItems:
			newItem = F_14_00_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_14_00_REF_FINREP_3_0s.extend(self.calc_F_14_00_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_15_00_a_REF_FINREP_3_0_logic import *

class F_15_00_a_REF_FINREP_3_0:
	unionOfLayers = None #  F_15_00_a_REF_FINREP_3_0_UnionItem  unionOfLayers
	def TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT(self) -> str:
		''' return string from RCGNTN_STTS enumeration '''
		return self.unionOfLayers.TRTMNT_TRNSFRRD_ASSTS_BLNC_SHT()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def AMNT_DRCGNSD_CPTL_PRPS(self) -> int:
		return self.unionOfLayers.AMNT_DRCGNSD_CPTL_PRPS()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_15_00_a_REF_FINREP_3_0_Table :
	F_15_00_a_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_15_00_a_REF_FINREP_3_0s = [] #F_15_00_a_REF_FINREP_3_0[]
	def  calc_F_15_00_a_REF_FINREP_3_0s(self) -> list[F_15_00_a_REF_FINREP_3_0] :
		items = [] # F_15_00_a_REF_FINREP_3_0[]
		for item in self.F_15_00_a_REF_FINREP_3_0_UnionTable.F_15_00_a_REF_FINREP_3_0_UnionItems:
			newItem = F_15_00_a_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_15_00_a_REF_FINREP_3_0s.extend(self.calc_F_15_00_a_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_18_00_a_REF_FINREP_3_0_logic import *

class F_18_00_a_REF_FINREP_3_0:
	unionOfLayers = None #  F_18_00_a_REF_FINREP_3_0_UnionItem  unionOfLayers
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()


class F_18_00_a_REF_FINREP_3_0_Table :
	F_18_00_a_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_18_00_a_REF_FINREP_3_0s = [] #F_18_00_a_REF_FINREP_3_0[]
	def  calc_F_18_00_a_REF_FINREP_3_0s(self) -> list[F_18_00_a_REF_FINREP_3_0] :
		items = [] # F_18_00_a_REF_FINREP_3_0[]
		for item in self.F_18_00_a_REF_FINREP_3_0_UnionTable.F_18_00_a_REF_FINREP_3_0_UnionItems:
			newItem = F_18_00_a_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_18_00_a_REF_FINREP_3_0s.extend(self.calc_F_18_00_a_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_18_00_b_REF_FINREP_3_0_logic import *

class F_18_00_b_REF_FINREP_3_0:
	unionOfLayers = None #  F_18_00_b_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()


class F_18_00_b_REF_FINREP_3_0_Table :
	F_18_00_b_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_18_00_b_REF_FINREP_3_0s = [] #F_18_00_b_REF_FINREP_3_0[]
	def  calc_F_18_00_b_REF_FINREP_3_0s(self) -> list[F_18_00_b_REF_FINREP_3_0] :
		items = [] # F_18_00_b_REF_FINREP_3_0[]
		for item in self.F_18_00_b_REF_FINREP_3_0_UnionTable.F_18_00_b_REF_FINREP_3_0_UnionItems:
			newItem = F_18_00_b_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_18_00_b_REF_FINREP_3_0s.extend(self.calc_F_18_00_b_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_18_00_c_REF_FINREP_3_0_logic import *

class F_18_00_c_REF_FINREP_3_0:
	unionOfLayers = None #  F_18_00_c_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_18_00_c_REF_FINREP_3_0_Table :
	F_18_00_c_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_18_00_c_REF_FINREP_3_0s = [] #F_18_00_c_REF_FINREP_3_0[]
	def  calc_F_18_00_c_REF_FINREP_3_0s(self) -> list[F_18_00_c_REF_FINREP_3_0] :
		items = [] # F_18_00_c_REF_FINREP_3_0[]
		for item in self.F_18_00_c_REF_FINREP_3_0_UnionTable.F_18_00_c_REF_FINREP_3_0_UnionItems:
			newItem = F_18_00_c_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_18_00_c_REF_FINREP_3_0s.extend(self.calc_F_18_00_c_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_18_00_d_REF_FINREP_3_0_logic import *

class F_18_00_d_REF_FINREP_3_0:
	unionOfLayers = None #  F_18_00_d_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()


class F_18_00_d_REF_FINREP_3_0_Table :
	F_18_00_d_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_18_00_d_REF_FINREP_3_0s = [] #F_18_00_d_REF_FINREP_3_0[]
	def  calc_F_18_00_d_REF_FINREP_3_0s(self) -> list[F_18_00_d_REF_FINREP_3_0] :
		items = [] # F_18_00_d_REF_FINREP_3_0[]
		for item in self.F_18_00_d_REF_FINREP_3_0_UnionTable.F_18_00_d_REF_FINREP_3_0_UnionItems:
			newItem = F_18_00_d_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_18_00_d_REF_FINREP_3_0s.extend(self.calc_F_18_00_d_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_19_00_a_REF_FINREP_3_0_logic import *

class F_19_00_a_REF_FINREP_3_0:
	unionOfLayers = None #  F_19_00_a_REF_FINREP_3_0_UnionItem  unionOfLayers
	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()

	def IMPRMNT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.IMPRMNT_STTS()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def NN_PRFRMNG_PRR_FRBRNC_INDCTR(self) -> str:
		''' return string from NN_PRFRMNG_PRR_FRBRNC_INDCTR enumeration '''
		return self.unionOfLayers.NN_PRFRMNG_PRR_FRBRNC_INDCTR()

	def PRFRMNG_STTS_RSN(self) -> str:
		''' return string from PRFRMNG_STTS_RSN enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS_RSN()


class F_19_00_a_REF_FINREP_3_0_Table :
	F_19_00_a_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_19_00_a_REF_FINREP_3_0s = [] #F_19_00_a_REF_FINREP_3_0[]
	def  calc_F_19_00_a_REF_FINREP_3_0s(self) -> list[F_19_00_a_REF_FINREP_3_0] :
		items = [] # F_19_00_a_REF_FINREP_3_0[]
		for item in self.F_19_00_a_REF_FINREP_3_0_UnionTable.F_19_00_a_REF_FINREP_3_0_UnionItems:
			newItem = F_19_00_a_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_19_00_a_REF_FINREP_3_0s.extend(self.calc_F_19_00_a_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_19_00_b_REF_FINREP_3_0_logic import *

class F_19_00_b_REF_FINREP_3_0:
	unionOfLayers = None #  F_19_00_b_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()


class F_19_00_b_REF_FINREP_3_0_Table :
	F_19_00_b_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_19_00_b_REF_FINREP_3_0s = [] #F_19_00_b_REF_FINREP_3_0[]
	def  calc_F_19_00_b_REF_FINREP_3_0s(self) -> list[F_19_00_b_REF_FINREP_3_0] :
		items = [] # F_19_00_b_REF_FINREP_3_0[]
		for item in self.F_19_00_b_REF_FINREP_3_0_UnionTable.F_19_00_b_REF_FINREP_3_0_UnionItems:
			newItem = F_19_00_b_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_19_00_b_REF_FINREP_3_0s.extend(self.calc_F_19_00_b_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_19_00_c_REF_FINREP_3_0_logic import *

class F_19_00_c_REF_FINREP_3_0:
	unionOfLayers = None #  F_19_00_c_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()


class F_19_00_c_REF_FINREP_3_0_Table :
	F_19_00_c_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_19_00_c_REF_FINREP_3_0s = [] #F_19_00_c_REF_FINREP_3_0[]
	def  calc_F_19_00_c_REF_FINREP_3_0s(self) -> list[F_19_00_c_REF_FINREP_3_0] :
		items = [] # F_19_00_c_REF_FINREP_3_0[]
		for item in self.F_19_00_c_REF_FINREP_3_0_UnionTable.F_19_00_c_REF_FINREP_3_0_UnionItems:
			newItem = F_19_00_c_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_19_00_c_REF_FINREP_3_0s.extend(self.calc_F_19_00_c_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_19_00_e_REF_FINREP_3_0_logic import *

class F_19_00_e_REF_FINREP_3_0:
	unionOfLayers = None #  F_19_00_e_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()


class F_19_00_e_REF_FINREP_3_0_Table :
	F_19_00_e_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_19_00_e_REF_FINREP_3_0s = [] #F_19_00_e_REF_FINREP_3_0[]
	def  calc_F_19_00_e_REF_FINREP_3_0s(self) -> list[F_19_00_e_REF_FINREP_3_0] :
		items = [] # F_19_00_e_REF_FINREP_3_0[]
		for item in self.F_19_00_e_REF_FINREP_3_0_UnionTable.F_19_00_e_REF_FINREP_3_0_UnionItems:
			newItem = F_19_00_e_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_19_00_e_REF_FINREP_3_0s.extend(self.calc_F_19_00_e_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_01_REF_FINREP_3_0_logic import *

class F_20_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()


class F_20_01_REF_FINREP_3_0_Table :
	F_20_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_01_REF_FINREP_3_0s = [] #F_20_01_REF_FINREP_3_0[]
	def  calc_F_20_01_REF_FINREP_3_0s(self) -> list[F_20_01_REF_FINREP_3_0] :
		items = [] # F_20_01_REF_FINREP_3_0[]
		for item in self.F_20_01_REF_FINREP_3_0_UnionTable.F_20_01_REF_FINREP_3_0_UnionItems:
			newItem = F_20_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_01_REF_FINREP_3_0s.extend(self.calc_F_20_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_02_REF_FINREP_3_0_logic import *

class F_20_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.unionOfLayers.TYP_HDG()


class F_20_02_REF_FINREP_3_0_Table :
	F_20_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_02_REF_FINREP_3_0s = [] #F_20_02_REF_FINREP_3_0[]
	def  calc_F_20_02_REF_FINREP_3_0s(self) -> list[F_20_02_REF_FINREP_3_0] :
		items = [] # F_20_02_REF_FINREP_3_0[]
		for item in self.F_20_02_REF_FINREP_3_0_UnionTable.F_20_02_REF_FINREP_3_0_UnionItems:
			newItem = F_20_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_02_REF_FINREP_3_0s.extend(self.calc_F_20_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_04_REF_FINREP_3_0_logic import *

class F_20_04_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_04_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def RPYMNT_RGHTS(self) -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		return self.unionOfLayers.RPYMNT_RGHTS()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def ENTRPRS_SZ(self) -> str:
		''' return string from SZ enumeration '''
		return self.unionOfLayers.ENTRPRS_SZ()

	def PRPS(self) -> str:
		''' return string from PRPS enumeration '''
		return self.unionOfLayers.PRPS()

	def DFLT_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.DFLT_STTS()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()


class F_20_04_REF_FINREP_3_0_Table :
	F_20_04_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_04_REF_FINREP_3_0s = [] #F_20_04_REF_FINREP_3_0[]
	def  calc_F_20_04_REF_FINREP_3_0s(self) -> list[F_20_04_REF_FINREP_3_0] :
		items = [] # F_20_04_REF_FINREP_3_0[]
		for item in self.F_20_04_REF_FINREP_3_0_UnionTable.F_20_04_REF_FINREP_3_0_UnionItems:
			newItem = F_20_04_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_04_REF_FINREP_3_0s.extend(self.calc_F_20_04_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_06_REF_FINREP_3_0_logic import *

class F_20_06_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_06_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()


class F_20_06_REF_FINREP_3_0_Table :
	F_20_06_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_06_REF_FINREP_3_0s = [] #F_20_06_REF_FINREP_3_0[]
	def  calc_F_20_06_REF_FINREP_3_0s(self) -> list[F_20_06_REF_FINREP_3_0] :
		items = [] # F_20_06_REF_FINREP_3_0[]
		for item in self.F_20_06_REF_FINREP_3_0_UnionTable.F_20_06_REF_FINREP_3_0_UnionItems:
			newItem = F_20_06_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_06_REF_FINREP_3_0s.extend(self.calc_F_20_06_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_20_07_1_REF_FINREP_3_0_logic import *

class F_20_07_1_REF_FINREP_3_0:
	unionOfLayers = None #  F_20_07_1_REF_FINREP_3_0_UnionItem  unionOfLayers
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def INSTTTNL_SCTR(self) -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		return self.unionOfLayers.INSTTTNL_SCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def ECNMC_ACTVTY(self) -> str:
		''' return string from ECNMC_ACTVTY enumeration '''
		return self.unionOfLayers.ECNMC_ACTVTY()

	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()

	def GRSS_CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.GRSS_CRRYNG_AMNT()


class F_20_07_1_REF_FINREP_3_0_Table :
	F_20_07_1_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_20_07_1_REF_FINREP_3_0s = [] #F_20_07_1_REF_FINREP_3_0[]
	def  calc_F_20_07_1_REF_FINREP_3_0s(self) -> list[F_20_07_1_REF_FINREP_3_0] :
		items = [] # F_20_07_1_REF_FINREP_3_0[]
		for item in self.F_20_07_1_REF_FINREP_3_0_UnionTable.F_20_07_1_REF_FINREP_3_0_UnionItems:
			newItem = F_20_07_1_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_20_07_1_REF_FINREP_3_0s.extend(self.calc_F_20_07_1_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_31_01_REF_FINREP_3_0_logic import *

class F_31_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_31_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def PRFRMNG_STTS(self) -> str:
		''' return string from CRDT_QLTY enumeration '''
		return self.unionOfLayers.PRFRMNG_STTS()

	def NMNL_AMNT(self) -> int:
		return self.unionOfLayers.NMNL_AMNT()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def NTNL_AMNT(self) -> int:
		return self.unionOfLayers.NTNL_AMNT()

	def ACCMLTD_IMPRMNT(self) -> int:
		return self.unionOfLayers.ACCMLTD_IMPRMNT()


class F_31_01_REF_FINREP_3_0_Table :
	F_31_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_31_01_REF_FINREP_3_0s = [] #F_31_01_REF_FINREP_3_0[]
	def  calc_F_31_01_REF_FINREP_3_0s(self) -> list[F_31_01_REF_FINREP_3_0] :
		items = [] # F_31_01_REF_FINREP_3_0[]
		for item in self.F_31_01_REF_FINREP_3_0_UnionTable.F_31_01_REF_FINREP_3_0_UnionItems:
			newItem = F_31_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_31_01_REF_FINREP_3_0s.extend(self.calc_F_31_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_41_01_REF_FINREP_3_0_logic import *

class F_41_01_REF_FINREP_3_0:
	unionOfLayers = None #  F_41_01_REF_FINREP_3_0_UnionItem  unionOfLayers
	def FV(self) -> int:
		return self.unionOfLayers.FV()

	def FV_HRRCHY(self) -> str:
		''' return string from FV_HRRCHY enumeration '''
		return self.unionOfLayers.FV_HRRCHY()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()


class F_41_01_REF_FINREP_3_0_Table :
	F_41_01_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_41_01_REF_FINREP_3_0s = [] #F_41_01_REF_FINREP_3_0[]
	def  calc_F_41_01_REF_FINREP_3_0s(self) -> list[F_41_01_REF_FINREP_3_0] :
		items = [] # F_41_01_REF_FINREP_3_0[]
		for item in self.F_41_01_REF_FINREP_3_0_UnionTable.F_41_01_REF_FINREP_3_0_UnionItems:
			newItem = F_41_01_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_41_01_REF_FINREP_3_0s.extend(self.calc_F_41_01_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

from .F_41_02_REF_FINREP_3_0_logic import *

class F_41_02_REF_FINREP_3_0:
	unionOfLayers = None #  F_41_02_REF_FINREP_3_0_UnionItem  unionOfLayers
	def CRRYNG_AMNT(self) -> int:
		return self.unionOfLayers.CRRYNG_AMNT()

	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.unionOfLayers.ACCNTNG_CLSSFCTN()

	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.unionOfLayers.HLD_SL_INDCTR()

	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.unionOfLayers.SBJCT_IMPRMNT_INDCTR()

	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.unionOfLayers.TYP_INSTRMNT()

	def FVO_DSGNTN(self) -> str:
		''' return string from FVO_DSGNTN enumeration '''
		return self.unionOfLayers.FVO_DSGNTN()


class F_41_02_REF_FINREP_3_0_Table :
	F_41_02_REF_FINREP_3_0_UnionTable = None # unionOfLayersTable
	F_41_02_REF_FINREP_3_0s = [] #F_41_02_REF_FINREP_3_0[]
	def  calc_F_41_02_REF_FINREP_3_0s(self) -> list[F_41_02_REF_FINREP_3_0] :
		items = [] # F_41_02_REF_FINREP_3_0[]
		for item in self.F_41_02_REF_FINREP_3_0_UnionTable.F_41_02_REF_FINREP_3_0_UnionItems:
			newItem = F_41_02_REF_FINREP_3_0()
			newItem.unionOfLayers = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.F_41_02_REF_FINREP_3_0s.extend(self.calc_F_41_02_REF_FINREP_3_0s())
		CSVConverter.persist_object_as_csv(self,True)
		return None

