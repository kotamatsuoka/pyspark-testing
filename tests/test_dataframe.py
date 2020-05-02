import pandas as pd
import pytest
from pyspark.sql import SparkSession

from testing.dataframe import assert_dataframe_equal

spark = SparkSession.builder.getOrCreate()


@pytest.fixture
def data():
    return pd.DataFrame(
        data=[['a', 'b', 'c'],
              ['x', 'y', 'z']],
        columns=['col_1', 'col_2', 'col_3']
    )


def test_assert_frame_equal(data):
    left = spark.createDataFrame(data)
    right = spark.createDataFrame(data)

    assert_dataframe_equal(left, right)


def test_is_no_dataframe_instance(data):
    left = spark.createDataFrame(data)
    right = dict()

    with pytest.raises(AssertionError, match="right is not an DataFrame"):
        assert_dataframe_equal(left, right)


def test_out_of_order_schema(data):
    second_data = pd.DataFrame(
        data=[['c', 'b', 'a'],
              ['z', 'y', 'x']],
        columns=['col_3', 'col_2', 'col_1']
    )
    left = spark.createDataFrame(data)
    right = spark.createDataFrame(second_data)

    assert_dataframe_equal(left, right, columns_order=False)


def test_not_equal_schema(data):
    second_data = pd.DataFrame(
        data=[['x', 'y', 'z']],
        columns=['col_x', 'col_y', 'col_z']
    )
    left = spark.createDataFrame(data)
    right = spark.createDataFrame(second_data)

    with pytest.raises(AssertionError, match="schema are not equal"):
        assert_dataframe_equal(left, right)


def test_not_equal_data(data):
    second_data = pd.DataFrame(
        data=[['a', 'b', 'invalid'],
              ['x', 'y', 'z']],
        columns=['col_1', 'col_2', 'col_3']
    )
    left = spark.createDataFrame(data)
    right = spark.createDataFrame(second_data)

    with pytest.raises(AssertionError, match="data is not equal"):
        assert_dataframe_equal(left, right)
