from pyspark.sql.dataframe import DataFrame


def assert_dataframe_equal(left, right, columns_order=True):
    """
    Check that left and right are equal.

    :param left: DataFrame
    :param right: DataFrame
    :param columns_order: bool

    - Check left and right are DataFrame instance
    - Check equal columns
    """
    assert isinstance(left, DataFrame), "left is not an DataFrame"
    assert isinstance(right, DataFrame), "right is not an DataFrame"

    if columns_order:
        assert left.columns == right.columns, "columns are not equal"
    else:
        assert left.columns == right.select(left.columns).columns, "columns are not equal"


