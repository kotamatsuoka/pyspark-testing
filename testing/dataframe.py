from pyspark.sql.dataframe import DataFrame


def assert_dataframe_equal(left, right, columns_order=True):
    """
    Check that left and right are equal.

    :param left: DataFrame
    :param right: DataFrame
    :param columns_order: bool

    - Check left and right are DataFrame instance
    - Check schema
    - Check data
    """
    assert isinstance(left, DataFrame), "left is not an DataFrame"
    assert isinstance(right, DataFrame), "right is not an DataFrame"

    if columns_order:
        assert left.schema == right.schema, "schema are not equal"
    else:
        assert left.schema == right.select(left.columns).schema, "schema are not equal"

    assert left.count() == left.join(right, left.columns, 'inner').count(), "data is not equal"
