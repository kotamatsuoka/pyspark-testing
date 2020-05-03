=====================
pyspark-testing
=====================
|PyPI pyversions| |GitHub license|

.. |PyPI pyversions| image:: https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue
   :target: https://www.python.org/

.. |GitHub license| image:: https://img.shields.io/github/license/Naereen/StrapDown.js.svg
   :target: https://github.com/Naereen/StrapDown.js/blob/master/LICENSE/

pyspark-testing is testing framework for pyspark


Installation
============
pyspark-testing is available at the `PyPI <https://pypi.org/project/pyspark-testing/>`_

::

    # PyPI
    $ pip install pyspark-testing



Basic Usage
===========

::

    from pyspark_testing import assert_dateframe_equal


    def test_sample():
        data = [('sample', 1)]

        left = spark.createDataFrame(data)
        right = spark.createDataFrame(data)

        assert_dataframe_equal(left, right)


License
=======
MIT License (see `LICENSE <https://github.com/kotamatsuoka/pyspark-testing/blob/master/LICENSE>`_).
