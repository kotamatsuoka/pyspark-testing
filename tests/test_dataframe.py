from testing.dataframe import assert_dataframe_equal
from pyspark.sql import SparkSession
import pytest

spark = SparkSession.builder.getOrCreate()


@pytest.fixture
def data():
    return [("test", 1)]


def test_assert_frame_equal(data):
    left = spark.createDataFrame(data)
    right = spark.createDataFrame(data)

    assert_dataframe_equal(left, right)


def test_is_no_dataframe_instance(data):
    left = spark.createDataFrame(data)
    right = dict()

    with pytest.raises(AssertionError, match="right is not an DataFrame"):
        assert_dataframe_equal(left, right)
