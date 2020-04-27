from pyspark.sql.dataframe import DataFrame


def assert_dataframe_equal(left, right):
    """
    Check that left and right are equal.

    :param left: DataFrame
    :param right: DataFrame

    - Check left and right are DataFrame instance
    """
    assert isinstance(left, DataFrame), "left is not an DataFrame"
    assert isinstance(right, DataFrame), "right is not an DataFrame"
