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


def test_is_out_of_order_columns(data):
    second_data = pd.DataFrame(
        data=[['x', 'y', 'z']],
        columns=['col_3', 'col_2', 'col_1']
    )
    left = spark.createDataFrame(data)
    right = spark.createDataFrame(second_data)

    assert_dataframe_equal(left, right, columns_order=False)


def test_is_not_equal_columns(data):
    second_data = pd.DataFrame(
        data=[['x', 'y', 'z']],
        columns=['col_x', 'col_y', 'col_z']
    )
    left = spark.createDataFrame(data)
    right = spark.createDataFrame(second_data)

    with pytest.raises(AssertionError, match="columns are not equal"):
        assert_dataframe_equal(left, right)
