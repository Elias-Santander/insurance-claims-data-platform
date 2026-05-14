import great_expectations as gx
from etl.utils.logger import logger

def validate_claims(df):

    logger.info(
        "Starting claims data validation"
    )

    # ==================================================
    # CREATE GREAT EXPECTATIONS DATAFRAME
    # ==================================================

    gx_df = gx.from_pandas(df)

    # ==================================================
    # VALIDATIONS LIST
    # ==================================================

    validations = []

    # ==================================================
    # CLAIM ID NOT NULL
    # ==================================================

    validations.append(
        gx_df.expect_column_values_to_not_be_null(
            "claim_id"
        )
    )

    # ==================================================
    # CLAIM ID UNIQUE
    # ==================================================

    validations.append(
        gx_df.expect_column_values_to_be_unique(
            "claim_id"
        )
    )

    # ==================================================
    # CLAIM AMOUNT VALID RANGE
    # ==================================================

    validations.append(
        gx_df.expect_column_values_to_be_between(
            "claim_amount",
            min_value=1,
            max_value=100000
        )
    )

    # ==================================================
    # CLAIM STATUS VALID VALUES
    # ==================================================

    validations.append(
        gx_df.expect_column_values_to_be_in_set(
            "claim_status",
            [
                "OPEN",
                "IN_REVIEW",
                "APPROVED",
                "REJECTED",
                "CLOSED"
            ]
        )
    )

    # ==================================================
    # INCIDENT TYPE VALID VALUES
    # ==================================================

    validations.append(
        gx_df.expect_column_values_to_be_in_set(
            "incident_type",
            [
                "COLLISION",
                "THEFT",
                "GLASS_DAMAGE",
                "FLOOD",
                "FIRE",
                "VANDALISM"
            ]
        )
    )

    # ==================================================
    # CLAIM DATE NOT NULL
    # ==================================================

    validations.append(
        gx_df.expect_column_values_to_not_be_null(
            "claim_date"
        )
    )

    # ==================================================
    # FRAUD FLAG NOT NULL
    # ==================================================

    validations.append(
        gx_df.expect_column_values_to_not_be_null(
            "fraud_flag"
        )
    )

    # ==================================================
    # CHECK FAILED VALIDATIONS
    # ==================================================

    failed_validations = [
        validation
        for validation in validations
        if validation["success"] is False
    ]

    # ==================================================
    # VALIDATION SUMMARY
    # ==================================================

    validation_results = {
        "total_validations":
            len(validations),
        "failed_validations":
            len(failed_validations),
        "success":
            len(failed_validations) == 0
    }

    logger.info(validation_results)

    # ==================================================
    # HANDLE FAILURES
    # ==================================================

    if failed_validations:
        logger.error(
            f"Validation failed: "
            f"{len(failed_validations)} checks failed"
        )
        for failure in failed_validations:

            logger.error(failure)
        raise Exception(
            "Data validation failed"
        )

    # ==================================================
    # SUCCESS
    # ==================================================

    logger.info(
        "All validations passed successfully"
    )

    return True