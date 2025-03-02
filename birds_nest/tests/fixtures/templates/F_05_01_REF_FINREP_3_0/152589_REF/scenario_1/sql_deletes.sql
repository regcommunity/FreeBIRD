DELETE FROM pybirdai_abstrct_instrmnt_rl
WHERE
    rowid = 1;

DELETE FROM pybirdai_balance_sheet_recognised_financial_asset_instrument_by_fair_value_type
WHERE
    rowid = 1;

DELETE FROM pybirdai_balance_sheet_recognised_financial_asset_instrument_type
WHERE
    rowid = 1;

DELETE FROM pybirdai_blnc_sht_rcgnsd_fnncnl_asst_instrmnt
WHERE
    rowid = 1;

DELETE FROM pybirdai_blnc_sht_rcgnsd_fnncnl_asst_instrmnt_ifrs
WHERE
    rowid = 1;

DELETE FROM pybirdai_crdtr
WHERE
    rowid = 1;

DELETE FROM pybirdai_entity_role_type
WHERE
    rowid = 1;

DELETE FROM pybirdai_entity_role_type
WHERE
    rowid = 2;

DELETE FROM pybirdai_entty_rl
WHERE
    rowid = 1;

DELETE FROM pybirdai_entty_rl
WHERE
    rowid = 2;

DELETE FROM pybirdai_financial_asset_instrument_type
WHERE
    rowid = 1;

DELETE FROM pybirdai_financial_asset_instrument_type_by_crr_article_123_retail_exposure
WHERE
    rowid = 1;

DELETE FROM pybirdai_financial_asset_instrument_type_by_fixed_interest_rate
WHERE
    rowid = 1;

DELETE FROM pybirdai_financial_asset_instrument_type_by_interest_rate_only
WHERE
    rowid = 1;

DELETE FROM pybirdai_financial_asset_instrument_type_by_renegotiation_status
WHERE
    rowid = 1;

DELETE FROM pybirdai_fnncl_asst_instrmnt
WHERE
    rowid = 1;

DELETE FROM pybirdai_fnncl_cntrct
WHERE
    rowid = 1;

DELETE FROM pybirdai_fxd_intrst_fnncl_asst_instrmnt
WHERE
    rowid = 1;

DELETE FROM pybirdai_instrmnt
WHERE
    rowid = 1;

DELETE FROM pybirdai_instrmnt_entty_rl_assgnmnt
WHERE
    rowid = 3;

DELETE FROM pybirdai_instrmnt_entty_rl_assgnmnt
WHERE
    rowid = 4;

DELETE FROM pybirdai_instrmnt_rl
WHERE
    rowid = 1;

DELETE FROM pybirdai_instrmnt_rsltng_drctly_fnncl_cntrct
WHERE
    rowid = 1;

DELETE FROM pybirdai_instrument_type_by_origin
WHERE
    rowid = 1;

DELETE FROM pybirdai_instrument_type_by_product
WHERE
    rowid = 1;

DELETE FROM pybirdai_lgl_prsn
WHERE
    rowid = 1;

DELETE FROM pybirdai_lgl_prsn
WHERE
    rowid = 2;

DELETE FROM pybirdai_lgl_prsn
WHERE
    rowid = 3;

DELETE FROM pybirdai_ln_dbtr
WHERE
    rowid = 1;

DELETE FROM pybirdai_ln_excldng_rprchs_agrmnt
WHERE
    rowid = 1;

DELETE FROM pybirdai_ln_excldng_rprchs_agrmnt_and_advnce
WHERE
    rowid = 1;

DELETE FROM pybirdai_nn_intrst_onl_fnncl_asst_instrmnt
WHERE
    rowid = 1;

DELETE FROM pybirdai_nn_rngttd_fnncl_asst_instrmnt
WHERE
    rowid = 1;

DELETE FROM pybirdai_nn_rtl_expsr_fnncl_asst_instrmnt
WHERE
    rowid = 1;

DELETE FROM pybirdai_nt_pst_du_fnncl_asst_instrmnt
WHERE
    rowid = 1;

DELETE FROM pybirdai_orgnstn
WHERE
    rowid = 1;

DELETE FROM pybirdai_orgnstn
WHERE
    rowid = 2;

DELETE FROM pybirdai_orgnstn
WHERE
    rowid = 3;

DELETE FROM pybirdai_othr_ln
WHERE
    rowid = 1;

DELETE FROM pybirdai_othr_ln_crdtr_assgnmnt
WHERE
    rowid = 2;

DELETE FROM pybirdai_othr_ln_dbtr_assgnmnt
WHERE
    rowid = 2;

DELETE FROM pybirdai_party_type
WHERE
    rowid = 1;

DELETE FROM pybirdai_party_type
WHERE
    rowid = 2;

DELETE FROM pybirdai_party_type
WHERE
    rowid = 3;

DELETE FROM pybirdai_past_due_financial_asset_instrument_indicator
WHERE
    rowid = 1;

DELETE FROM pybirdai_prfrmng_nn_rtl_expsr_clss_fnncl_asst_instrmnt
WHERE
    rowid = 1;

DELETE FROM pybirdai_prty
WHERE
    rowid = 1;

DELETE FROM pybirdai_prty
WHERE
    rowid = 2;

DELETE FROM pybirdai_prty
WHERE
    rowid = 3;

DELETE FROM pybirdai_prty_rl
WHERE
    rowid = 1;

DELETE FROM pybirdai_prty_rl
WHERE
    rowid = 2;

DELETE FROM pybirdai_sngl_fnncl_cntrct
WHERE
    rowid = 1;

UPDATE pybirdai_blnc_sht_rcgnsd_fnncnl_asst_instrmnt
SET
    ACCNTNG_CLSSFCTN = NULL
WHERE
    rowid = 1;

UPDATE pybirdai_fnncl_asst_instrmnt
SET
    Financial_asset_instrument_has_Financial_asset_instrument_derived_data_id = NULL
WHERE
    rowid = 1;

DELETE FROM pybirdai_fnncl_asst_instrmnt_drvd_dt
WHERE
    rowid = 1;
